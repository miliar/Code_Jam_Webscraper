#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <map>
#include <vector>
#include <string>
#include <cctype>
#include <set>
#include <utility>
#include <stack>
#include <iostream>

using namespace std;

int t,k;
typedef long long ll;
typedef pair<int, int> pii;
const double eps = 1e-1;

int main (){
	#ifdef INTERNO
		freopen("in", "r", stdin);
		freopen("out", "w", stdout);
	#endif
	scanf("%d", &t);
	double r,n;
	for(int _ = 1; _ <= t; ++_){
		scanf("%lf %lf", &r, &n);
		int tot = 0;
		double area, rr = r;
		int lo = 0, hi = 1000000001,mid;
		while(hi-lo > 1){
			mid = (hi+lo)/2;
			area = (r+r+(mid<<1)-1);
			area *= ((r+(mid<<1)-1)-r+1)/2;
			if(area > n+eps) hi = mid;
			else lo = mid;
		}
		printf("Case #%d: %d\n", _, lo);
	}
	return 0;
}
