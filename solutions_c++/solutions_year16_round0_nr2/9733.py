#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <iomanip>
#include <iostream>
#include <queue>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

#define INF 1000000000
#define FOR(i, a, b) for(int i=int(a); i<int(b); i++)
#define FORC(cont, it) for(typeof((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;

#define maxN 11

int ans[maxN][1 << maxN], q[1<<maxN];

int swapBits(int num, int fb) {
	int ret = num&~((1<<fb)-1), s=0;
	FOR(i, 0, fb) {
		s <<= 1;
		if (num & 1 << i) s+=0;
		else s++;
	}
	return ret+s;
}

int main() {
	int T, caso = 1;
	string S;
	cin >> T;
	FOR(i, 0, maxN) {
		FOR(j, 0, 1 << maxN) ans[i][j] = INF;
	}
	FOR(i, 1, maxN) {
		ans[i][0] = 0;
		int qt = 1;
		q[0] = 0;
		for (int qh = 0; qh < qt; qh++) {
			FOR(j, 1, i+1) {
				int k = swapBits(q[qh], j);
				if (ans[i][k]>ans[i][q[qh]]+1) {
					q[qt++] = k;
					ans[i][k] = ans[i][q[qh]] + 1;
				}
			}
		}
	}
	while (T--) {
		cin >> S;
		int v = 0;
		FOR(i, 0, S.length()) {
			v |= (S[i] == '-') << i;
		}
		cout << "Case #" << caso++ << ": ";
		cout << ans[S.length()][v] << endl;
	}
	return 0;
}
