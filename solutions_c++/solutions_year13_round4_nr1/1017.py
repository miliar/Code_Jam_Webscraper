#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:128000000")
#define _USE_MATH_DEFINES
#include<iostream>
#include<vector>
#include<string>
#include<stack>
#include<algorithm>
#include<cmath>
#include<set>
#include<queue>
#include<sstream>
#include<utility>
#include<map>
#include<ctime>
#include<cstdio>

 
using namespace std; 
 
typedef long long ll; 
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
const long double PI = 3.14159265358979323846;  
const long double gammama = 0.57721566490153286060;
//const long double eps = 1e-5;
//const int INF = 50000;
//const int N = 1000 * 1000 * 1000 + 10;

ll mod = 1000002013;

ll solve() {
    int n, m;
    cin >> n >> m;
    vector<pair<pii, int> > e(m);
    map<int, int> out, in;
    set<int> v;
    for (int i = 0; i < m; ++i) {
        cin >> e[i].first.first >> e[i].first.second >> e[i].second;
        v.insert(e[i].first.first);
        v.insert(e[i].first.second);
        if (out.find(e[i].first.first) == out.end())
            out[e[i].first.first] = 0;
        out[e[i].first.first] += e[i].second;
        if (in.find(e[i].first.second) == in.end())
            in[e[i].first.second] = 0;
        in[e[i].first.second] += e[i].second;
    }
    ll cur = 0;
    vector<pll> g;
    for (set<int>::iterator it = v.begin(); it != v.end(); ++it) {
        int x = *it;
        g.push_back(make_pair(x, cur - in[x] + out[x]));
        cur += -in[x] + out[x];
    }
    ll res = 0;
    vector<pll> a;
    for (int i = 0; i + 1 < g.size(); ++i) {
        for (int j = 0; j < a.size(); ++j) {
            ll x = a[j].second;
            ll y = min(x, g[i].second);
            res = (res + (y * ((g[i + 1].first - g[i].first) * (g[i].first - a[j].first)) % mod) % mod) % mod;
            g[i].second -= y;
            a[j].second = y;
        }
        a.push_back(g[i]);
    }
    for (int i = 0; i < m; ++i) {
        int j = 0;
        ll p = 0;
        while(g[j].first < e[i].first.first)
            ++j;
        /*if (g[j + 1].first == e[i].first.second)
            continue;*/
        for (;g[j].first < e[i].first.second; ++j) {
            p = (p + (g[j].first - e[i].first.first) * (g[j + 1].first - g[j].first)) % mod;
        }
        p = (mod - ((p * e[i].second) % mod)) % mod;
        res += p;
    }
    return (res % mod);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt;
	//scanf("%d\n", &tt);
	cin >> tt;
	for (int i = 0; i < tt; ++i) {
		cout << "Case #" << i + 1 << ": " << solve() << endl;
		std::cerr << i << endl;
	}
	return 0;
}