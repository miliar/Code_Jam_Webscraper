#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;
typedef long long ll;
typedef double R;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i, s, t) for(i = (s); i < (t); i++)
#define RFOR(i, s, t) for(i = (s)-1; i >= (t); i--)
const int MAXN = 1123456;
int a[MAXN];

int main() {
#ifdef LOCAL
	freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
#endif
	int i0 = 1;
	int T;
	scanf("%d", &T);
	for (i0 = 1; i0 <= T; i0++) {
		int i, j, k;
		int n;
		scanf("%d", &n);
		{
			int p, q, r, s;
			scanf("%d%d%d%d", &p, &q, &r, &s);
			for(i = 0; i < n; i++)
				a[i] = ((ll)i*p+q)%r+s;
		}
		ll l, r;
		l = 0;
		r = 1LL<<50;
		while(r-l > 1){
			ll mid = (r+l)/2;
			ll sum = 0;
			int cnt = 0;
			bool bad = false;
			for(i = 0; i < n; i++){
				if(sum+a[i] > mid){
					sum = 0;
					cnt++;
				}
				sum += a[i];
				if(sum > mid)
					bad = true;
			}
			if(bad || cnt > 2){
				l = mid;
			}
			else{
				r = mid;
			}
		}

		ll sum = 0;
		for(i = 0; i < n; i++)
			sum += a[i];


		printf("Case #%d: %.10f\n", i0, 1-((R)r/sum));
	}
	return 0;
}
