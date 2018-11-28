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

void solve() {
	int x1, x2, x, a[20], b[20];
	vector<int> c;
	cin >> x1;
	--x1;
	for (int i = 0; i < 16; ++i) {
		cin >> x;
		--x;
		a[x] = i / 4;	
	}
	cin >> x2;
	--x2;
	for (int i = 0; i < 16; ++i) {
		cin >> x;
		--x;
		b[x] = i / 4;
	}
	for (int i = 0; i < 16; ++i) {
		if (a[i] == x1 && b[i] == x2) {
			c.push_back(i + 1);
		}
	}
	
	if (c.size() == 0) {
		cout << "Volunteer cheated!" << endl;
	} else if (c.size() == 1) {
		cout << c[0] << endl;
	} else {
		cout << "Bad magician!" << endl;
	}
}

int main() {
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
	
	return 0;
}
