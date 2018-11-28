#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>

using namespace std;

int a[200][200];

string solve() {
	int n, m;

	cin >> n >> m;
	
	for (int  i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			cin >> a[i][j];
		}
	}
	
	for (int l = 1; l <= 100; ++l) {
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				if (a[i][j] == l) {
					bool f = true;
					for (int k = 0; k < n; ++k) {
						if (a[k][j] > a[i][j]) {
							f = false;
							break;
						}
					}
					if (!f) {
						f = true;
						for (int k = 0; k < m; ++k) {
							if (a[i][k] > a[i][j]) {
								f = false;
								break;
							}
						}
						if (!f) {
							return "NO";
						}
					}
				}
			}
		}
	}
	
	return "YES";
}

int main() {
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	
	int n;
	
	cin >> n;
	
	for (int i = 0; i < n; ++i) {
		cout << "Case #" << i + 1 << ": ";
		cout << solve() << endl;
	}
	
	return 0;
}
