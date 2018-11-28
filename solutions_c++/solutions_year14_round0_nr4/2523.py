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
#define rall(v) v.rbegin(),v.rend()
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

int n;
vector<double> nm, kn;

int playWar() {
	int w = n;
	sort(all(nm));
	sort(all(kn));

	int i = 0, j = 0;
	w = n;
	for (i = 0; i < n && j < n; ++i) {
		while (j < n && nm[i] > kn[j])
			j++;
		if (j < n && nm[i] < kn[j])
			w--, j++;
	}
	return w;
}

int playDWar() {
	int score = 0;
	sort(rall(nm));
	sort(rall(kn));
	while (nm.size()) {
		if (nm[0] > kn[0]) {
			nm .erase(nm.begin()), kn.erase(kn.begin()), n--, score++;
		} else {
			if (nm[n - 1] > kn[0])
				score++;
			nm.pop_back(), kn.erase(kn.begin()), n--;
		}
	}
	return score;
}

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	int TS, w, dw;
	double x;
	cin >> TS;
	for (int tt = 1; tt <= TS; ++tt) {

		cin >> n;

		nm.clear();
		kn.clear();

		for (int i = 0; i < n; ++i)
			cin >> x, nm .push_back(x);
		for (int i = 0; i < n; ++i)
			cin >> x, kn .push_back(x);
		w = playWar();
		dw = playDWar();
		printf("Case #%d: %d %d\n", tt, dw, w);

	}
	return 0;
}
