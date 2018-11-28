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


int testcase_itr(int R, int C, vector<string> m)
{
    vector<int> left(R, -1), right(R, -1);
    vector<int> up(C, -1), down(C, -1);
    // solution start
    for(int r=0;r<R;r++){
        for(int c=0;c<C;c++){
            if(m[r][c]!='.'){
                left[r] = c;
                break;
            }
        }
        for(int c=C-1;c>=0;c--){
            if(m[r][c]!='.'){
                right[r] = c;
                break;
            }
        }
    }
    for(int c=0;c<C;c++){
        for(int r=0;r<R;r++){
            if(m[r][c]!='.'){
                up[c] = r;
                break;
            }
        }
        for(int r=R-1;r>=0;r--){
            if(m[r][c]!='.'){
                down[c] = r;
                break;
            }
        }
    }
    for(int r=0;r<R;r++){
        for(int c=0;c<C;c++){
            if(m[r][c] != '.'){
                if(left[r]==c && right[r]==c && up[c]==r && down[c]==r){
                    return -1;
                }
            }
        }
    }
    int count = 0;
    for(int r=0;r<R;r++){
        {
            int c = left[r];
            if(c!=-1){
                if(m[r][c]=='<'){
                    count++;
                }
            }
        }
        {
            int c = right[r];
            if(c!=-1){
                if(m[r][c]=='>'){
                    count++;
                }
            }
        }
    }
    for(int c=0;c<C;c++){
        {
            int r = up[c];
            if(r!=-1){
                if(m[r][c]=='^'){
                    count++;
                }
            }
        }
        {
            int r = down[c];
            if(r!=-1){
                if(m[r][c]=='v'){
                    count++;
                }
            }
        }
    }
    
    
    // solution end
    
    return count;
}
void testcase(istream &in)
{
    int T;
    in >> T;
    for(int i=0;i<T;i++){
        int R, C;
        in >> R >> C;
        vector<string> m(R);
        for(int r=0;r<R;r++){
            in >> m[r];
        }
        auto ret = testcase_itr(R, C, m);
        if(ret==-1){
            cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
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



