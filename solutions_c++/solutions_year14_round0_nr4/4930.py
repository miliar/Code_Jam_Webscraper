#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
using namespace std;
typedef  long long LL;          
const int N = 105;
const int M = 20005;
const int INF = 1000000007;
int n ;
double a[N] , b[N];

int main () {
	#ifndef ONLINE_JUDGE
        freopen ("input.txt" , "r" , stdin);                                           
        freopen ("output.txt" , "w" , stdout);
    #endif
    int t , cas = 0;
    scanf ("%d" , &t);
    while (t --) {
        set <double> myset1 , myset2;
        int ans = 0 , ret = 0;
        scanf ("%d" , &n);
        for(int i = 0 ; i < n ; i ++) {
            scanf ("%lf" , &a[i]);
        }
        for(int i = 0 ; i < n ; i ++) {
            scanf ("%lf" , &b[i]);
        }
        set <double>:: iterator it,tt;
        myset1.clear();
        myset2.clear();
        for(int i = 0 ; i < n ; i++) {
            myset1.insert (a[i]);
            myset2.insert (b[i]);
        }
        for(it = myset1.begin () ; it != myset1.end() ; it ++) {
            double num = *it;
            tt = myset2.lower_bound (num);
            if(tt != myset2.end ())
                myset2.erase ((*tt));
            else {
                tt = myset2.begin();
                ans++;
                myset2.erase ((*tt));
            }
        }
        myset1.clear();
        myset2.clear();
        for(int i = 0 ; i < n ; i++) {
            myset1.insert (a[i]);
            myset2.insert (b[i]);
        }
        for (it = myset1.begin() ; it != myset1.end() ; it ++) {
            double num = *it;
            if(num > (*myset2.begin())) {
                ret ++;
                tt = myset2.begin();
                myset2.erase ((*tt));
            }else {
                tt = --myset2.end();
                myset2.erase((*tt));
            }
        }
        printf("Case #%d: %d %d\n" , ++ cas , ret , ans);
    }
    return 0;
}