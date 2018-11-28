#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
	int k,t,n,x,a[20000],i,j,disk;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		scanf("%d %d",&n,&x);
		for(i=1;i<=n;i++) scanf("%d",&a[i]);
		sort(a+1,a+n+1);
		disk=0;
		i=1;
		for(j=n;j>i;j--)
		{
			if((a[i]+a[j])<=x) {i++;disk++;}
			else disk++;
		}
		if(j==i) disk++;
		printf("Case #%d: %d\n",k,disk);
	}
}
