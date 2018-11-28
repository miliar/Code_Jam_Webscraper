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

bool ok(int num, const vector<int> &ps)
{
    if(num==7){
        sleep(0);
    }
    int N = (int)ps.size();
    for(int sc=0;sc<num;sc++){
        int sc2 = sc;
        int nsc = num - sc;
        for(int i=0;i<N;i++){
            int p = ps[i];
            int sc3 = (p-1)/nsc;
            sc2 -= sc3;
        }
        if(sc2>=0){
            return true;
        }
    }
    return false;
    /*
    
    priority_queue<int> pq;
    for(auto v:ps){
        pq.push(v);
    }
    for(int i=0;i<num;i++){
        int left = num - i;
        int topnum = pq.top() - i;
        if(topnum <= left){
            return true;
        }
        if(topnum>=2){
            pq.pop();
            int nextval = (topnum-(left-1));
            int pushval = nextval + (i+1);
            pq.push(pushval);
        }
    }
    return false;
     */
}

string testcase_itr(int X, string str_)
{
    map<char, map<char, pair<int, char>> > cmap;
    cmap['1']['1'] = make_pair(1, '1');
    cmap['1']['i'] = make_pair(1, 'i');
    cmap['1']['j'] = make_pair(1, 'j');
    cmap['1']['k'] = make_pair(1, 'k');

    cmap['i']['1'] = make_pair(1, 'i');
    cmap['i']['i'] = make_pair(-1, '1');
    cmap['i']['j'] = make_pair(1, 'k');
    cmap['i']['k'] = make_pair(-1, 'j');
    
    cmap['j']['1'] = make_pair(1, 'j');
    cmap['j']['i'] = make_pair(-1, 'k');
    cmap['j']['j'] = make_pair(-1, '1');
    cmap['j']['k'] = make_pair(1, 'i');

    cmap['k']['1'] = make_pair(1, 'k');
    cmap['k']['i'] = make_pair(1, 'j');
    cmap['k']['j'] = make_pair(-1, 'i');
    cmap['k']['k'] = make_pair(-1, '1');
    
    
    
    // solution start
    string str;
    for(int i=0;i<X;i++){
        str.append(str_);
    }
    int N = (int)str.size();

    vector< vector< pair<int, char> > > fromto(N, vector< pair<int, char> >(N));
    for(int i=0;i<N;i++){
        char c = '1';
        int sign = 1;
        for(int j=i;j<N;j++){
            auto mret = cmap[c][str[j]];
            c = mret.second;
            sign = sign * mret.first;
            fromto[i][j] = make_pair(sign, c);
        }
    }
    
    for(int i=1;i<N;i++){
        auto mret0 = fromto[0][i-1];
        char c0=mret0.second;
        int sign0 =mret0.first;
        if(!(c0=='i' && sign0 == 1)){
            continue;
        }
        for(int j=i+1;j<N;j++){
            auto mret1 = fromto[i][j-1];
            char c1=mret1.second;
            int sign1 =mret1.first;
            if(!(c1=='j' && sign1 == 1)){
                continue;
            }
            
            auto mret2 = fromto[j][N-1];
            char c2=mret2.second;
            int sign2 =mret2.first;
            if(!(c2=='k' && sign2 == 1)){
                continue;
            }
            
            return string("YES");
            
            
        }
    }
    
    // solution end
    
    return string("NO");
}
void testcase(istream &in)
{
    int T;
    in >> T;
    for(int i=0;i<T;i++){
        int L, X;
        string str;
        in >> L >> X >> str;
        auto ret = testcase_itr(X, str);
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



