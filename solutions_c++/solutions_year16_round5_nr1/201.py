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
#define FORC(cont, it) for(decltype((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;

#define maxN 22001

int l[maxN], r[maxN];
char S[maxN];

int main() {
	int T, caso = 1;
	cin >> T;
	while (T--) {
		cin >> S;
		int len = strlen(S), ans = 0, st = 0;
		FOR(i, 0, len+1) {
			l[i] = i - 1;
			r[i] = i + 1;
		}
		int llen = len;
		while (st < len) {
			if (S[r[st]] == S[st]) {
				ans += 10;
				l[r[r[st]]] = l[st];
				if (l[st] != -1) {
					r[l[st]] = r[r[st]];
					st = l[st];
				}
				else st = r[r[st]];
				llen -= 2;
			}
			else st = r[st];
		}
		cout << "Case #" << caso++ << ": " << ans+5*(llen/2) << endl;
	}
	return 0;
}
