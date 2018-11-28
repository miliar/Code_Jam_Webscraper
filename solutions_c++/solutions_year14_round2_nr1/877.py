#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define debug 1

#define cerr if(debug) cerr

#define For(i, a, b) for(int i = a; i < b; i++)
#define sz(a) ((int)a.size())
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef pair<int, int> pii;
typedef long long lint;

const int inf = 0x7fffffff;
const int Size = 1000 * 1000 + 1;
char buffer[Size];


void init() {

}


vector<string> v;
vector<vector<pair<char, int> > > ar;

void clear(int i) {
	v.clear();
	ar.clear();
}

const char won[] = "Fegla Won";

int solution(int nTest) {
	int n;
	scanf("%d", &n);
	For(i, 0, n) {
		scanf("%s", buffer);
		v.pb(buffer);
	}
	For(i, 0, n) {
		char c = v[i][0];
		int count = 0;
		vector<pair<char, int> > sym;
		For(j, 0, sz(v[i])) {
			if(v[i][j] != c) {
				sym.pb(mp(c, count));
				count = 1;
				c = v[i][j];
			} else {
				count++;
			}
		}
		sym.pb(mp(c, count));
		ar.pb(sym);
	}
	int z = ar[0].size();
	For(i, 0, n) {
		if(ar[i].size() != z) {
			puts(won);
			return 0;
		}
	}
	For(i, 0, n) {
		For(j, 0, z) {
			if(ar[i][j].first != ar[0][j].first) {
				puts(won);
				return 0;
			}
		}
	}
	int res = 0;
	For(j, 0, z) {
		int mn = inf;
		int mx = -inf;
		For(i, 0, n) {
			mn = min(mn, ar[i][j].second);
			mx = max(mx, ar[i][j].second);
		}
		int t = inf;
		for(int k = mn; k <= mx; k++) {
			int cnt = 0;
			For(i, 0, n) {
				cnt += abs(ar[i][j].second - k);
			}
			t = min(t, cnt);
		}
		res += t;
	}
	printf("%d\n", res);

	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 999999;
	scanf("%d", &n);
	init();
	For(i, 0, n) {
		printf("Case #%d: ", i + 1);
		clear(i);
		solution(i);
	}

	return 0;
}
	
