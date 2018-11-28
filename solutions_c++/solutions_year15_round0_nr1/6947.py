/* V-Sat Template */

//#include <bits/stdc++.h>
#include <string>
#include <algorithm>
#include <utility>
#include <iostream>
#include <sstream>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <cstring>
#include <cstdio>
#include <cmath>

#define FOR(i, a, b) for (int i = a; i <= b; ++i)
#define FORD(i, a, b) for (int i = a; i >= b; --i)
#define FORN(i, n) for (int i = 0; i < n; ++i)

#define MAX(a,b) (a > b ? a : b)
#define MIN(a,b) (a < b ? a : b)
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define VI vector<int>
#define PI pair<int, int>
#define VVI vector<VI>
#define VPI vector<PI>

#define debug(i) cout << i << endl

using namespace std;

#define ll long long

const ll MOD = 1e9+7;

ll gcd(ll a, ll b) { return b ? gcd(b, a%b) : a; }
ll lcm(ll a, ll b) { return a/gcd(a, b)*b; }
ll power(ll a, ll b, ll mod = MOD) {
    if (b == 0) return 1;
    else {
        ll temp = power(a, b >> 1, mod);
        temp *= temp;
        temp %= mod;
        if (b&1)
            temp *= a;
        temp %= mod;
        return temp;
    }
}
ll inv(ll a, ll mod = MOD) { return power(a, mod-2); }

template <class T>
inline string to_str (const T& t) {
    stringstream ss;
    ss << t;
    return ss.str();
}
template <class T>
inline ll to_ll (const T& t) {
    stringstream ss;
    ll val;
    ss.str(t);
    ss >> val;
    return val;
}


int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    /* Code starts here */

    long long n;
    cin >> n;
    for (long long i = 0; i < n; ++i) {
        long long max;
        string s;
        cin >> max;
        char c;
        cin.get(c);
        cin >> s;
        long long total = 0, req = 0;
        for (long long j = 0; j < s.length(); ++j) {
            long long x = s[j]-'0';
            if (j > total && x > 0) {
                long long addition = j-total;
                req += addition;
                total += addition;
            }
            total += x;
        }
        cout << "Case #" << i+1 << ": " << req << endl;
    }

    /* End of code */
    return 0;
}
