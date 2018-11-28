#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

const int MAXN = 2010;

int T, N;
int a[MAXN], b[MAXN], x[MAXN];

int main() {
	cin >> T;
	for (int c = 0; c < T; ++c) {
		cin >> N;
		for (int i = 0; i < N; ++i) {
			cin >> a[i];
		}
		for (int i = 0; i < N; ++i) {
			cin >> b[i];
		}
		for (int i = 0; i < N; ++i) {
			x[i] = -1;
		}
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				if (x[j] != -1) continue;
				if (a[j] + b[j] > i + 2) continue;
				int l = 1;
				int r = 1;
				bool find = true;
				for (int k = 0; k < j; ++k) {
					if (x[k] > 0 && x[k] < i + 1 && a[k] + 1 > l) {
						l = a[k] + 1;
					}
					if (x[k] < 0 && b[k] < b[j] + 1) {
						find = false;
					}
				}
				for (int k = j + 1; k < N; ++k) {
					if (x[k] > 0 && x[k] < i + 1 && b[k] + 1 > r) {
						r = b[k] + 1;
					}
					if (x[k] < 0 && a[k] < a[j] + 1) {
						find = false;
					}
				}
				if (!find) continue;
				if (l == a[j] && r == b[j]) {
					x[j] = i + 1;
					break;
				}
			}
		}
		cout << "Case #" << c + 1 << ":";
		for (int i = 0; i < N; ++i) {
			cout << " " << x[i];
		}
		cout << endl;
	}
	return 0;
}
