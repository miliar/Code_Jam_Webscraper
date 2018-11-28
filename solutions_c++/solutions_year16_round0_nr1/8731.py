#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <ctime>
#include <cassert>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <bitset>
using namespace std;

typedef long double LD;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair <int, int> pii;
typedef pair<LL, LL> pll;
#define pub push_back
#define mp make_pair
const LD EPS = 1e-9;
const int INF = INT_MAX;
const int N = 110;
const LD PI = acosl(-1.0);

//A-small-attempt0.in
int main() {
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		int n, ans;
		cin >> n;
		if (n == 0) {
			cout << "Case #" << i << ": INSOMNIA" << endl;
			continue;
		}
		int a[10] = { 0 };
		for (int j = 1; ; j++) {
			bool flag = 0;
			int k = j * n;
			ans = k;
			while (k > 0) {
				a[k % 10]++;
				k /= 10;
			}
			for (int l = 0; l <= 9; l++)
				if (a[l] == 0)
					flag = 1;
			if (!flag)
				break;
		}
		cout << "Case #" << i << ": " << ans << endl;
	}
	
	return 0;
}