#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <map>
#include <set>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;

const int N = 1010;

int a[N], b[N];

int main() {
	int T;
	scanf("%d\n", &T);
	for (int test = 1; test <= T; ++test) {
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &a[i]);
			b[i] = a[i];
		}
		sort(b, b + n);
		int nextleft = 0, nextright = n - 1;
		int ans = 0;
		for (int t = 0; t < n; ++t) {
			int now = b[t];
			int j = 0;
			for (int i = 0; i < n; ++i) {
				if (a[i] == now) {
					j = i;
					break;
				}
			}
			if (j - nextleft < nextright - j) {
				for (int i = j; i > nextleft; --i) {
					swap(a[i], a[i - 1]);
					++ans;
				}
				++nextleft;
			} else {
				for (int i = j; i < nextright; ++i) {
					swap(a[i], a[i + 1]);
					++ans;
				}
				--nextright;
			}
		}
		//for (int i = 0; i < n; ++i) cout << a[i] << ' '; cout << endl;
		printf("Case #%d: %d\n", test, ans);
	}
	return 0;
}