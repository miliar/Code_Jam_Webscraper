#include <iostream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string.h>
#include <utility>
#include <queue>
#include <stack>
#include <iomanip>
#include <ctype.h>
#include <sstream>
#include <map>
#include <set>
#include <stdio.h>
#include <assert.h>
#include <ctype.h>

using namespace std;

#define FOR(i,n) for(int i = 0;i < n;i++)
#define FORR(i,n) for(int i = n-1;i >= 0;i--)
#define REP(i,a,b) for(int i = (a);i<(b);++i)
#define MP make_pair
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define PII pair<int,int>
#define sz(a) (int)(a).size()
#define CLEAR(a) memset(a, 0, sizeof(a))
#define INF 2000000000

typedef long long LL;

int a[1005];

void solve() {
	int n;
	//cout << endl;
	cin >> n;
	FOR(i,n)
	cin >> a[i];

	int l = 0;
	int r = n-1,p;

	int res = 0;
	FOR(it,n) {
		int mn = 2000000000;
		for (int i = l; i <= r; i++) {
			if (a[i] < mn) {
				mn = a[i];
				p = i;
			}
		}

		if (p - l <= r - p) {
			res += (p - l);
			for (int j = p; j > l; j--) {
				swap(a[j], a[j-1]);
			}
			l++;
		} else {
			res += (r - p);
			for (int j = p; j < r; j++) {
				swap(a[j], a[j+1]);
			}
			r--;
		}
	}

	cout << res << endl;
}

int main() {
  ios_base::sync_with_stdio(0);
  int tt;
  cin >> tt;

  FOR(tn,tt) {
    cout << "Case #" << tn + 1 << ": ";
    solve();
  }

  return 0;
}
