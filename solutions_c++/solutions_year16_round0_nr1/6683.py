#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <numeric>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <cmath>
#include <list>
#include <set>
#include <map>
#include <ctime>
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
const int INF = (int) 1e9;
const long long INF64 = (long long) 1e18;
const long double eps = 1e-9;
const long double pi = 3.14159265358979323846;
using namespace std;

int main() {
	freopen("A_large.in", "r", stdin);
	freopen("A_large.out", "w", stdout);
	ll T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		map<int, int> mark;
		ll num;
		cin >> num;
		int idx = 1;
		if (num == 0) cout << "Case #" << (t + 1) << ": INSOMNIA" << endl;
		else {
			ll cur = num;
			while (1) {
				ll test = cur;
				while (test) {
					int m = test % 10;
					mark[m] = 1;
					test /= 10;
				}
				if (mark.size() == 10) break;
				idx++;
				cur = num * idx;
			}
			cout << "Case #" << (t + 1) << ": " << cur << endl;
		}
	}
	return 0;
}