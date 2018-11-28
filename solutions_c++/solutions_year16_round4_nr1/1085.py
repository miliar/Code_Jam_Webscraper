#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>


using namespace std;

string sortres(string &k, int l, int r) {
	if (l == r) {
		string res = "";
		res += k[l];
		return res;
	}
	int num = r - l + 1;
	string ls = sortres(k, l, l + num / 2 - 1);
	string rs = sortres(k, l + num / 2, r);
	if (ls < rs)
		return ls + rs;
	else
		return rs + ls;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int tc;
	cin >> tc;
	for (int ti = 1; ti <= tc; ti++) {
		int n, r, p, s;
		cin >> n >> r >> p >> s;
		n = r + p + s;
		int apr[20] = { 0, }, aps[20] = { 0, }, ars[20] = { 0, };
		int cnt = 0;
		while (n > 1) {
			int pr, rs, ps;
			pr = (p + r - s) / 2;
			apr[cnt] = pr;
			rs = (r + s - p) / 2;
			ars[cnt] = rs;
			ps = (p + s - r) / 2;
			aps[cnt] = ps;
			cnt++;
			if (pr < 0 || rs < 0 || ps < 0)
				break;
			p = pr;
			r = rs;
			s = ps;
			n = p + r + s;
		}

		if (n > 1) {
			cout << "Case #" << ti << ": IMPOSSIBLE" << endl;
			continue;
		}
		string res;
		if (p)
			res = "P";
		if (r)
			res = "R";
		if (s)
			res = "S";
		
		for (int i = cnt - 1; i >= 0; i--) {
			string nres = "";
			for (int j = 0; j < res.size(); j++) {
				if (res[j] == 'P') {
					nres += "PR";
				}
				else if (res[j] == 'R') {
					nres += "RS";
				}
				else {
					nres += "PS";
				}
			}
			res = nres;
		}
		cout << "Case #" << ti << ": " << sortres(res, 0, res.size() - 1) << endl;
	}
}