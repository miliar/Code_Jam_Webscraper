#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>
#include <iomanip>
#include <cassert>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for(__typeof__((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define mp make_pair
#define pb push_back
const ull MOD = 1000000007l;
struct W {
	char start, end;
	int next = -1, last = -1;
	set<char> middle;
	bool used = false;
};
ull fak(int a) {
	if (a <= 1) return 1;
	return (a * fak(a-1)) % MOD;
}
int main() {
	int tc;
	cin >> tc;
	FOR(tt, 0, tc) {
		int n;
		cin >> n;
		vector<W> v(n);
		vs p(n);
		FOR(i, 0, n) {
			cin >> p[i];
		}
		bool fail = false;
		vi dups(26);
		vector<W> mod;
				int groups = 0;
		ull ret = 1;
		vector<bool> found(26);
		set<char> globalMid;
				vector<bool> startL(26), endL(26);
		FOR(i, 0, n) {
			string s = p[i];
			v[i].start = s[0];
			v[i].end = s[s.size() - 1];
			char last = 0;
			bool toEnd = false;
			FOR(k, 0, s.size()) {
				if (toEnd && s[k] != v[i].end) {
					goto error;
				}
				if (globalMid.find(s[k]) != globalMid.end() && last != s[k]) goto error;
				if (last != s[k]) {
					if (v[i].middle.find(s[k]) != v[i].middle.end()) {
						goto error;
					}
					if (s[k] != v[i].start && s[k] != v[i].end) {
						if (found[s[k]-'a']) goto error; // middle already found
						v[i].middle.insert(s[k]);
						if (found[s[k]-'a'] && last != s[k]) goto error;
						globalMid.insert(s[k]);
					}
					last = s[k];
					if (last == v[i].end) {
						toEnd = true;
					}
				}
				found[s[k]-'a'] = true;
			}
			if (fail) goto error;
			if (v[i].start == v[i].end) {
				dups[v[i].start - 'a']++;
			} else {
				mod.pb(v[i]);
			}
		}
		FOR(i, 0, mod.size()) {
			FOR(j, 0, mod.size()) {
				if (i == j) continue;
				if (mod[i].end == mod[j].start) {
					if (mod[i].next != -1) goto error;
					if (mod[j].last != -1) goto error;
					mod[i].next = j;
					mod[j].last = i;
				}
			}
		}

		FOR(i, 0, mod.size()) {
			if (mod[i].used) continue;
			int k = i;
			mod[k].used = true;
			while(mod[k].next != -1) {
				k = mod[k].next;
				if (mod[k].used) goto error;
				mod[k].used = true;
				ret = (ret * fak(dups[mod[k].start-'a'])) % MOD;
				dups[mod[k].start-'a'] = 0;
			}
			ret = (ret * fak(dups[mod[k].end-'a'])) % MOD;
			dups[mod[k].end-'a'] = 0;
			k = i;
			while(mod[k].last != -1) {
				k = mod[k].last;
				if (mod[k].used) goto error;
				mod[k].used = true;
				ret = (ret * fak(dups[mod[k].end-'a'])) % MOD;
				dups[mod[k].end-'a'] = 0;
			}
			ret = (ret * fak(dups[mod[k].start-'a'])) % MOD;
			dups[mod[k].start-'a'] = 0;
			groups++;
		}

		FOR(i, 0, mod.size()) {
			if (startL[mod[i].start-'a']) goto error;
			if (endL[mod[i].end-'a']) goto error;
			startL[mod[i].start-'a'] = true;
			endL[mod[i].end-'a'] = true;
		}
		FOR(i, 0, 26) if (dups[i] > 0) {
			groups++;
			ret = (ret * fak(dups[i])) % MOD;
		}
		ret = (ret * fak(groups)) % MOD;
		cout << "Case #" << tt+1 << ": " << ret << endl;
		continue;
error:
		cout << "Case #" << tt+1 << ": 0" << endl;
	}

	return 0;
}
