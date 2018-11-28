#include<stdio.h>
#include<stdlib.h>
int t,s[1010],i,j,k,n,q,r,ans;
char p[1010];
int main()
{
	freopen("inputA2.txt","r",stdin);
	freopen("outputA2.txt","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		for(k=0;p[k];k++)p[k]=s[k]=0;
		scanf("%d%s",&j,p);
		for(k=0;p[k];k++)s[k]=p[k]-'0';
		for(q=r=ans=0;q<k;q++)
		{
			if(r<q)ans+=(q-r),r=q;
			r+=s[q];
		}
		printf("Case #%d: %d\n",i,ans);
	}
}
