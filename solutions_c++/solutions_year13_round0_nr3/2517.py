// -*- C++ -*-
// File: fairandsquare.cpp
// Copyright (C) 2013
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <numeric>
#include <memory.h>
#include <cstdio>
#include <assert.h>

using namespace std;

#define pb push_back
#define INF 1011111111
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define rep(i,n) FOR(i,0,n)
#define CL(a,v) memset((a),(v),sizeof(a))
#define mp make_pair
#define X first
#define Y second
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))

typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> pii;
typedef vector<ll> VL;
/*** TEMPLATE CODE ENDS HERE */

bool is_palindrome(ll x) {
    static int a[16];
    int n = 0;
    while(x) {
        a[n++] = x%10;
        x /= 10;
    }
    rep(i,n/2) if(a[i]!=a[n-i-1]) return false;
    return true;
}

VL get_palindromes() {
    ll x = 1;
    const ll maxn = ll(1e14);
    VL a;
    for(; x*x <= maxn; ++x) {
        if(is_palindrome(x) && is_palindrome(x*x))
            a.pb(x*x);
    }
    return a;
}

int main() {
#ifdef LOCAL_HOST
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif

    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;

    VL p = get_palindromes();
    ll A,B;
    const ll inf = 1LL<<60;
    p.pb(inf);

    int cs = 1;
    while(T--) {
        cin >> A >> B;
        int cnt = 0;
        rep(i,p.size()) if(A <= p[i] && p[i] <= B) cnt++;
        cout << "Case #" << cs++ << ": " << cnt << endl;
    }

// #ifdef LOCAL_HOST
//     printf("TIME: %.3lf\n",double(clock())/CLOCKS_PER_SEC);
// #endif

    return 0;
}
