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

pll solve() {
	int n, m;
	cin >> m >> n;
	vector<string> a(m);
	for (int i = 0; i < m; ++i)
		cin >> a[i];
	int up = 1;
	for (int i = 0; i < m; ++i)
		up *= n;
	vector<vector<int> > b(m, vector<int> (m, 0));
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < m; ++j) {
			int k = 0;
			while((k < a[i].size()) && (k < a[j].size())) {
				if (a[i][k] == a[j][k])
					++k;
				else
					break;
			}
			b[i][j] = k;
		}
	}
	pll res(0, 0);
	for (int i = 0; i < up; ++i) {
		vector<vector<int> > c(n);
		int x = i;
		for (int j = 0; j < m; ++j) {
			c[x % n].push_back(j);
			x /= n;
		}
		ll cur = n;
		int f = 0;
		for (int i = 0; i < n; ++i) {
			if (c[i].empty()) {
				f = 1;
				break;
			}
			for (int j = 0; j < c[i].size(); ++j) {
				cur += a[c[i][j]].size();
				int sub = 0;
				for (int k = 0; k < j; ++k)
					sub = max(sub, b[c[i][k]][c[i][j]]);
				cur -= sub;
			}
		}
		if (f)
			continue;
		if (cur > res.first) {
			res = pll(cur, 1);
		}
		else {
			if (cur == res.first)
				++res.second;
		}
	}
	return res;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt;
	//scanf("%d\n", &tt);
	cin >> tt;
	for (int i = 0; i < tt; ++i) {
		pll res = solve();
		cout << "Case #" << i + 1 << ": " << res.first << " " << res.second << endl;
		std::cerr << i << endl;
	}
	return 0;
}