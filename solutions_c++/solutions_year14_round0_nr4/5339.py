#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t,n,i,x,d,w;
	scanf("%d",&t);
	for(x=1;x<=t;x++){
		scanf("%d",&n);
		d=w=0;
		float naomi[n],ken[n];
		for(i=0;i<n;i++)scanf("%f",&naomi[i]);
		for(i=0;i<n;i++)scanf("%f",&ken[i]);
		sort(naomi,naomi+n);
		sort(ken,ken+n);
		int j=0,k=n-1,l=0;
		for(i=n-1;i>=0;i--)
		{
				if(naomi[i]>ken[k])w++;
				else k--;
		}
		k=n-1;
		for(i=0;i<n;i++)
		{
			if(naomi[i]<ken[j])k--;
			else{
				j++;d++;
			}
		}
		printf("Case #%d: %d %d\n",x,d,w);
	}
}
