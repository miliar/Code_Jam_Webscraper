#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#include <unordered_map>
#include <unordered_set>

#define oo 1e9
#define pi 3.1415926536
#define all(x) x.begin(),x.end()
#define sorta(x) sort(all(x))
#define sortam(x,comp) sort(all(x),comp)
#define sortd(x) sort(x.rbegin(),x.rend())
#define sf(x) scanf("%d", &x);
#define sf2(x, y) scanf("%d %d", &x, &y);
#define sf3(x, y, z) scanf("%d %d %d", &x, &y, &z);
#define sfll(x) scanf("%I64d", &x);
#define sfll2(x, y) scanf("%I64d %I64d", &x, &y);
#define sfll3(x, y, z) scanf("%I64d %I64d %I64d", &x, &y, &z);
#define sfd(x) scanf("%f", &x);

typedef long long ll;
using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	sf(t);
	for(int tc = 1; tc <= t; tc++) {
		string ts, s;
		cin >> s;
		ts += s[0];
		for(int i = 1; i < s.size(); i++) {
			if(s[i] != ts.back()) ts += s[i];
		}

		int res = ts.size() - (ts.back() == '+');
		printf("Case #%d: %d\n", tc, res);
	}
	return 0;
}
