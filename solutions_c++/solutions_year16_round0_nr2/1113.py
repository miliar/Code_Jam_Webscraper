#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <algorithm> // max...
#include <utility> // pair
#include <complex>
#include <climits> // int, ll...
#include <limits> // double...
#include <cmath> // abs, atan...
#include <cstring> // memset
#include <string>
#include <functional> // greater, less...
#include <bitset>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<int, double> id;
typedef pair<double, int> di;
typedef pair<ll, ll> ll_ll;
typedef pair<double, double> dd;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<ll> vll;
typedef vector<ii> vii;
typedef vector<dd> vdd;
typedef vector<id> vid;
typedef vector<vi> vvi;
typedef map<int, int> mii;
typedef map<int, ll> mil;
typedef map<ll, ll> mll;

//#define ONLINE_JUDGE

int main() {
#ifdef ONLINE_JUDGE
    freopen("X-small-practice.in", "r", stdin);
        freopen("X-small-practice.out", "w", stdout);
        //freopen("X-large-practice.in", "r", stdin);
        //freopen("X-large-practice.out", "w", stdout);
#endif

#ifndef ONLINE_JUDGE
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
#endif
    int T;
    cin >> T; cin.get();
    for (int t = 1; t <= T; t++) {
        string s; getline(cin, s);
        int flips = 0;
        //cout << s << endl;

        while (true) {
            char ini = s[0];
            char opp = (ini == '+' ? '-' : '+');
            int i = 0;
            while (i < s.length() && s[i] == ini) {
                s[i] = opp;
                i++;
            }
            if (i == s.length() && ini == '+') break;
            flips++;
        }

        printf("Case #%d: %d\n", t, flips);
    }

    return 0;
}