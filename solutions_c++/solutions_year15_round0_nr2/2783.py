#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
using namespace std;
int t,n, ans, tmp, maks;
int a[1005];
int main(){
	scanf("%d",&t);
	for (int tc = 1; tc <= t; ++tc){
		scanf("%d",&n);
		maks = 0;
		for (int i = 0; i < n; ++i){
			scanf("%d",&a[i]);
			maks = max(a[i], maks);
		}
		ans = maks;
		for (int x = 1; x <= maks; ++x){
			// x pancakes per person
			tmp = x;
			for (int i = 0; i < n; ++i){
				int z = a[i]/x;
				if (a[i] % x > 0) z++;
				tmp += z - 1;
			}
			ans = min(ans, tmp);
		}
		printf("Case #%d: %d\n",tc, ans);
	}
}