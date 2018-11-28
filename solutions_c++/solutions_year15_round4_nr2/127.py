#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <vector>
#include <cassert>
#include <queue>
#include <sstream>
#include <set>
#include <functional>
#include <cfloat>
#include <unordered_map>
#include <ctime>
#include <complex>
#include <cmath>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef complex<double> cd;
#define mp make_pair                                                  

const ll MN = 21000;
const ll mod = 1e9 + 7;

void solve()
{
    cout.setf(ios::fixed);
    cout.precision(12);
    int n;
    cin >> n;
    double V, T;
    vector<double> t(n);
    vector<double> s(n);
    cin >> V >> T;
    for (int i = 0; i < n; ++i)
        cin >> s[i] >> t[i];
    if (n == 1)
    {
        if (t[0] == T)
        {
            cout << V / s[0];
        }
        else
        {
            cout << "IMPOSSIBLE";
        }
        return;
    }

    if (t[0] == t[1])
    {
        if (t[0] == T)
        {
            cout << V / (s[0] + s[1]);
        }
        else
        {
            cout << "IMPOSSIBLE";
        }
        return;
    }

    double V2 = (V * T - V * t[0]) / (t[1] - t[0]);
    double V1 = V - V2;
    double res = max(V1 / s[0], V2 / s[1]);
    if (t[0] < T && t[1] < T || t[0] > T && t[1] > T)
    {
        cout << "IMPOSSIBLE";
    }
    else
    {
        cout << res;
    }
}

int main()
{
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cout << "Case #" << i + 1 << ": ";
        solve();
        cout << endl;
    }
}