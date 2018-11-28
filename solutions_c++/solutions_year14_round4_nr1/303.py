#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <string>
#define lld long long
#define INF 2100000000
#define eps 1e-8
#define mem(a,b) memset(a,b,sizeof(a))

using namespace std;
int a[200000];
int main()
{
	int T;
	int n, m, i, j, cas=0;

	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
		cin>>T;
	while(T--){
		scanf("%d%d", &n, &m);
		for(i = 1; i <= n; i++)
			scanf("%d", &a[i]);
		sort(a + 1, a + 1 + n);
		int ans = 0, l = 1, r = n;
		while(l <= r){
			if (l == r){
				ans++;
				break;
			}
			if (a[l] + a[r] <= m){
				l++;
				r--;
				ans++;
			} else {
				r--;
				ans++;
			}
		}
		printf("Case #%d: %d\n", ++cas, ans);
	}
	return 0;
}
