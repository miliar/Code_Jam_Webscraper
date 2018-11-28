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

double f, c, x;

double calc() {
	double prev = x / 2.0;
	double farmCost = c / 2.0;
	double s = 2.0 + f;
	double cur = farmCost + (x / s);

	for (int i = 0; i < x; i++) {
		if (cur > prev) {
			break;
		}
		prev = cur;
		farmCost += (c / s);
		s += f;
		cur = farmCost + (x / s);
	}
	return prev;
}

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	int TC;
	scanf("%d", &TC);
	for (int t = 1; t <= TC; ++t) {
		cin >> c >> f >> x;
		printf("Case #%d: %.7lf\n", t, calc());
	}
	return 0;
}
