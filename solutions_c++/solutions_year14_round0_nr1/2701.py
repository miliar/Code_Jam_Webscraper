#include <map>
#include <set>
#include <math.h>
#include <deque>
#include <stack>
#include <queue>
#include <vector>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <stdio.h>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rep(i,s,m) for(int i=s;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define PI = (2.0 * acos(0.0));
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define OO ((int)1e9)
#define sz 10010

int di[] = { -1, 0, 1, 0 };
int dj[] = { 0, 1, 0, -1 };

int row1[4], row2[4];

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.in", "rt", stdin);
	freopen("output.out", "wt", stdout);
#endif
	int TS, r1, r2, x;
	scanf("%d", &TS);
	for (int t = 1; t <= TS; ++t) {
		scanf("%d", &r1);
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				scanf("%d", &x);
				if (i + 1 == r1)
					row1[j] = x;
			}
		}
		scanf("%d", &r2);
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				scanf("%d", &x);
				if (i + 1 == r2)
					row2[j] = x;
			}
		}
		int idx = -1;
		x = 0;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				if (row1[i] == row2[j])
					x++, idx = i;
			}
		}
		switch (x) {
		case 0:
			printf("Case #%d: Volunteer cheated!\n", t);
			break;
		case 1:
			printf("Case #%d: %d\n", t, row1[idx]);
			break;
		default:
			printf("Case #%d: Bad magician!\n", t);
			break;
		}
	}

	//Case
	//#2: Bad magician!

	return 0;
}
