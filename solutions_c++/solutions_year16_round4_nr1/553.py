//author: whd

#pragma comment(linker, "/STACK:1024000000,1024000000")
#include <iostream>
#include <string>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <queue>
#include <set>
#include <map>

#define mp make_pair
#define pb push_back
#define x first
#define y second

using namespace std;
typedef long long big;

typedef pair<int, int> pii;

const int N = 222;
int n;
int P, R, S;
bool check(int r, int p, int s) {
//	cerr << r << " " << p << " " << s << endl;
	if (r + p + s == 1)
		return true;
	if (r + p < s || r + s < p || p + s < r)
		return false;
	int x = (r + p - s) / 2;
	return check(r - x, x, p - x);
}
void mt(string &str, int l, int r) {
	if (r <= l + 2)
		return;
	int mid = l + r >> 1;
	mt(str, l, mid);
	mt(str, mid, r);
	int nn = (r - l) / 2;
//	string res = str;
	if (str.substr(l, nn) > str.substr(l + nn, nn)) {
		for (int i = l; i < l + nn; i++) {
			swap(str[i], str[i + nn]);
		}
	}
//	str = res;
}
string get(int r, int p, int s) {
	if (r + p + s == 1) {
		if (r)
			return "R";
		if (p)
			return "P";
		if (s)
			return "S";
	}
	int x = (r + p - s) / 2;
	string tmp = get(r - x, x, p - x);
	string res = "";
	for (int i = 0; i < tmp.size(); i++) {
		if (tmp[i] == 'R')
			res += "RS";
		if (tmp[i] == 'P')
			res += "PR";
		if (tmp[i] == 'S')
			res += "PS";
	}
	mt(res, 0, res.size());
//	int nn = res.size() / 2;
//	if (res.substr(0, nn) > res.substr(nn, nn)) {
//		for (int i = 0; i < nn; i++)
//			swap(res[i], res[i + nn]);
//	}
	return res;
}
int main() {
	int cas, cass;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int i, j, k;
	scanf("%d", &cas);
	for (cass = 1; cass <= cas; cass++) {
		scanf("%d%d%d%d", &n, &R, &P, &S);
		printf("Case #%d: ", cass);
		string ans;
		if (!check(R, P, S)) {
			puts("IMPOSSIBLE");
		} else {
			cout << get(R, P, S) << endl;
		}
	}

}
