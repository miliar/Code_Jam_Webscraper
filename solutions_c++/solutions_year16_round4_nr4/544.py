//be naame khodaa

#include <iostream>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <string>
#include <cstdio>
#include <algorithm>
#include <set>
#include <cassert>
#include <iomanip>
#include <cstring>
typedef long long ll;

using namespace std;
typedef pair <int, int> pii;

bool mark[4];
int a[4][4];
char c[4][4];
bool f = false;

bool BT2(int y, int x, int n){
	if (x == n) return true;
	if (a[y][x] == 0) return BT2(y, x+1, n);
	for (int ii = 0; ii < n; ii++){
		if (ii != y && !mark[ii] && a[ii][x]){
			mark[ii] = true;
			if (BT2(y, x+1, n)) { mark[ii] = false; return true; }
			mark[ii] = false;
		}
	}
	return false;
}

bool good(int n){
	for (int i = 0; i < n; i++)
		if (BT2(i, 0, n))
			return false;
	return true;
}

int BT(int ii, int n){
	if (ii == n*n) return (good(n) ? 0 : n*n);
	int y = ii/n, x = ii%n, res = n*n;
	res = min(res, BT(ii+1, n));
	if (a[y][x] == 0){
		a[y][x] = 1;
		res = min(res, BT(ii+1, n) + 1);
		a[y][x] = 0;
	}
	return res;
}

int main()
{
	ios_base::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int it = 1; it <= t; it++){
		int n;
		cin >> n;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				cin >> c[i][j], a[i][j] = (c[i][j] == '1' ? 1 : 0);
		cout << "Case #" << it << ": " << BT(0, n) << '\n';
	}
	return 0;
}
