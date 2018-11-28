#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <complex> 
#include <ctime>
#include <cstring>

using namespace std;

#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()

int ans = 1000;
int cur = 0;
vector<vector<int>> edge;

vector<int> x(4);

bool bf1(const vector<int> &q, int k, int n, int f) {
	if (k == sz(q)) 
		return true;
	bool fl = false;
	for (int i = 0; i < n; ++i)
		if (i != f && edge[i][q[k]] && !x[i]) {
			x[i] = 1;
			if (bf1(q, k + 1, n, f))
				fl = true;
			x[i] = 0;
		}
	return fl;
}


void bf(int k, int n) {
	if (k == n * n) {
		bool f = true;
		for (int i = 0; i < n; ++i) {
			vector<int> q;
			for (int j = 0; j < n; ++j)
				if (edge[i][j] == 1)
					q.push_back(j);
			if (sz(q) == n)
				continue;
			x.assign(4, 0);
			if (bf1(q, 0, n, i))
				f = false;
		}
		if (f)
			ans = min(ans, cur);
		return;
	}


	int i = k / n;
	int j = k % n;
	bf(k + 1, n);

	if (edge[i][j] == 0) {
		++cur;
		edge[i][j] = 1;
		bf(k + 1, n);
		edge[i][j] = 0;
		--cur;
	}
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tests;
    cin >> tests;
    edge.resize(4);
    for (int i = 0; i < 4; ++i)
    	edge[i].resize(4);

    for (int t = 0; t < tests; ++t) {
    	cout << "Case #" << t + 1 << ": ";
    	int n;
    	cin >> n;
    	for (int i = 0; i < n; ++i) {
    		string s;
    		cin >> s;
    		for (int j = 0; j < n; ++j)
    			edge[i][j] = s[j] - '0';
    	}
    	ans = 1000;
    	bf(0, n);
    	cout << ans << endl;
    }

    return 0;
}