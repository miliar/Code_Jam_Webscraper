#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cstring>
using namespace std;

int ntest, a, b;

bool isPalin(int x) {
	string s = "";
	while (x > 0) {
		s += char(x % 10 + '0');
		x /= 10;
	}
	for (int i = 0, j = s.length() - 1; i < j; i++, j--)
		if (s[i] != s[j]) return false;
	return true;
}

int main() {
	//freopen("input.txt", "r", stdin);
	freopen("c_small.in", "r", stdin);
	freopen("c_small.out", "w", stdout);
	cin >> ntest;
	for (int test = 0; test < ntest; test++) {
		cin >> a >> b;
		int ans = 0;
		for (int i = 1; i <= b; i++) 
			if (isPalin(i)) {
				int j = i * i;
				if (isPalin(j) && j >= a && j <= b) ans++;
			}
		cout << "Case #" << test + 1<< ": " << ans << endl;
	}
}
