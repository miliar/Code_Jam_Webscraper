#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <string>
#include <cstring>
#include <cstdio>
#include <cassert>
using namespace std;

void openFiles() {
#ifndef ONLINE_JUDGE
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("B-small-attempt0.out", "wt", stdout);
#endif
}

int flip(int n, int k, int b) {
	for (int i = 0; i < k; i++)
		b ^= (1 << (n - i - 1));
	return b;
}

void printBinary(int n, int b) {
	for (int i = 0; i < n; i++) {
		cout << (b & 1);
		b >>= 1;
	}
}

typedef pair<int, int> pii;

pii readBinary() {
	char line[200];
	scanf("%s ", line);
	int len = strlen(line);
	int b = 0;
	for (int i = 0; i < len; i++) {
		b <<= 1;
		char c = line[i];
		if (c == '+') b |= 1;
		else if (c == '-') c = line[i];
		else throw 1;
	}
	return pii(len, b);
}

void solve() {
	pii p = readBinary();
	int n = p.first, b = p.second;
	queue<int> q;
	q.push(b);
	map<int, int> dist;
	dist[b] = 0;

	int target = (1 << n) - 1;

	while (!q.empty()) {
		int x = q.front(); q.pop();		
		int d = dist[x];
		if (x == target) {
			cout << dist[x] << endl;
			return;
		}
		for (int k = 1; k <= n; k++) {
			int y = flip(n, k, x);
			if (!dist.count(y)) {
				dist[y] = d + 1;
				q.push(y);
				//cout << "from "; printBinary(n, x); cout << " to "; printBinary(n, y); cout << endl;
			}
		}
	}

	//cout << "FAIL" << endl;
}

int main() {
    openFiles();
    int n; scanf("%d ", &n);
    for (int i = 0; i < n; i++) {
            printf("Case #%d: ", i + 1);
            solve();
    }

    return 0;
}
