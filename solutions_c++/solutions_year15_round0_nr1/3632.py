#include <iostream>
#include <string>
#include <sstream>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstring>
#include <list>
#include <bitset>
#include <numeric>
using namespace std;

#define ll long long
#define ull unsigned long long
#define INF 1e9
#define MOD 1000000007
#define getcx getchar_unlocked
#define putcx putchar_unlocked
//setprecision - cout << setprecision (4) << f << endl; Prints x.xxxx
//setbase - cout << setbase (16); cout << 100 << endl; Prints 64

int main() {
	ios_base::sync_with_stdio(0);

	int T, temp;
	string d;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> temp >> d;
		int ans = 0;
		int count = 0;
		for (int i = 0; i < d.length(); i++) {
			if (count < i) {
				ans = ans + i - count;
				count = count + i - count;
			}
			count = count + (d[i] - '0');
		}
		cout << "Case #" << t << ": " << ans << endl;
	}

	return 0;
}