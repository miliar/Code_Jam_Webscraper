/*
Author : SRIRAM S
*/
// Libs 
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <cstring>
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,A,n) for(int i=A;i<n;i++)
#define sz(c) (signed int) c.size()
#define pb(c) push_back(c)
#define INF (int) 1e9
#define all(c) c.begin(),c.end()
#define GI(t) scanf("%d",&t)
#define VI vector<int>
#define PII pair <int,int>
typedef long long LL;

using namespace std;

int main() {
    int t;
    double C,F,X;
    GI(t);
    REP(te,t) {
        scanf("%lf %lf %lf",&C,&F,&X);
        double total_time = 0;
        double num_farms = 0;
        double num_cookies = 0;
        while(1) {
            double first = X / (num_farms * F + 2);
            double second = C / (num_farms * F + 2) + X / ((num_farms+1) * F + 2);
            //cout<<first<<" "<<second<<" "<<total_time<<endl;
            if(first <= second) {
                total_time += first;
                break;
            }
            else {
                total_time += C / (num_farms * F + 2);
                ++num_farms;
            } 
        }
        printf("Case #%d: %.7lf\n",te+1,total_time);
    }
    return 0;
}
