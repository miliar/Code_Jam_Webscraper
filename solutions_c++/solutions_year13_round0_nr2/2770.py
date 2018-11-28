// -*- C++ -*-
// File: lawnmower.cpp
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

/*** TEMPLATE CODE ENDS HERE */

int a[111][111];
int mi[111], mj[111];
int N,M;

int main() {
#ifdef LOCAL_HOST
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif

    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;

    FOR(cs,1,T+1) {
        cin >> N >> M;
        rep(i,N)  rep(j,M) cin >> a[i][j];

        rep(i,N) {
            mi[i] = a[i][0];
            rep(j,M) mi[i] = min(mi[i], a[i][j]);
        }

        rep(j,M) {
            mj[j] = a[0][j];
            rep(i,N) mj[j] = min(mj[j], a[i][j]);
        }

        rep(i,N) rep(j,M) {

            if(a[i][j] != mi[i] && a[i][j] != mj[j]) continue;

            bool ok1 = true;
            rep(k,N) if(k!=i) ok1 &= a[k][j] == a[i][j];

            bool ok2 = true;
            rep(k,M) if(k!=j) ok2 &= a[i][k] == a[i][j];

            if(!(ok1||ok2)) {
                cout << "Case #" << cs << ": NO" << endl;
                goto AAA;
            }
        }
        cout << "Case #" << cs << ": YES" << endl;
    AAA:;
    }

// #ifdef LOCAL_HOST
//     printf("TIME: %.3lf\n",double(clock())/CLOCKS_PER_SEC);
// #endif

    return 0;
}
