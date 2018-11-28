#include <map>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;
#define maxn 10010

int n,s[maxn],x,vis[maxn];

void work() {
	scanf("%d%d",&n,&x);
	for (int i=0; i<n; i++ ) scanf("%d",&s[i]);
	sort(s,s+n);
	int ans = n;
	for (int i=0, j=n-1; i<n; i++ ) {
		while (j>i && s[i]+s[j]>x) j--;
		if (j>i) {
			ans--;
			j--;
		}
	}
	printf("%d\n",ans);
}

int main() {
	int cas;
	freopen("test.txt","r",stdin);
	freopen("ans.txt","w",stdout);
	scanf("%d",&cas);
	for (int i=1; i<=cas; i++ ) {
		printf("Case #%d: ",i);
		work();
	}
	return 0;
}
