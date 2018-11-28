#include <iostream>
#include <math.h>
#include <string.h>
#include <string>
#include <cmath>
#include <stdio.h>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <functional>
#include <algorithm>
#include <bitset>
#include <set>
#include <stack>
#include <limits>
#include <sstream>
#include <ctime> 
#define endl '\n'
#pragma warning (disable : 4996)

using namespace std;

#define lli long long int
#define ull unsigned long long int
#define MP make_pair

const int N = (int)(2e7 + 20);
const int L = 20;
const lli M = 1000000007;
const double E = 1e-7;

int bits(int n) {
	int res = 0;
	while (n) {
		res += n & 1;
		n /= 2;
	}
	return res;
}

int p[10][10];

int main()
{
	ios_base::sync_with_stdio(0);
#ifdef FILE_IO
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif      
	int T;
	cin >> T;

	for (int qq = 0; qq < T; ++qq) {
		cout << "Case #" << (qq + 1) << ": ";

		int n, r, c;
		cin >> r >> c >> n;
		int b = (1 << (r*c));
		int ans = 202020;

		for (int mask = 0; mask < b; ++mask) {
			if (bits(mask) == n) {
				int la = 0;
				int tm = mask;
				for (int i = 0; i < r; ++i) {
					for (int j = 0; j < c; ++j) {
						p[i][j] = (tm & 1);
						tm >>= 1;
						if (p[i][j])
							la += (i > 0) * p[i - 1][j] + (j > 0) * p[i][j - 1];
					}
				}
				ans = min(ans, la);
			}
		}

		cout << ans;

		cout << endl;
	}
}