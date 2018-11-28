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

const int size = 11;
int dp[size][size];

void clear(int i) {
	For(i, 0, size) {
		For(j, 0, size) {
			dp[i][j] = 0;
		}
	}
}

int solution(int nTest) {
	int e, r, n;
	scanf("%d%d%d", &e, &r, &n);
	vector<int> v;
	For(i, 0, n) {
		int t;
		scanf("%d", &t);
		v.pb(t);
	}
	For(i, 0, n) {
		For(j, 1, e + 1) {
			For(k, 0, j + 1) {
				int rest = (j - k) + r;
				rest = min(rest, e);
				dp[i+1][rest] = max(dp[i+1][rest],
						dp[i][j] + k * v[i]);
			}
		}
	}
	int res = 0;
	For(i, 0, e + 1) {
		res = max(res, dp[n][i]);
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
	
