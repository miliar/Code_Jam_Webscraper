//
//  main.cpp
//  googlecodejam
//
//  Created by Yoshioka Tsuneo on 4/12/14.
//  Copyright (c) 2014 Yoshioka Tsuneo. All rights reserved.
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

#include <thread>

#define decltype(X) __typeof(X)
#define REP(i, n) for(int i=0; i<(int)n; i++)
#define FOR(it, c) for(decltype((c).begin()) it = (c).begin(); it!=(c).end(); it++)
#define ALL(c) (c).begin(), (c).end()

#define EPS 0.000001
using namespace std;

typedef long long ll;

#include <mutex>
#include <condition_variable>
using namespace std;

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



//string testcase_itr(vector<int> graph)
//{
//}


ll  testcase(istream &in, int t)
{
    int N;
    in >> N;
    vector<ll> vals;
    for(int i=0;i<N;i++){
        ll val;
        in >> val;
        vals.push_back(val);
    }
    int left = 0, right = N-1;
    int count = 0;
    // printf("N=%d\n", N);
    for(int i=0;i<N;i++){
        auto it = min_element(vals.begin()+left, vals.begin()+right+1);
        int index = (int)(it - vals.begin());
        // printf("index=%d, left=%d, right=%d\n", index, left, right);
        if(index-left < right-index){
            while(index > left){
                swap(vals[index], vals[index-1]);
                index--;
                count++;
            }
            left++;
        }else{
            while(index<right){
                swap(vals[index], vals[index+1]);
                index++;
                count++;
            }
            right--;
        }
    }
    
    return count;
    //int A, B, K;
    //in >> A >> B >> K;
    //return testcase_itr(A, B, K);
}


// #define MULTI_THREAD

#ifdef MULTI_THREAD
semaphore sem(6);
vector< pair<bool, double> > g_results;

void testcase_for_multithread(int t, double C, double F, double X)
{
    g_results[t].second = testcase_itr(C, F, X);
    g_results[t].first = true;
    // sleep(rand()/(RAND_MAX/3.0));
    sem.notify();
}
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
    }
    ifstream in(fname);
    if(!in){
        cout << "File open error:" << fname << endl;
        exit(1);
    }
    int T;
    in >> T;
    
#ifndef MULTI_THREAD
    for(int t=0;t<T;t++){
        auto result = testcase(in, t);
        cout << "Case #" << t+1 << ": " << result << endl;
        // return 0;
    }
#else
    vector<thread> threads;
    g_results.resize(T);
    int cur_result = 0;
    for(int t=0;t<T;t++){
        sem.wait();
        while(g_results[cur_result].first == true){
            cout << "Case #" << cur_result+1 << ": " << g_results[cur_result].second << endl;
            cur_result++;
        }
        double C, F, X;
        
        in >> C >> F >> X;
        
        // thread th(testcase_for_multithread, t, C, F, X );
        threads.push_back(thread(testcase_for_multithread, t, C, F, X ));
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
#endif
    // std::cout << "Hello, World!\n";
    return 0;
}


