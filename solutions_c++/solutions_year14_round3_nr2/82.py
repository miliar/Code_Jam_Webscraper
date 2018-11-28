#include <iostream>
#include <map>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>

using namespace std;


bool check(string& s) {
	char buf[110];
	
	memcpy(buf, s.c_str(), s.length());
	int n1 = unique(buf, buf + s.length()) - buf;
	s = string(buf, n1);
	sort(buf, buf + s.length());
	int n2 = unique(buf, buf + s.length()) - buf;
	if (n1 != n2)
		return false;

	return true;
}

string a[110];
const long long MOD = 1000000007;
long long jc[110];


int work() {
	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> a[i];
		if (!check(a[i]))
			return 0;
	}
	long long ans = 1;
	for (char c = 'a'; c <= 'z'; c++) {
		int cnt = 0;
		int nht = 0;

		for (int i = 0; i < n; i++)
			if (a[i].find(c) != a[i].npos) {
				cnt++;
				if (a[i][0] == c && a[i][a[i].length() - 1] == c)
					nht++;
			}
		if (cnt <= 1)
			continue;
		ans = ans * jc[nht] % MOD;

		string str = "";
		string strm = "";
		string str2 = "";
		for (int i = 0; i < n; i++)
			if (a[i].find(c) != a[i].npos) {
				if (a[i][a[i].length() - 1] == c) {
					if (a[i][0] == c) {
						strm = a[i];
					} else {
						str = a[i] + str;
						if (!check(str))
							return 0;
					}
				} else {
					str2 = str2 + a[i];
					if (!check(str2))
						return 0;
				}

				a[i] = a[--n];
				i--;
			}
		str = str + strm + str2;
		if (!check(str))
			return 0;
		a[n++] = str;
	}
	ans = ans * jc[n] % MOD;
	return ans;
}

int main() {
	//ios::sync_with_stdio(false);
	freopen("G:/1.in", "r", stdin);
	freopen("G:/1.out", "w", stdout);

	jc[0] = 1;
	for (int i = 1; i < 105; i++) {
		jc[i] = jc[i - 1] * i % MOD;
	}
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		cout << work() << endl;
	}
	return 0;
}

