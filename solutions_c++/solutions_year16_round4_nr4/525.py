// Smile please :)

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cctype>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <string>
#include <iomanip>
#include <numeric>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <list>
#include <bitset>
#include <climits>
#include <unordered_map>
#include <unordered_set>
using namespace std;

//#undef KVARK_DEBUG

#ifdef KVARK_DEBUG
	#include "../h/debug.h"
#else
#define dbg(...) (void(1));
#define dbg2(...) (void(1));
#define dbg3(...) (void(1));
#define dbg4(...) (void(1));
#define dbg5(...) (void(1));
#define dbgp(...) (void(1));
#define dbg_arr(...) (void(1));
#define dbg_vec(...) (void(1));
#endif

typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
typedef pair<double, int> pdi;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
typedef vector<vector<int> > vvi;
typedef vector<vector<pii> > vvpii;
typedef vector<vector<long long> > vvl;
typedef vector<long long> vl;
typedef long long int llint;

#define ALL(v) (v.begin()), (v.end())
#define SZ(v) ((int)((v).size()))
#define endl "\n"

void task();

 #undef KVARK

int main(){
#ifdef KVARK
	freopen("input.txt", "r", stdin);
#else
	freopen("src/gcj_input.txt", "r", stdin);
	freopen("src/gcj_output.txt", "w", stdout);
	srand(time(0));
#endif
//	ios_base::sync_with_stdio(0);

	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ": ";
		task();
		cout << endl;
	}

#ifdef KVARK_DEBUG
//	my_debug::printProcessInfo();
#endif
	return 0;
}
const int INF = 0x3f3f3f3f;
const int N = 3e5+10;
const int M = 3e5+10;

int n;
string s[10];
string cur[10];
vi v1;
int used[10];

bool check(int i) {
	if (i == n)
		return true;
	int ok = 0;
	for (int j = 0; j < n; ++j) if (cur[v1[i]][j] == '1' && !used[j]) {
		ok = 1;
		used[j] = 1;
		int res = check(i + 1);
		used[j] = 0;
		if (!res)
			return false;
	}
	return ok;
}

void task(){
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> s[i];
		cur[i] = s[i];
	}
	int ans = n*n;
	for (int mask = 0; mask < (1 << (n*n)); ++mask) {
		int ok = 1;
		int need = 0;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j) {
				if ((mask & (1 << (i * n + j))) > 0) {
					cur[i][j] = '1';
					need += s[i][j] == '0';
				} else {
					if (s[i][j] == '1') {
						ok = 0;
						break;
					}
					cur[i][j] = '0';
				}
			}
		if (!ok)
			continue;
		v1.assign(n, 0);
		for (int i = 0; i < n; ++i)
			v1[i] = i;
		int YES = 1;
		do {
			YES &= check(0);
		} while (YES && next_permutation(ALL(v1)));
		if (YES)
			ans = min(ans, need);
	}
	cout << ans;
}
