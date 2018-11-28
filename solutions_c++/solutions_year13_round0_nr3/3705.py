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

int freq[1011];

bool isPlaindrom(int x) {
	int tmp = x, y = 0;
	while (tmp) {
		y *= 10;
		y += (tmp % 10);
		tmp /= 10;
	}
	return (y == x);
}

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.in", "rt", stdin);
	freopen("output.out", "wt", stdout);
#endif
	for (int i = 1; i < 1011; ++i) {
		freq[i] = freq[i - 1];
		int sq = sqrt(i);
		if (sq * sq == i)
			if (isPlaindrom(i) && isPlaindrom(sqrt(i))) {
				freq[i]++;
			}
	}
	int T, A, B;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		cin >> A >> B;
		printf("Case #%i: %i\n", t + 1, freq[B]-freq[A-1]);
	}
	return 0;
}
