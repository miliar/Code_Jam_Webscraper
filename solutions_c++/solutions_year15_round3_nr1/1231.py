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

int calcLastRow(int c, int w) {
	int cnt = 0;
	for (int j = c - 1; j >= w; j -= w)
		cnt++;
	return cnt + w;
}

int calc(int r, int c, int w) {
	int cnt = 0;
	// can be equation bs fakes tfkeer!
	for (int i = 0; i < r - 1; ++i)
		for (int j = w - 1; j < c; j += w)
			cnt++;
	return cnt + calcLastRow(c, w);
}

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.in", "rt", stdin);
	freopen("output.out", "wt", stdout);
#endif
	int T, r, c, w;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		cin >> r >> c >> w;
		int sol = calc(r, c, w);
		printf("Case #%d: %d\n", t + 1, sol);
	}

	return 0;
}
