#include <iostream>
#include <sstream>
#include <algorithm>
#include <unordered_map>
#include <vector>
#include <cstdio>
#include <cmath>
#include <map>
#include <set>
#include <unordered_set>


using namespace std;


int t;
string b[10001];



int main() {
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	cin >> t;
	map<pair<string, string>, string> m;
	m[make_pair("1", "1")] = "1";
	m[make_pair("1", "i")] = "i";
	m[make_pair("1", "j")] = "j";
	m[make_pair("1", "k")] = "k";
	m[make_pair("i", "1")] = "i";
	m[make_pair("j", "1")] = "j";
	m[make_pair("k", "1")] = "k";
	m[make_pair("i", "j")] = "k";
	m[make_pair("j", "i")] = "-k";
	m[make_pair("i", "k")] = "-j";
	m[make_pair("k", "i")] = "j";
	m[make_pair("j", "k")] = "i";
	m[make_pair("k", "j")] = "-i";

	m[make_pair("i", "i")] = "-1";
	m[make_pair("j", "j")] = "-1";
	m[make_pair("k", "k")] = "-1";

	m[make_pair("-i", "-i")] = "-1";
	m[make_pair("-j", "-j")] = "-1";
	m[make_pair("-k", "-k")] = "-1";

	m[make_pair("-i", "i")] = "1";
	m[make_pair("-j", "j")] = "1";
	m[make_pair("-k", "k")] = "1";

	m[make_pair("i", "-i")] = "1";
	m[make_pair("j", "-j")] = "1";
	m[make_pair("k", "-k")] = "1";

	m[make_pair("-1", "-1")] = "1";
	m[make_pair("-1", "-i")] = "i";
	m[make_pair("-1", "-j")] = "j";
	m[make_pair("-1", "-k")] = "k";
	m[make_pair("-i", "-1")] = "i";
	m[make_pair("-j", "-1")] = "j";
	m[make_pair("-k", "-1")] = "k";
	m[make_pair("-i", "-j")] = "k";
	m[make_pair("-j", "-i")] = "-k";
	m[make_pair("-i", "-k")] = "-j";
	m[make_pair("-k", "-i")] = "j";
	m[make_pair("-j", "-k")] = "i";
	m[make_pair("-k", "-j")] = "-i";

	m[make_pair("-1", "1")] = "-1";
	m[make_pair("-1", "i")] = "-i";
	m[make_pair("-1", "j")] = "-j";
	m[make_pair("-1", "k")] = "-k";
	m[make_pair("-i", "1")] = "-i";
	m[make_pair("-j", "1")] = "-j";
	m[make_pair("-k", "1")] = "-k";
	m[make_pair("-i", "j")] = "-k";
	m[make_pair("-j", "i")] = "k";
	m[make_pair("-i", "k")] = "j";
	m[make_pair("-k", "i")] = "-j";
	m[make_pair("-j", "k")] = "-i";
	m[make_pair("-k", "j")] = "i";

	m[make_pair("1", "-1")] = "-1";
	m[make_pair("1", "-i")] = "-i";
	m[make_pair("1", "-j")] = "-j";
	m[make_pair("1", "-k")] = "-k";
	m[make_pair("i", "-1")] = "-i";
	m[make_pair("j", "-1")] = "-j";
	m[make_pair("k", "-1")] = "-k";
	m[make_pair("i", "-j")] = "-k";
	m[make_pair("j", "-i")] = "k";
	m[make_pair("i", "-k")] = "j";
	m[make_pair("k", "-i")] = "-j";
	m[make_pair("j", "-k")] = "-i";
	m[make_pair("k", "-j")] = "i";
	for (int k = 0; k < t; k++) {
		int l, x;
		scanf("%d %d", &l, &x);
		string s1;
		cin >> s1;
		string s;
		for (int j = 0; j < x; j++) {
			s += s1;
		}
		l *= x;
		bool bbb = false;
		for (int j = l - 1; j >= 2; j--) {
			string ss;
			ss += s[j];
			b[j] = (j < l - 1 ? m[make_pair(ss, b[j + 1])]: ss);
			if (b[j] == "k") {
				bbb = true;
			}
		}
		if (!bbb) {
			printf("Case #%d: NO\n", k + 1);
			continue;
		}
		string p;
		bool bb = true;
		for (int j = 0; j < l - 2 && bb; j++) {
			string ss1;
			ss1 += s[j];
			if (j == 0) {
				p = ss1;
			} else {
				p = m[make_pair(p, ss1)];
			}
			if (p != "i") {
				continue;
			}
			//cout << s[j] << endl;
			string p1;
			for (int g = j + 1; g < l - 1; g++) {
				string ss;
				ss += s[g];
				if (g == j + 1) {
					p1 = ss;
				} else {
					p1 = m[make_pair(p1, string(ss))];
				}
				//cout << p1 << ' ' << ss << endl;
				if (p1 == "j") {
					//cout << "opa" << endl;
					if (b[g + 1] == "k") {
						bb = false;
						printf("Case #%d: YES\n", k + 1);
						break;
					}
				}
			}
		}
		if (bb) {
			printf("Case #%d: NO\n", k + 1);
		}
	}
    return 0;
}
