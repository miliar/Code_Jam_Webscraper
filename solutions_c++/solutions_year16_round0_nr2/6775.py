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
	freopen("B_large.in", "r", stdin);
	freopen("B_large.out", "w", stdout);
	ll T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		string str;
		cin >> str;
		ll res = 0;
		str += '+';
		for (int i = str.size() - 2; i >= 0; i--) {
			if (str[i] != str[i + 1]) res++;
		}
		cout << "Case #" << (t + 1) << ": " << res << endl;
		
	}
	return 0;
}