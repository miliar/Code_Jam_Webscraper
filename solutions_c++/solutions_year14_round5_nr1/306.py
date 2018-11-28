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

int TESTS, CASE;

const int MAXN = 1000005;

int n;
ll p, q, r, s, a[MAXN], sum[MAXN];

ll getSum(int l, int r) {
	if(l>r) return 0;
	return sum[r] - (l?sum[l-1]:0);
}

void solve() {
	cout << "Case #" << CASE << ": ";
	memset(sum,0,sizeof(sum));
	for(int i = 0; i < n; i++) {
		a[i] = (i * p + q) % r + s;
		sum[i] = (i?sum[i-1]:0) + a[i];
	}
	
	ll total = sum[n-1];
	
	ll cnt = 0;
	
	for(int i = 0; i+1 < n; i++) {
		cnt = max(cnt,min(getSum(0,i),getSum(i+1,n-1)));
	}
	
	if(n >= 3) {
		int r = 1;
		ll midSum = a[1];
		for(int l = 1; l+1 < n; l++) {
			ll leftSum = getSum(0,l-1);
			ll rightSum = getSum(r+1,n-1);
			while(r+1 < n-1 && (midSum < rightSum || midSum < leftSum)) {
				r++;
				midSum += a[r];
				rightSum -= a[r];
			}
			if(leftSum <= midSum && midSum >= rightSum) {
				cnt = max(cnt,leftSum+rightSum);
			}
			midSum -= a[l];
		}
		
		ll leftSum = 0;
		r = 1;
		for(int l = 0; l < n-2; l++) {
			leftSum += a[l];
			r = max(r,l+1);
			midSum = getSum(l+1,r);
			ll rightSum = getSum(r+1,n-1);
			while(r+1<n-1 && midSum+a[r+1]<=leftSum) {
				r++;
				midSum += a[r];
				rightSum -= a[r];
			}
			if(leftSum >= midSum && leftSum >= rightSum) {
				cnt = max(cnt,midSum+rightSum);
			}
		}
		
		ll rightSum = 0;
		int l = n-2;
		for(r = n-1; r >= 2; r--) {
			rightSum += a[r];
			l = min(l,r-1);
			midSum = getSum(l,r-1);
			leftSum = getSum(0,l-1);
			while(l-1 >= 1 && midSum+a[l-1]<=rightSum) {
				l--;
				midSum += a[l];
				leftSum -= a[l];
			}
			if(rightSum >= leftSum && rightSum >= midSum) {
				cnt = max(cnt,leftSum+midSum);
			}
		}
	}
	cout << fixed << setprecision(12) << cnt*1./total << '\n';
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	ios_base::sync_with_stdio(false);
	cin >> TESTS;
	for(CASE = 1; CASE <= TESTS; CASE++) {
		cin >> n >> p >> q >> r >> s;
		solve();
	}
}
