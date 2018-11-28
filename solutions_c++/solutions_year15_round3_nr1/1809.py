#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
	int t,n=1;
	scanf("%d",&t);
	while(t--)
	{
		int ans,r,c,w,d;
		cin>>r>>c>>w;
		ans=c/w;
		ans+=w;
		d=c%w;
		if(w==2 || d==0)
		ans--;
		printf("Case #%d: %d\n",n,ans);
		n++;
	}
}