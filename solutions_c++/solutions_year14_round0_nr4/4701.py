#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("question.txt","r",stdin);
	freopen("ans.txt","w",stdout);
	int i,t,n,c,d,x=1;
	scanf("%d",&t);
	while(t--) {
		c=0;d=0;
		scanf("%d",&n);
		double a[n],b[n];
		for(i=0;i<n;i++) scanf("%lf",&a[i]);
		for(i=0;i<n;i++) scanf("%lf",&b[i]);
		int f=0;
		sort(a,a+n);
		sort(b,b+n);
		for(i=0;i<n;i++) {
			if(a[i]>b[f]) {
				c++;
				f++;
			}
		}
		f=n-1;
		for(i=n-1;i>=0;i--) {
			if(a[i]>b[f]) d++;
			else f--;
		}
		printf("Case #%d: %d %d\n",x++,c,d);
	}
	fclose(stdout);
}
