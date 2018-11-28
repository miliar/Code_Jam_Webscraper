#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
#include <cmath>
#include <cstdlib>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>

using namespace std;

int T, ti;
string s, ans;

string work(string ws) {
	int l = ws.length();
	if (l == 0) return "";
	int i, t;
	char c = 'A';
	for (i = 0; i < l; i++)
		if (ws[i] >= c) {
			c = ws[i];
			t = i;
		}
	if (t + 1 != l)
		return ws[t] + work(ws.substr(0, t)) + ws.substr(t + 1, l - t - 1);
	else return ws[t] + work(ws.substr(0, t));
}

int main() {
	//freopen("./a.in", "r", stdin);
	//freopen("./a.out", "w", stdout);
	scanf("%d", &T);
	for (ti = 1; ti <= T; ++ti) {
		//coding
		cin >> s;
		ans = work(s);

		printf("Case #%d: ", ti);
		cout << ans << endl;
	}
	return 0;
}
