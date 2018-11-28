#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <ctime>
using namespace std;
typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
#define PB push_back
#define MP make_pair
#define FOR(i, n) for(int i = 0; i < (n); i++)
#define REP(i, a, b) for(int i = (a); i <= (b); i++)
#define CLR(x, a) memset(x, a, sizeof(x))
//#define L(x) ((x) << 1)
#define R(x) (((x) << 1) + 1)
#define LB(x) ((x)&(-(x)))
#define SL(x) (1 << (x))
#define X first
#define Y second
const int MAXN = 10000 + 20;

int n, x, s[MAXN];

void solve() {
	cin >> n >> x;
	FOR(i, n) cin >> s[i];
	sort(s, s + n);
	int res = 0;
	for (int i = n - 1, j = 0; i >= j;) {
		if (i == j) {
			if (s[i] <= x) {
				i--;
			}
		} else {
			if (s[i] + s[j] <= x) {
				i--;
				j++;
			} else {
				i--;
			}	
		}
		res++;
	}
	cout << res << endl;
}

int main(){
	int T; cin >> T;
	FOR(cas, T){
		printf("Case #%d: ", cas + 1);
		solve();
	}
}