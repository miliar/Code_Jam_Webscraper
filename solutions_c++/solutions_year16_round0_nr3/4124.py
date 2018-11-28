#include <string>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string.h>
#include <utility>
#include <queue>
#include <stack>
#include <iomanip>
#include <ctype.h>
#include <map>
#include <set>
#include <stdio.h>
#include <assert.h>
#include <ctype.h>
#include <math.h>
#include <time.h>
#include <iostream>
#include <iomanip>

using namespace std;

typedef long long LL;

#define FOR(i,n) for(int i = 0;i < n;i++)
#define MP make_pair
#define PB push_back
#define ALL(a) (a).begin(),(a).end()
#define PII pair<int, int>
#define PLL pair<long long, long long>
#define CLEAR(a) memset(a, 0, sizeof(a))
#define INF 2000000007
#define y1 uu1
#define y2 uu2
#define hash mash
const double EPS = 1E-12;
const double PI = acos(-1.0);
const LL mod = 1000000007;

using namespace std;

string ans[50];
vector<LL> ansd[50];
int res = 0;

int a[16];

void go() {
	a[0] = a[15] = 1;
	for (int i = 1; i < 15; i++) {
		a[i] = rand() % 2;
	}

	vector<LL> q;
	for (int i = 2; i <= 10; i++) {
		LL z = 0;
		LL cur = 1;
		FOR(j, 16) {
			if (a[j]) z += cur;
			cur *= (LL)i;
		}

		bool g = 0;
		for (LL j = 2; j <= 10000; j++) {
			if (z % j == 0) {
				q.push_back(j);
				g = 1;
				break;
			}
		}

		if (!g) return;
	}

	string ss = "";
	for (int i = 15; i >= 0; i--) ss += (char)('0' + a[i]);

	ans[res] = ss;
	ansd[res] = q;
	res++;

	//cout << "FOUND " << res << endl;
}

int main() {
  ios_base::sync_with_stdio(0);

  while (res < 50) {
  	go();
  }

  cout << "Case #1:" << endl;

  FOR(i, 50) {
  	cout << ans[i];
  	FOR(j, ansd[i].size()) cout << ' ' << ansd[i][j];
  	cout << endl;
  } 
  cout << endl;

  return 0;
}
