#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
int t,X,a[2000000],n;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for (int test=1;t;t--,test++) {
		printf("Case #%d: ",test);
		scanf("%d%d",&n,&X);
		for (int i=1;i<=n;i++) scanf("%d",&a[i]);
		sort(a+1,a+n+1);
		int ans=0;
		for (int i=n,j=1;i>=j;i--) {
			if (a[i]+a[j]<=X && i>j) {
				ans++,j++;
			}
			else {
				ans++;
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}
