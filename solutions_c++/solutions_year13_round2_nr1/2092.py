#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
#define s second
#define f first
long long t[1000004];
long long wyn,roz,n,z,a,b,c,d;
pair<long long,long long> x,y;
pair<long long,long long> zrownaj(long long z,long long to)//zwraca ile zmian,wielkosc
{
if(z==1)return make_pair(1000000000,1);
int zm=0;
while(z<=to)
	{
	zm++;
	z+=z-1;
	}
return make_pair(zm,z);
}
main()
{
scanf("%lld",&z);
for(int xx=1;xx<=z;xx++)
	{
	scanf("%lld%lld",&roz,&n);
	for(int i=0;i<n;i++)
		{
		scanf("%lld",&t[i]);
		}
	sort(t,t+n);
	wyn=0;
	for(long long i=0;i<n;i++)
		{
		x=zrownaj(roz,t[i]);
		if(x.f<n-i)
			{
			roz=x.s;
			wyn+=x.f;
			roz+=t[i];
			}
		else 
			{
			wyn+=n-i;
			break;
			}
		}
	printf("Case #%d: %lld\n",xx,wyn);
	}
}
