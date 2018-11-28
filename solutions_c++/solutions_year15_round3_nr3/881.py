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

const int size = 40;
int dp[size];

void clear(int i) {
	For(j, 0, size) {
		dp[j] = 0;
	}
}

int ctt= 20;

int solution(int nTest) {
	int c, d, v;
	cin >> c >> d >> v;
	set <int> s;
	For (i, 0, d) {
		int t;
		cin >> t;
		s.insert(t);
	}

	int res = inf;
	For (i, 0, 1 << ctt) {
		set<int> b;
		for (set<int>::iterator it = s.begin(); it != s.end(); it++) {
			b.insert(*it);
		}
		int add = 0;
		For (j, 0, ctt) {
			if (i & (1 << j)) {
				b.insert(j);
				if (s.count(j) == 0) {
					add++;
				}
			}
		}
		For (i, 0, v + 1) {
			dp[i] = 0;
		}
		dp[0] = 1;
		for (set<int>::iterator it = b.begin(); it != b.end(); it++) {
			int u = *it;
			For (j, 0, c) {
				for (int k = v - u; k >= 0; k--) {
					if (dp[k]) {
						dp[k + u] = 1;
					}
				}
			}
		}
		int flag = true;
		For (i, 0, v + 1) {
			if (dp[i] == 0) {
				flag = false;
				break;
			}
		}
		if (flag) {
			res = min(res, add);
		}
	}

	cout << res << endl;

	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 999999;
	scanf("%d", &n);
	init();
	For(i, 0, n) {
		cerr << i << endl;
		printf("Case #%d: ", i + 1);
		clear(i);
		solution(i);
	}

	return 0;
}
	
