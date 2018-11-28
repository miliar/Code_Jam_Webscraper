#include <stdio.h>
#include <unistd.h>
#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#define _USE_MATH_DEFINES
#include <math.h>
#include <assert.h>
#include <cstdlib>
#include <algorithm>
#include <list>

#define forn(i,n) for (int i=0;i<n;i++)
#define rforn(i,n) for (int i=n-1;i>=0;i--)
#define mp(a,b) make_pair(a,b)
#define LL long long
#define S(n) scanf("%d", &n)
#define Sa(n,i) scanf("%lf", n+i)
#define N 1000
#define MOD 1000000007
#define EPS 0.00000001

using namespace std;

double a[N], b[N];
bool used[N];


pair<int, int> solve_small(int n){
    sort(a, a + n);
    sort(b, b + n);
    memset(used, 0, sizeof(bool) * n);
    int x = 0, y = 0;
    forn(i, n){
        int j = 0;
        for(; j < n && (used[j] || b[j] < a[i]); ++j);
        if(j == n){
            x += 1;
            for(j=0; j < n && used[j]; ++j);
            used[j] = true;
        }else{
            used[j] = true;
        }
    }
    memset(used, 0, sizeof(bool) * n);
    forn(i, n){
        int j = 0;
        for(; j < n && (used[j] || a[j] < b[i]); ++j);
        if(j == n){
            for(j=0; j < n && used[j]; ++j);
            used[j] = true;
        }else{
            y += 1;
            used[j] = true;
        }
    }
    return mp(y, x);
}


int main(){
#ifndef ONLINE_JUDGE
    //freopen("input.txt","rt",stdin);
    freopen("/Users/ramis/Downloads/D-large.in","rt",stdin);
    freopen("output.txt","wt",stdout);
#endif
    
    int T;
    S(T);
    
    for(int _t=1; _t <= T; ++_t){
        int n; S(n);
        forn(i, n) Sa(a, i);
        forn(i, n) Sa(b, i);
        pair<int, int> res = solve_small(n);
        printf("Case #%d: %d %d\n", _t, res.first, res.second);
    }
    
    
    return 0;
}

