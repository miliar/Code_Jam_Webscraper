#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <ctime>
#include <stdint.h>

using namespace std;

int a[1010];

void Solve()
{
	int n;
	scanf("%d", &n);
	for(int i = 0; i<n; ++i){
		scanf("%d", &a[i]);
	}
	int l = 0, r = n-1;
	int ans = 0;
	for(int t = 0; t<n; ++t){
		int now = l;
		for(int i = l; i<=r; ++i){
			if(a[i] < a[now]){
				now = i;
			}
		}
//		printf("\n%d %d %d", l, r, now);
		int tmp = a[now];
		if(now-l < r-now){
			ans += now-l;
			for(int i = now; i>l; --i){
				a[i] = a[i-1];
			}
			a[l] = tmp;
			l++;
		}else{
			ans += r-now;
			for(int i = now; i<r; ++i){
				a[i] = a[i+1];
			}
			a[r] = tmp;
			r--;
		}
	}
	printf("%d\n", ans);
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int nCase;
	scanf("%d", &nCase);
	for(int i = 1; i<=nCase; ++i){
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}

