#include <cmath>
#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
#include <stack>
#include <queue>
#include <cstring>
#include <cstdio>
#include <string>
#include <functional>

#define all(cont) cont.begin(), cont.end()
#define rall(cont) cont.end(), cont.begin()
#define tr(cont, it) for (typeof(cont.begin()) it = cont.begin() ; it != cont.end() ; it++)
#define FOR(i, j, k, l) for(int i=(j) ; i<(k) ; i+=(l))
#define rep(i, j) FOR(i, 0, j, 1)
#define rrep(i, j) FOR(i, j, -1, -1)

#define INF 1000000000

using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef long long ll;

int C, board1[4][4], board2[4][4];
int g1, g2;

int main() {
	scanf("%d", &C);
	for (int c=1 ; c<=C ; c++) {
		scanf("%d", &g1);
		rep(i, 4) rep(j, 4)
			scanf("%d", &board1[i][j]);
		scanf("%d", &g2);
		rep(i, 4) rep(j, 4)
			scanf("%d", &board2[i][j]);
		g1--, g2--;
		vector<int> f, s;
		rep(i, 4) {
			f.push_back(board1[g1][i]);
		}

		rep(i, 4) {
			s.push_back(board2[g2][i]);
		}

		int repeated = 0, n;
		rep(i, 4) {
			rep(j, 4) {
				if (f[i] == s[j]) {
					repeated++;
					n = f[i];
					break;
				}
			}
		}
		printf("Case #%d: ", c);
		if (repeated == 0) {
			printf("Volunteer cheated!\n");
		}
		else if (repeated == 1) {
			printf("%d\n", n);
		}
		else {
			printf("Bad magician!\n");
		}
	}
}