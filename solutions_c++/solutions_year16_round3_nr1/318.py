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

void clear(int i) {

}

int solution(int nTest) {
	int n;
	scanf("%d", &n);
	vector<pair<int, char> > v;
	For (i, 0, n) {
		int t;
		scanf("%d", &t);
		v.pb(mp(t, i + 'A'));
	}
	cerr << nTest << endl;
	sort(all(v));
	reverse(all(v));
	vector<string> res;
	while (v[0].first > v[1].first) {
		res.pb(string(1, v[0].second));
		v[0].first--;
	}
	For (i, 0, sz(res)) cerr << res[i] << " "; cerr << endl;
	For (i, 2, sz(v)) {
		For (j, 0, v[i].first) {
			res.pb(string(1, v[i].second));
		}
	}
	For (i, 0, sz(res)) cerr << res[i] << " "; cerr << endl;
	For (i, 0, v[0].first) {
		string s(2, v[1].second);
		s[0] = v[0].second;
		res.pb(s);
	}
	For (i, 0, sz(res)) cerr << res[i] << " "; cerr << endl;
	printf("%s", res[0].c_str());
	For (i, 1, sz(res)) {
		printf(" %s", res[i].c_str());
	}
	printf("\n");


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
	
