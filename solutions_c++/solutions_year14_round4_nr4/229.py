#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <complex>
#include <numeric>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stdio.h>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>
#include <assert.h>
#define REP(i,n) for(int i=0;i<n;i++)
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))
#define FILL(x,c) memset(x,c,sizeof(x))

using namespace std;

const double eps = 1e-8;
const double pi = acos(-1);

#define PB push_back
#define MP make_pair

typedef map<int,int> MII;
typedef map<string,int> MSI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<long double> VD;
typedef pair<int,int> PII;
typedef long long int64;
typedef long long ll;
typedef unsigned int UI;
typedef long double LD;
typedef unsigned long long ULL;

const int N = 2000;

const int INF = 0x3F3F3F3F;

string words[N];
int nodes[N];
int m, n;

struct Node {
	int ch[26];
	void reset() { FILL(ch, -1);}
};

Node tree[N];
int last;

void ins(string s) {
	int current = 0;
	REP(i, s.size()) {
		int x = s[i] - 'A';
		if (tree[current].ch[x] == -1) {
			tree[current].ch[x] = last;
			tree[last++].reset();
		}
		current = tree[current].ch[x];
	}
}

int go(int mask) {
	tree[0].reset();
	last = 1;
	REP(i, m) {
		if (mask & (1 << i)) {
			ins(words[i]);
		}
	}

	return last;
}

int dp[10][N], ways[10][N];

const int MOD = 1000000007;

void solve(int nowCase) {
	cin >> m >> n;
	REP(i, m) cin >> words[i];
	REP(i, (1 << m)) nodes[i] = go(i);
	REP(j, n + 1) REP(i, (1 << m)) { dp[j][i] = -1; ways[j][i] = 0;}
	dp[0][0] = 0;
	ways[0][0] = 1;
	REP(i, n) {
		REP(j, (1 << m)) {
			if (dp[i][j] == -1) continue;
			int rest = (1 << m) - 1 - j;
			for (int sub = rest; sub; sub = (sub - 1) & rest) {
				if (dp[i][j] + nodes[sub] > dp[i + 1][j + sub]) {
					dp[i + 1][j + sub] = dp[i][j] + nodes[sub];
					ways[i + 1][j + sub] = ways[i][j] % MOD;
				} else if (dp[i][j] + nodes[sub] == dp[i + 1][j + sub]) {
					ways[i + 1][j + sub] = (ways[i + 1][j + sub] + ways[i][j]) % MOD;
				}
			}
		}
	}

	cout << "Case #" << nowCase << ": " << dp[n][(1 << m) - 1] << " " << ways[n][(1 << m) - 1] << endl;
}

int main() {
	int T;
	cin >> T;
	for (int nowCase = 1; nowCase <= T; ++nowCase) {
		solve(nowCase);
	}
	return 0;
}