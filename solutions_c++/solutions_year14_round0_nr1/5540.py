// -*- C++ -*-
// File: a.cpp
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

int main() {
#ifdef LOCAL_HOST
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif

    ios_base::sync_with_stdio(false);
    
    int T;
    cin >> T;
    
    int a[4][4], b[4][4], A, B;
    
    FOR(cs,1,T+1) {
        cin >> A; --A;
        rep(i,4) rep(j,4) cin >> a[i][j];
        cin >> B; --B;
        rep(i,4) rep(j,4) cin >> b[i][j];
        
        bool was[22];
        CL(was,0);
        int cnt = 0;
        
        rep(i,4) was[ a[A][i] ] = true;
        rep(i,4) cnt += was[ b[B][i] ];
        
        if(cnt == 0) {
            cout << "Case #" << cs << ": " << "Volunteer cheated!";
            if(cs!=T) cout << endl;
        }else if(cnt==1) {
            int num = -1;
            rep(i,4) if(was[b[B][i]]) {
                num = b[B][i];
                break;
            }
            cout << "Case #" << cs << ": " << num;
            if(cs!=T) cout << endl;
        }
        else {
            cout << "Case #" << cs << ": " << "Bad magician!";
            if(cs!=T) cout << endl;
        }
    }

    return 0;
}
