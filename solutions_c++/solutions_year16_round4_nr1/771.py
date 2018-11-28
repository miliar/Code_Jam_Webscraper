#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <fstream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <ctime>
#include <stack>
#include <map>
#include <set>
#if __cplusplus > 199711L
#include <unordered_set>
#include <unordered_map>
#include <tuple>
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
//	tree<key, mapped = null_type, cmp = less<key>, rb_tree_tag, tree_order_statistics_node_update> name;
//	order_of_key
//	find_by_order
#endif

using namespace std;

#define pb push_back
#define ppb pop_back
#define mp make_pair
#define fs first
#define sc second
#define abs(a) ((a) < 0 ? -(a) : (a))
#define sqr(a) ((a) * (a))

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;

const double eps = 1e-9;
const int mod = (int)1e+9 + 7;
const double pi = acos(-1.);
const int maxn = 100100;

int dpr[20][3], dpp[20][3], dps[20][3];
string r[20], p[20], s[20];

void update(string &s) {
	int l = s.length();
	int c = 1;
	while(c < l) {
		for(int i = 0; i < l; i += c * 2) {
			bool ok = 1;
			for(int j = 0; j < c; j++) {
				if(s[i + j] < s[i + c + j]) {
					break;
				}
				if(s[i + j] > s[i + c + j]) {
					ok = 0;
					break;
				}
			}
			if(!ok)
			for(int j = 0; j < c; j++) {
				swap(s[i + j], s[i + c + j]);
			}
		}
		c *= 2;
	}
}

int main() {

	#ifdef SOL
	{
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	}
	#else
	{
		srand(time(0));
		const string file = "";
		if(!file.empty()) {
			freopen((file + ".in").c_str(), "r", stdin);
			freopen((file + ".out").c_str(), "w", stdout);
		}
	}
	#endif

	//0 - r, 1 - p, 2 - s
	r[0] = "R";
	dpr[0][0] = 1;
	for(int i = 1; i < 13; i++) {
		dpr[i][0] = dpr[i - 1][0] + dpr[i - 1][1];
		dpr[i][1] = dpr[i - 1][1] + dpr[i - 1][2];
		dpr[i][2] = dpr[i - 1][2] + dpr[i - 1][0];
		for(int j = 0; j < (int)r[i - 1].length(); j++) {
			if((j & 1) == 0 && j + 1 != (int)r[i - 1].length()) {
				if(r[i - 1][j] == 'R' && r[i - 1][j + 1] == 'S') {
					r[i].pb('P');
					r[i].pb('S');
					r[i].pb('R');
					r[i].pb('S');
					j++;
					continue;
				}
			}
			if(r[i - 1][j] == 'R') {
				r[i].pb('R');
				r[i].pb('S');
			}
			if(r[i - 1][j] == 'P') {
				r[i].pb('P');
				r[i].pb('R');
			}
			if(r[i - 1][j] == 'S') {
				r[i].pb('P');
				r[i].pb('S');
			}
		}
	}
	p[0] = "P";
	dpp[0][1] = 1;
	for(int i = 1; i < 13; i++) {
		dpp[i][0] = dpp[i - 1][0] + dpp[i - 1][1];
		dpp[i][1] = dpp[i - 1][1] + dpp[i - 1][2];
		dpp[i][2] = dpp[i - 1][2] + dpp[i - 1][0];
		for(int j = 0; j < (int)p[i - 1].length(); j++) {
			if((j & 1) == 0 && j + 1 != (int)p[i - 1].length()) {
				if(p[i - 1][j] == 'R' && p[i - 1][j + 1] == 'S') {
					p[i].pb('P');
					p[i].pb('S');
					p[i].pb('R');
					p[i].pb('S');
					j++;
					continue;
				}
			}
			if(p[i - 1][j] == 'R') {
				p[i].pb('R');
				p[i].pb('S');
			}
			if(p[i - 1][j] == 'P') {
				p[i].pb('P');
				p[i].pb('R');
			}
			if(p[i - 1][j] == 'S') {
				p[i].pb('P');
				p[i].pb('S');
			}
		}
	}
	s[0] = "S";
	dps[0][2] = 1;
	for(int i = 1; i < 13; i++) {
		dps[i][0] = dps[i - 1][0] + dps[i - 1][1];
		dps[i][1] = dps[i - 1][1] + dps[i - 1][2];
		dps[i][2] = dps[i - 1][2] + dps[i - 1][0];
		for(int j = 0; j < (int)s[i - 1].length(); j++) {
			if((j & 1) == 0 && j + 1 != (int)s[i - 1].length()) {
				if(s[i - 1][j] == 'R' && s[i - 1][j + 1] == 'S') {
					s[i].pb('P');
					s[i].pb('S');
					s[i].pb('R');
					s[i].pb('S');
					j++;
					continue;
				}
			}
			if(s[i - 1][j] == 'R') {
				s[i].pb('R');
				s[i].pb('S');
			}
			if(s[i - 1][j] == 'P') {
				s[i].pb('P');
				s[i].pb('R');
			}
			if(s[i - 1][j] == 'S') {
				s[i].pb('P');
				s[i].pb('S');
			}
		}
	}

	int t;
	scanf("%d", &t);
	for(int q = 1; t--; q++) {
		printf("Case #%d: ", q);
		int n, R, P, S;
		scanf("%d%d%d%d", &n, &R, &P, &S);
		if(dpr[n][0] == R && dpr[n][1] == P && dpr[n][2] == S) {
			update(r[n]);
			printf("%s\n", r[n].c_str());
		} else
		if(dpp[n][0] == R && dpp[n][1] == P && dpp[n][2] == S) {
			update(p[n]);
			printf("%s\n", p[n].c_str());
		} else
		if(dps[n][0] == R && dps[n][1] == P && dps[n][2] == S) {
			update(s[n]);
			printf("%s\n", s[n].c_str());
		} else {
			printf("IMPOSSIBLE\n");
		}
	}

	#ifdef SOL
	{
		fflush(stdout);
		fprintf(stderr, "%.3lf ms\n", 1000. * clock() / CLOCKS_PER_SEC);
		fflush(stderr);
	}
	#endif
	return(0);
}

// by Andrey Kim
