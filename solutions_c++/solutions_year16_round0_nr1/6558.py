//
//  code.cpp
//  One Punch AC
//
//  Created by user on 3/8/16.
//  Copyright © 2016 user. All rights reserved.
//


#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <deque>
#include <algorithm>
#include <queue>
#include <cmath>
#include <map>
#include <complex>
#include <cstring>

using namespace std;
#define rep(i, a, b) for(int i = (a); i < (b); i++)
#define repd(i, a, b) for(int i = (a); i > (b); i--)
#define forIt(it, a) for(__typeof((a).begin()) it = (a).begin(); it != (a).end(); it++)
#define forRev(it, a) for(__typeof((a).rbegin()) it = (a).rbegin(); it != (a).rend(); it++)
#define ll long long
#define ld long double
#define fi first
#define se second
#define mk make_pair
#define pb push_back
#define sz(a) (a).size()
#define all(a) (a).begin(), (a).end()
#define Rep(i,n) for(int i = 0; i < (n); ++i)

typedef complex<ld> cplex;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef pair<ii, int> iii;
typedef vector<ii> vii;
typedef vector<iii> viii;

const int N = 1000000 + 7;
const int M = 107;
const int mod = 998244353;
const int inf = 1e9 + 7;
const double pi = acos(-1);
const int maxn = N * 2;
const double PI = acos(-1);


string s;

bool check[10];

int get(int x) {
    rep(i, 0, 10) check[i] = 0;
    int cnt = 0;
    int fir = 0;
    while (cnt < 10) {
        fir += x;
        //cout << fir << "\n";
        //cout << x << " " << fit << "\n";
        int nw = fir;
        while (nw > 0) {
            //cout << nw << " ";
            int cur = nw % 10;
            if (!check[cur]) {
                cnt++;
                check[cur] = 1;
            }
            nw /= 10;
        }
        if (cnt == 10) return fir;
    }
    return -1;
}

void solve() {
    int n;
    cin >> n;
    if (n == 0)
        puts("INSOMNIA");
    else cout << get(n) << "\n";
    
}



int main() {
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin); freopen("out.txt", "w", stdout);
#endif
    
    int T = 1;
    cin >> T;
    rep(i, 1, T + 1) {
        printf("Case #%d: ", i);
        solve();
        //puts("");
    }
}