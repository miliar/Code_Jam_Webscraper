#include<cstdio>
#include<map>
#include<cstring>
#include<iostream>
using namespace std;
map<long long,long long> M;
map<long long,long long> ::iterator in,in1;
char buf[100];
long long a,b,c,d,e,n;
bool pal(long long x)
{
sprintf(buf,"%lld",x);
a=strlen(buf);
a--;
b=0;
while(a>b)
	{
	if(buf[a]!=buf[b])return 0;
	a--;
	b++;
	}
return 1;
}

main()
{
M[0]=0;
M[1]=1;
for(long long i=2;i<=10000000;i++)
	{
	if(pal(i)&&pal(i*i))M[i*i]=1;	
	}
scanf("%lld",&n);
for(int u=1;u<=n;u++)	
	{
	scanf("%lld%lld",&a,&b);
	c=0;
	for(in=M.begin();in!=M.end();in++)
		{
	//	cout<<in->first<<" "<<in->second<<endl;
		if(in->first>=a&&in->first<=b)c++;
		}
	printf("Case #%d: %lld\n",u,c);
	}






}
