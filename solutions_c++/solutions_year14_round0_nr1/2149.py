#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <map>
#include <set>
using namespace std;

typedef long long		ll;
typedef pair<int, int> 	ii;
typedef vector<ii>		vii;
typedef vector<int>		vi;
typedef set<int>		si;
typedef map<string, int>msi;

#define INF 1000000000
#define REP(i, n) \
	for (int i = 0; i < int(n); i++) //i is local
#define TRvi(c, it) \
	for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) \
	for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) \
	for (msi::iterator it = (c).begin(); it != (c).end(); it++)
#define pb push_back

bool rowContains(int row[], int n) {
	REP(i, 4) {
		if (row[i] == n) {
			return true;
		}
	}
	return false;
}

int main() {
	int T;
	int nCase = 1;
	scanf("%d ", &T);
	while (T--) {
		printf("Case #%d: ", nCase++);
		int first[5][5] = {{0}};
		int second[5][5] = {{0}};
		int firstRow, secondRow;
		scanf("%d ", &firstRow);
		REP(r, 4) {
			REP(c, 4) {
				scanf("%d ", &first[r][c]);
			}
		}
		scanf("%d ", &secondRow);
		REP(r, 4) {
			REP(c, 4) {
				scanf("%d ", &second[r][c]);
			}
		}
		firstRow--; secondRow--;
		int overlap = 0;
		int match = 0;
		REP(c, 4) {
			if (rowContains(second[secondRow], first[firstRow][c])) {
				match = first[firstRow][c];
				overlap++;
			}
		}
		if (overlap == 0) {
			printf("Volunteer cheated!");
		} else if (overlap == 1) {
			printf("%d", match);
		} else {
			printf("Bad magician!");
		}
		printf("\n");
	}
	return 0;
}

