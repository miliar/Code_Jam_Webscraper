#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <ctype.h>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;

const int N = 2e3;
#define MP make_pair
#define lli long long int

int f[N], d[N];
int ans;
vector<int> masks[N];


bool check(int l) {
	int v = (1 << l);
	vector<int> test(l);
	do {

	} while (next_permutation(test.begin(), test.end()));
	return 1;
}

int bc(int v) {
	int res = 0;
	while (v) {
		res += v & 1;
		v >>= 1;
	}
	return v;
}

bool used[N];
int answer;

bool isFriends(int v, int from) {
	if (from <= 0) return true;
	if (f[v] == from) return true;
	return false;
}

int n;
void dfs(int v, int from) {
	bool friends = isFriends(v, from);
	if (d[v] >= 0) {
		if (friends || d[f[v]] == d[v] + 1) {
			int l = d[from] - d[v];
			answer = max(answer, l + 1);
		}
		return;
	}
	else {
		if (from >= 0) d[v] = d[from] + 1;
		else d[v] = 0;

		if (!friends) {
			dfs(f[v], v);
		}
		else {
			for (int i = 1; i <= n; ++i) {
				if (i != v) dfs(i, v);
			}
		}
	}
	
	d[v] = -1;
}

int main() {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;

	int b = (1 << 10);
	for (int i = 1; i < b; ++i) {
		masks[bc(i)].push_back(i);
	}
	memset(d, -1, N*sizeof(int));

	for (int qq = 0; qq < T; ++qq) {
		cout << "Case #" << (qq + 1) << ": ";
		
		cin >> n;
		for (int i = 1; i <= n; ++i) cin >> f[i];
		answer = 0;
		for (int i = 1; i <= n; ++i) {
			dfs(i, -1);
		}
		cout << answer;

		cout << endl;
	}
}