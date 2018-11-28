#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <bitset>
#include <set>
#include <sstream>
#include <stdlib.h>
#include <map>
#include <queue>
#include <assert.h>
#include <deque>
#include <string.h>


using namespace std;

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

typedef long long int64;

typedef vector <int> vi;
typedef vector <vi> vvi;



const string bad = "Bad magician!";
const string cheat = "Volunteer cheated!";


void update(vi& a) {
	int ans;
	cin >> ans;
	--ans;
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			int x;
			cin >> x;
			if (i == ans) {
				++a[x];
			}
		}
	}
}

void solve() {
	vi a(17);
	update(a);
	update(a);
	int num2 = 0;
	int best = 0;
	for (int i = 1; i < 17; ++i) {
		if (a[i] == 2) {
			++num2;
			best = i;
		}
	}
	if (num2 == 0) cout << cheat << endl;
	else if (num2 == 1) cout << best << endl;
	else cout << bad << endl;
}

int main () {
	//freopen("", "rt", stdin);
	//freopen("", "wt", stdout);
	//std::ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		cout << "Case #" << t + 1 << ": ";
		solve();
	}


    return 0;
}

