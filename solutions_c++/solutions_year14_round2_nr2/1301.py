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

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	int ts, a, b, c;
	scanf("%d", &ts);
	for (int t = 1; t <= ts; ++t) {
		scanf("%d %d %d", &a, &b , &c);
		int cnt = 0;
		for (int i = 0; i < a; ++i) {
			for (int j = 0; j < b; ++j) {
				if ((i & j) < c)
					cnt++;
			}
		}

		printf("Case #%d: %d\n", t, cnt);
	}

	return 0;
}
