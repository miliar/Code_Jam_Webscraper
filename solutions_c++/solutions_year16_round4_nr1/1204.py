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
#define sf(x) scanf("%d", &x)
#define sf2(x, y) scanf("%d %d", &x, &y)
#define sf3(x, y, z) scanf("%d %d %d", &x, &y, &z)
#define sfll(x) scanf("%I64d", &x)
#define sfll2(x, y) scanf("%I64d %I64d", &x, &y)
#define sfll3(x, y, z) scanf("%I64d %I64d %I64d", &x, &y, &z)
#define sfd(x) scanf("%f", &x)

typedef long long ll;
using namespace std;
int n;
int u[3];
string tmp, com = "RPS";
void go(char c, int lev) {
	if(lev == n) {
		tmp += c;
		u[com.find(c)]++;
		return;
	}

	if(c == 'R') {
		go('R', lev + 1);
		go('S', lev + 1);
	}

	if(c == 'S') {
		go('P', lev + 1);
		go('S', lev + 1);
	}

	if(c == 'P') {
		go('P', lev + 1);
		go('R', lev + 1);
	}
}

void get(string &s, int l, int r) {
	if(l == r)
		return;

	int mid = (l + r) / 2;
	get(s, l, mid);
	get(s, mid + 1, r);
	string t1 = s.substr(l, mid - l + 1), t2 = s.substr(mid + 1, mid - l + 1);
	if(t2 < t1) {
		for(int i = 0; i < t2.size(); i++)
			s[i + l] = t2[i];
		for(int i = 0; i < t1.size(); i++)
			s[i + mid + 1] = t1[i];
	}
}

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	sf(t);
	for(int tc = 1; tc <= t; tc++) {
		int a, b, c;
		sf(n); sf3(a, b, c);

		string res = "IMPOSSIBLE";
		memset(u, 0, sizeof u);
		tmp = "";
		go('R', 0);
		if(u[0] == a && u[1] == b && u[2] == c) {
			get(tmp, 0, tmp.size() - 1);
			if(res == "IMPOSSIBLE")
				res = tmp;
			else res = min(res, tmp);
		}
		memset(u, 0, sizeof u);
		tmp = "";

		go('P', 0);
		if(u[0] == a && u[1] == b && u[2] == c) {
			get(tmp, 0, tmp.size() - 1);
			if(res == "IMPOSSIBLE")
				res = tmp;
			else res = min(res, tmp);
		}
		memset(u, 0, sizeof u);
		tmp = "";

		go('S', 0);
		if(u[0] == a && u[1] == b && u[2] == c) {
			get(tmp, 0, tmp.size() - 1);
			if(res == "IMPOSSIBLE")
				res = tmp;
			else res = min(res, tmp);
		}
		printf("Case #%d: ", tc);
		cout << res << endl;
	}
	return 0;
}
