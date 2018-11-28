#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <complex>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
#define fi first
#define se second
#define rep(i, n) for (int i = 0, _##i = (n); i < _##i; ++i)
#define pb push_back
#define pf push_front
#define MAXN 110
#define MAXM 110
#define PROBNAME "lawn"

int rowmax[MAXM];
int colmax[MAXN];
int arr[MAXN][MAXM];

int main() {  
	freopen(PROBNAME".in","r",stdin); freopen(PROBNAME".out","w",stdout);
	int t;
	cin >> t;
	rep(z, t) {
		int n, m;
		bool ans = 1;
		cin >> n >> m;
		cout << "Case #" << z+1 << ": ";
		rep(i, n) {
			rep(j, m) {
				cin >> arr[i][j];
			}
		}
		//precomp row and colmax
		rep(i, m) {
			rowmax[i] = arr[0][i];
			rep(j, n) {
				rowmax[i] = max(rowmax[i], arr[j][i]);
			}
		}
		rep(i, n) {
			colmax[i] = arr[i][0];
			rep(j, m) {
				colmax[i] = max(colmax[i], arr[i][j]);
			}
		}
		//check: if any value is less than max for both its row and columns, then NO
		rep(i, n) {
			rep(j, m) {
				if (arr[i][j] < rowmax[j] && arr[i][j] < colmax[i]) {
					ans = 0;
				}
			}
		}
		if (ans == 0) cout << "NO\n";
		else if (ans == 1) cout << "YES\n";
	}
	return 0;
}