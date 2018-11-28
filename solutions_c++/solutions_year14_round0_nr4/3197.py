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
int decietful_war(set <double> naomi_masses, set <double> ken_masses, int N)
{
    int count = 0;
    while(naomi_masses.size()>0){
        // printf("decietful_war loop\n");
        while(naomi_masses.size()>0 && *ken_masses.rbegin() > *naomi_masses.rbegin()){
            auto ken_it = ken_masses.lower_bound(*naomi_masses.rbegin());
           // cout << "ken_it: " << *ken_it << endl;
            ken_masses.erase(ken_it);
            naomi_masses.erase(*naomi_masses.begin());
        }
        if(naomi_masses.size()==0){
            break;
        }
        count++;
        auto nao_it = naomi_masses.lower_bound(*ken_masses.begin());
        // cout << "*ken_masses.begin(): " << *ken_masses.begin() << endl;
        if(nao_it == naomi_masses.end()){
            cout << "nao_it: end" << endl;
        }
        // cout << "nao_it: " << *nao_it << endl;
        naomi_masses.erase(nao_it);
        ken_masses.erase(*ken_masses.begin());
    }
    return count;
}
int war(set <double> naomi_masses, set <double> ken_masses, int N)
{
    int count = 0;
    // cout << "=====war=======" << endl;
    while(naomi_masses.size()>0){
        auto ken_it = ken_masses.lower_bound(*naomi_masses.rbegin());
        // cout << "*naomi_masses.rbegin(): " << *naomi_masses.rbegin() << endl;
        // cout << "ken_it:" << *ken_it << endl;
        if(ken_it != ken_masses.end()){
            ken_masses.erase(*ken_it);
        }else{
            count++;
            ken_masses.erase(*ken_masses.begin());
        }
        
        naomi_masses.erase(*naomi_masses.rbegin());
        
    }
    return count;
}

pair<int, int> testcase_itr(const set <double> & naomi_masses, const set <double> &ken_masses, int N)
{
    int result1 = decietful_war(naomi_masses, ken_masses, N);
    int result2 = war(naomi_masses, ken_masses, N);
    return make_pair(result1, result2);
    
}
pair<int, int>  testcase(istream &in, int t)
{
    int N;
    in >> N;
    set <double> naomi_masses;
    for(int i=0;i<N;i++){
        double mass;
        in >> mass;
        naomi_masses.insert(mass);
    }
    set <double> ken_masses;
    for(int i=0;i<N;i++){
        double mass;
        in >> mass;
        ken_masses.insert(mass);
    }
    
   // cout << "Naomi: ";
   // for(auto mass:naomi_masses){
   //     cout << mass << " ";
   // }
   // cout << endl;
    
   // cout << "Ken: ";
   // for(auto mass:ken_masses){
   //     cout << mass << " ";
   // }
   // cout << endl;

    return testcase_itr(naomi_masses, ken_masses, N);
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
        cout << "Case #" << t+1 << ": " << result.first << " " << result.second << endl;
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


