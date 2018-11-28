#include <bits/stdc++.h>
/*
#include <iostream>
#include <cstring>
#include <climits>
#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <map>
*/
#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair
#define fst first
#define scd second
#define f(x, let) for(int let=0; let<x; let++)
#define ms(x, v) memset(x, v, sizeof x)
using namespace std;
typedef long long ll;
typedef pair<int, int> pi;
typedef vector<int> vi;
typedef vector<pair<int, int> > vpi;
typedef set<int> si;
typedef set<int>::iterator sit;
const int MOD = 1000000007;
const int OO = 1000000000;
//REMEMBER LONG LONG INT
//REMEMBER TO INITIALZE THINGS
ll notprime (ll n) {
    ll x = 2;
    while (x*x <= n) {
        if (n % x == 0) return x;
        x++;
    }
    return n;
}

ll convert (ll n, ll b) {
    ll ans = 0, aux = 1;
    while (n > 0) {
        ans += (n % 2) * aux;
        n /= 2;
        aux *= b;
    }
    return ans;
}

int main(){
    std::ios::sync_with_stdio(false);
    int t, m, j;
    cin >> t >> m >> j;
    ll n = (1 << m-1) + 1;
    cout << "Case #1:" << endl;
    int answers = 0;
    while (answers < j) {
        vector<ll> v;
        for (ll i = 2; i <= 10; i++) {
            ll x = convert(n, i);
            ll y = notprime (x);

            if (y != x) {
                v.pb (y);
            }
        }
        if (v.size () == 9) {
            answers++;
            cout << convert (n, 10);
            f (v.size (), i) {
                cout << " " << v[i];
            }
            cout << endl;
        }
        n += 2;
    }
}
