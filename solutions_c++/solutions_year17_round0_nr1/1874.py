//
//  main.cpp
//  googlecodejam2017
//
//  Created by Yoshioka Tsuneo on 2017/04/08.
//  Copyright © 2017年 Yoshioka Tsuneo. All rights reserved.
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


void flip(char &c)
{
    if(c=='-'){
        c = '+';
    }else{
        c = '-';
    }
}
int testcase_itr(string &s, int k)
{
    // solution start
    int N = (int)s.size();
    int count = 0;
    for(int i=0; i<N-(k-1); i++){
        if(s[i] == '-'){
            count ++;
            for(int j=i;j<i+k;j++){
                // char & c = s[j];
                flip(s[j]);
            }
        }
    }
    if(s.find('-') != -1){
        return -1;
    }
    return count;
}
void testcase(istream &in)
{
    int T;
    in >> T;
    for(int i=0;i<T;i++){
        string s;
        int k;
        in >> s >> k;
        auto ret = testcase_itr(s, k);
        if(ret == -1){
            cout << "Case #" << i+1 << ": IMPOSSIBLE" <<  endl;
        }else{
            cout << "Case #" << i+1 << ": " << ret << endl;
        }
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

