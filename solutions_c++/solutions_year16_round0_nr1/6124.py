#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <cstring>
#include <string>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <limits>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef pair<int,int> pii;
typedef vector<vector<int> > graph;

const double pi = acos(-1.0);

#define oned(a, x1, x2) { cout << #a << ":"; for(int _i = (x1); _i < (x2); _i++){ cout << " " << a[_i]; } cout << endl; }
#define twod(a, x1, x2, y1, y2) { cout << #a << ":" << endl; for(int _i = (x1); _i < (x2); _i++){ for(int _j = (y1); _j < (y2); _j++){ cout << (_j > y1 ? " " : "") << a[_i][_j]; } cout << endl; } }

#define mp make_pair
#define pb push_back
#define fst first
#define snd second

int n;

void solve() {
	if(n==0) {
		printf("INSOMNIA\n");
	} else {
		int dig[10];
		int cnt = 0;
		memset(dig,0,sizeof(dig));
		ll x = 0;
		while(cnt<10) {
			x += n;
			ll y = x;
			while(y > 0) {
				int d = y%10;
				y /= 10;
				if(dig[d]==0) {
					cnt++;
					dig[d] = 1;
				}
			}
		}
		printf("%lld\n", x);
	}
}

int main() {
	int t; scanf("%d", &t);
	for(int c = 1; c <= t; c++) {
		scanf("%d", &n);
		printf("Case #%d: ", c);
		solve();
	}
}
