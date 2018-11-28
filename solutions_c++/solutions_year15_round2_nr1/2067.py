//
//  main.cpp
//  googlecodejam2015
//
//  Created by Yoshioka Tsuneo on 2015/04/11.
//  Copyright (c) 2015年 Yoshioka Tsuneo. All rights reserved.
//

#include <fstream>
#include <iostream>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <numeric>
#include <algorithm>
#include <sstream>
#include <queue>
#include <stdexcept>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cassert>
#include <unistd.h>
#include <string.h>

#include <stack>

// #define MULTI_THREAD

#ifdef MULTI_THREAD
#include <thread>
#endif

#define decltype(X) __typeof(X)
#define REP(i, n) for(int i=0; i<(int)n; i++)
#define FOR(it, c) for(decltype((c).begin()) it = (c).begin(); it!=(c).end(); it++)
#define ALL(c) (c).begin(), (c).end()

#define EPS 0.000001
using namespace std;

typedef long long ll;

ll get_num_digits(ll n)
{
    ll count = 0;
    while(n>0){
        n /= 10LL;
        count++;
    }
    return count;
}
ll num_reverse(ll n)
{
    ll result = 0;
    while(n>0){
        result *= 10;
        result += (n%10);
        
        n/=10;
    }
    return result;
}
ll get_opt_num(ll digits)
{
    ll result = 1;
    for(ll d=1;d<digits/2;d++){
        result *=10;
    }
    for(ll d=digits/2;d<digits;d++){
        result *=10;
        result +=9;
    }
    return result;
}
ll get_opt_num2(ll num)
{
    ll digits = get_num_digits(num);
    ll result = 1;
    num /= 10;
    for(ll d=1;d<digits/2;d++){
        result *=10;
        num /= 10;
    }
    for(ll d=digits/2;d<digits;d++){
        result *=10;
        result += (num%10);
        num /= 10;
    }
    return result;

}
ll get_final_count(ll cur_num, ll n)
{
    ll to_num = get_opt_num2(n);
    ll count = 0;
    if(to_num<n){
        ll rev_num = num_reverse(to_num);
        
        if(rev_num>to_num && rev_num<=n){
            count += (to_num - cur_num);
            count += 1;
            cur_num = rev_num;
        }
    }
    count += (n - cur_num);
    return count;
}
ll testcase_itr(ll n)
{
    if(n<=10){
        return n;
    }
    
    ll num_digits = get_num_digits(n);
    // solution start
    ll count = 10;
    ll cur_num = 10;
    
    for(ll d=2;d<num_digits;d++){
        ll to_num = get_opt_num(d);

        count += (to_num - cur_num);
        count += 1;
        cur_num = num_reverse(to_num);
    }

    ll count1 = get_final_count(cur_num, n);
    if(get_num_digits(n)==get_num_digits(n-1)){
        ll count2 = get_final_count(cur_num, n-1);
        return min(count1, count2+1) + count;
    }
    return count1 + count;
}
void testcase(istream &in)
{
    int T;
    in >> T;
    for(int i=0;i<T;i++){
        ll n;
        in >> n;
        auto ret = testcase_itr(n);
        cout << "Case #" << i+1 << ": " << ret << endl;
    }
}

#ifdef MULTI_THREAD
void testcase_multi(istream &in);
#endif

int main(int argc, const char * argv[])
{
    // sleep(1000);
    // insert code here...
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.precision(15);
    string fname = "/dev/stdin";
    if(argc>=2){
        fname = argv[1];
        ifstream in(fname, ifstream::in);
        if(!in){
            cout << "File open error:" << fname << endl;
            exit(1);
        }
#ifdef MULTI_THREAD
        testcase_multi(in);
#else
        testcase(in);
#endif
        /*
         int result = testcase(in);
         cout << result << endl;
         */
    }else{
#ifdef MULTI_THREAD
        testcase_multi(cin);
#else
        testcase(cin);
#endif
        /*
         int result = testcase(cin);
         cout << result << endl;
         */
        
    }
    return 0;
}

#ifdef MULTI_THREAD
class semaphore{
private:
    mutex mtx;
    condition_variable cv;
    int count;
    
public:
    semaphore(int count_ = 0):count(count_){;}
    void notify()
    {
        unique_lock<mutex> lck(mtx);
        ++count;
        cv.notify_one();
    }
    void wait()
    {
        unique_lock<mutex> lck(mtx);
        
        while(count == 0){
            cv.wait(lck);
        }
        count--;
    }
};
semaphore sem(6);
vector< pair<bool, double> > g_results;

void testcase_for_multithread(int t, int M, int N, vector<string> X)
{
    g_results[t].second = testcase_itr(C, F, X);
    g_results[t].first = true;
    // sleep(rand()/(RAND_MAX/3.0));
    sem.notify();
}

void testcase_multi(istream &in)
{
    int T;
    in >> T;
    
    vector<thread> threads;
    g_results.resize(T);
    int cur_result = 0;
    for(int t=0;t<T;t++){
        sem.wait();
        while(g_results[cur_result].first == true){
            cout << "Case #" << cur_result+1 << ": " << g_results[cur_result].second << endl;
            cur_result++;
        }
        
        int M, N;
        in >> M >> N;
        vector<string> ma;
        for(int i=0;i<M;i++){
            string line;
            in >> line;
            ma.push_back(line);
        }
        threads.push_back(thread(testcase_for_multithread, t, M, N, ma ));
        
    }
    while(cur_result<T){
        sem.wait();
        while(g_results[cur_result].first == true){
            cout << "Case #" << cur_result+1 << ": " << g_results[cur_result].second << endl;
            cur_result ++;
        }
    }
    for(int t=0;t<T;t++){
        threads[t].join();
    }
    
}
#endif



