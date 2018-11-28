#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <queue>
#include <deque>
#include <set>
#include <utility>
#include <vector>
#include <map>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define all(v) v.begin(), v.end()
#define mp make_pair

map< pair<string, string>, string > m;

void init()
{
	m[mp("1", "1")] = "1";
	m[mp("1", "i")] = "i";
	m[mp("1", "j")] = "j";
	m[mp("1", "k")] = "k";

	m[mp("-1", "1")] = "-1";
	m[mp("-1", "i")] = "-i";
	m[mp("-1", "j")] = "-j";
	m[mp("-1", "k")] = "-k";

	m[mp("i", "1")] = "i";
	m[mp("i", "i")] = "-1";
	m[mp("i", "j")] = "k";
	m[mp("i", "k")] = "-j";

	m[mp("-i", "1")] = "-i";
	m[mp("-i", "i")] = "1";
	m[mp("-i", "j")] = "-k";
	m[mp("-i", "k")] = "j";

	m[mp("j", "1")] = "j";
	m[mp("j", "i")] = "-k";
	m[mp("j", "j")] = "-1";
	m[mp("j", "k")] = "i";

	m[mp("-j", "1")] = "-j";
	m[mp("-j", "i")] = "k";
	m[mp("-j", "j")] = "1";
	m[mp("-j", "k")] = "-i";

	m[mp("k", "1")] = "k";
	m[mp("k", "i")] = "j";
	m[mp("k", "j")] = "-i";
	m[mp("k", "k")] = "-1";

	m[mp("-k", "1")] = "-k";
	m[mp("-k", "i")] = "-j";
	m[mp("-k", "j")] = "i";
	m[mp("-k", "k")] = "1";
}

string mul(string a, string b)
{
	//cout << "mul " << a << " " << b << ", res = " << m[mp(a, b)] << endl;
	return m[mp(a, b)];
}

void main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int tt, n, x;
	string s;
	cin >> tt;
	init();
	forn(tc, tt) {
		cin >> n >> x;
		cin >> s;
		string c = "1";
		/*
		forn(f, x) {
			forn(i, n)
				c = mul(c, s.substr(i, 1));
		}
		string res = (c == "-1" ? "YES" : "NO");
		printf("Case #%d: %s", tc+1, res.c_str());
		*/
		c = "1";
		int passed = 0;
		forn(f, x)
			forn(i, n) {
				if (passed == 0 && c == "i")
					passed = 1, c = "1";
				if (passed == 1 && c == "j")
					passed = 2, c = "1";
				c = mul(c, s.substr(i, 1));
			}
		string res2 = (passed == 2 && c == "k") ? "YES" : "NO";
		printf("Case #%d: %s\n", tc+1, res2.c_str());
		//printf (" %s, %s\n", res2.c_str(), res != res2 ? "FAIL" : "");
	}

	/*int tt, n;
	cin >> tt;
	string s;
	forn(tc, tt) {
		cin >> n >> s;
		++n;
		int res = 0, c = 0;
		forn(i, n) {
			if (s[i] > '0' && c < i) {
				res += i - c;
				c = i;
			}
			c += s[i] - '0';
		}
		printf("Case #%d: %d\n", tc+1, res);
	}
	*/
}