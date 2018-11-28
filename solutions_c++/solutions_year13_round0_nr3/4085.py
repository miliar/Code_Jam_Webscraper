#include<iostream>
#include<cstdio>
using namespace std;
#define ll long long
ll que[100];
bool IsHuiWen(ll i)
{
  	ll oldi,newi;
	oldi = i;
	for(newi=0;oldi;)
 	{
    	newi=newi*10+oldi%10;
     	oldi=oldi/10;
	}
  	return (i == newi);
}
int main()
{
	freopen("C-large-1.in","r",stdin);
	freopen("o.txt","w",stdout);
	int top=0,t,cas=0;
	for(ll i=1;i<=10000000;i++)
		if(IsHuiWen(i) && IsHuiWen(i*i))
    		que[top++]=i*i;
	scanf("%d",&t);
	ll a,b;
	while(t--)
	{
		scanf("%lld %lld",&a,&b);
		int l,h;
		for(l=0;l<top;l++)
			if(a<=que[l])
				break;
		for(h=0;h<top;h++)
			if(b<que[h])
				break;
		printf("Case #%d: %d\n",++cas,h-l);
	}
	return 0;
}

