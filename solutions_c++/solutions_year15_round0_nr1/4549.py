//============================================================================
// Name        : B.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <vector>
#include <iostream>
#include <cstring>
#include <cstdio>
#define MAXN 1010
using namespace std;
int p[MAXN];
int main() {
//	freopen("B-small-attempt0.in", "r", stdin);
//	freopen("B-small-attempt0.out", "w", stdout);
	int T;
	int ca = 1;
	cin >> T;
	while (T--) {
		int d;
		cin >> d;
		memset(p, 0, sizeof(p));
		for (int i = 0; i < d; i++) {
			int tmp;
			cin >> tmp;
			p[tmp]++;
		}
		int ans = 0;
		while (1) {
			int idx = 0;
			for (int i = MAXN - 1; i >= 0; i--) {
				if (p[i]) {
					idx = i;
					break;
				}
			}
			if (!idx) {
				break;
			}
			int tot = p[idx];

			int a = idx;
			int c = idx / 2 + idx % 2;
			int b = tot + c;
			if (a <= b) {
				for (int i = 0; i < MAXN - 1; i++) {
					p[i] = p[i + 1];
				}
				p[MAXN - 1] = 0;
			} else {
				p[idx] = 0;
				p[idx / 2] += tot;
				p[idx - idx / 2] += tot;
			}
//			for (int i = 0; i < 5; i++) {
//				cout << p[i] << " ";
//			}
//			cout << endl;
			ans++;
		}
		cout << "Case #" << ca++ << ": " << ans << endl;
	}
	return 0;
}
