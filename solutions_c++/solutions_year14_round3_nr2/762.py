#include <cstdio>
#include <cstring>
#include <iostream>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;

#define debug 0

#define pb push_back
#define mp make_pair

#define For(i, a, b) for(int i = a; i < b; i++)

#define sz(a) ((int)a.size())

typedef long long lint;


const int inf = 0x7fffffff;
const int Size = 1000 * 1000 * 10;
char buffer[Size];

map<char, int> full;
map<char, char> pref;
map<char, char> suff;

set<char> color;

void clear() {
	color.clear();
	full.clear();
	pref.clear();
	suff.clear();
}

bool hasCycle;
void dfs(char c) {
	color.insert(c);
	if(pref.count(c)) {
		char v = pref[c];
		if(color.count(v)) {
			if(suff[v] != c) {
				cerr << "hasClycle" << "(" << c << v << ")";
				hasCycle = true;
			}
		} else {
			dfs(v);
		}
	}
	if(suff.count(c)) {
		char v = suff[c];
		if(color.count(v)) {
			if(pref[v] != c) {
				cerr << "hasClycle" << "(" << c << v << ")";
				hasCycle = true;
			}
		} else {
			dfs(v);
		}
	}

}

const lint md = 1000000007;

lint fact[200];

int solution(int nTest) {
	int n;
	scanf("%d", &n);
	vector<string> v;
	fact[0] = 1;
	For(i, 1, 200) {
		fact[i] = (i * fact[i-1]) % md;
	}
	For(i, 0, n) {
		scanf("%s", buffer);
		v.pb(buffer);
	}
	vector<string> vv;
	For(i, 0, n) {
		string res;
		string &s = v[i];
		char cur = s[0];
		For(j, 0, sz(s)) {
			if(s[j] != cur) {
				res.pb(cur);
			}
			cur = s[j];
		}
		res.pb(cur);
		if(sz(res) > 26) {
			cerr << "sz(res) > 26" << endl;
			puts("0");
			return 0;
		}
		vv.pb(res);
	}
	v = vv;
	For(i, 0, n) { cerr << v[i] << " ";} cerr << endl;
	For(i, 0, n) {
		string &s = v[i];
		For(j, 1, sz(s) - 1) {
			For(k, 0, sz(s)) {
				if(k == j) {
					continue;
				}
				if(s[k] == s[j]) {
					cerr << "middle " << s << endl;
					puts("0");
					return 0;
				}
			}
			For(k, 0, n) {
				if(k == i) {
					continue;
				}
				string &b = v[k];
				For(m, 0, sz(b)) {
					if(b[m] == s[j]) {
						cerr << "middle " << s << " " << b << endl;
						puts("0");
						return 0;
					}
				}
			}
		}
	}
	For(i, 0, n) {
		string &s = v[i];
		if(s.size() == 1) {
			char c = s[0];
			if(full.count(c) == 0) {
				full[c] = 0;
			}
			full[c]++;
		} else {
			char b = s[0];
			char e = s[sz(s) - 1];
			if(pref.count(b)) {
				cerr << "pref " << b << " " << s << endl;
				puts("0");
				return 0;
			}
			if(suff.count(e)) {
				cerr << "suff " << e << " " << s << endl;
				puts("0");
				return 0;
			}
			if(b == e) {
				cerr << "suff=pref " << e << " " << s << endl;
				puts("0");
				return 0;
			}

			pref[b] = e;
			suff[e] = b;
		}
	}
	hasCycle = false;
	for(map<char, char>::iterator it = pref.begin();
			it != pref.end(); it++) {
		if(color.count(it->first) == false) {
			dfs(it->first);
		}
		if(hasCycle) {
			cerr << "cycle " << it->first << " " << endl;
			puts("0");
			return 0;
		}
		char u = it->first;
		char v = it->second;
		if(suff.count(u) && suff[u] == v) {
			cerr << "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!doubleedge " << u << " " << v << endl;
			puts("0");
			return 0;
		}
	}

	int cnt = 0;
	for(map<char, char>::iterator it = pref.begin();
			it != pref.end(); it++) {

		char b = it->first;
		char e = it->second;
		if(suff[b] == 0) {
			cnt++;
		}
	}
	lint res = 1;
	cerr << cnt << "!";
	for(map<char, int>::iterator it = full.begin();
			it != full.end(); it++) {
		char b = it->first;
		int k = it->second;
		if(suff.count(b) == 0 && pref.count(b) == 0) {
			cnt++;
		}
		res *= fact[k];
		res %= md;
	}
	cerr << res << "!";
	res *= fact[cnt];
	res %= md;

	cerr << cnt << "res" <<  res << endl;
	cout << res << endl;


	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	For(i, 0, n) {
		printf("Case #%d: ", i + 1);
		solution(i);
		clear();
	}


	return 0;
}


