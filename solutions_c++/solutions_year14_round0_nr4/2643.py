#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
	int T,n,scorenaomi,scoreken;
	double a[1010],b[1010];
	scanf("%d",&T);
	for(int t=1;t<=T;++t) {
		scanf("%d",&n);
		for(int i=0;i<n;++i)
			scanf("%lf",&a[i]);
		for(int i=0;i<n;++i)
			scanf("%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		printf("Case #%d: ",t);
		scoreken=scorenaomi=0;
		for(int i=0,j=0;;++scorenaomi,++i,++j) {
			while(a[i]<b[j] && i<n) ++i;
			if(i==n) {
				printf("%d ",scorenaomi);
				break;
			}
		}
		for(int i=0,j=0;;++scoreken,++i,++j) {
			while(b[j]<a[i] && j<n) ++j;
			if(j==n) {
				printf("%d\n",n-scoreken);
				break;
			}
		}
	}
	return 0;
}
