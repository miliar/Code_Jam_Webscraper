#include<cstdio>
#include<iostream>
using namespace std;
#define PII pair<int,int>
#define s second
#define f first
PII x;
int t[1000];//MAX to 100
int n,m,z,p;
long long optymalne,normalne;
int poc,kon,il;
long long don(long long a)
{
return a*(a+1)/2;
}
void insert(int a,int b,int ile)
{
for(int i=a;i<=b;i++)t[i]+=ile;
}
PII prz()
{
int w=1;
while(t[w]==0)w++;
int w2=w;
while(t[w2+1]>0)w2++;
return make_pair(w,w2);
}
main()
{
t[102]=1;
scanf("%d",&z);
for(int uu=1;uu<=z;uu++)
	{
	optymalne=normalne=0;
	printf("Case #%d: ",uu);
	scanf("%d%d",&n,&m);
		for(int i=1;i<=m;i++)
		{
		scanf("%d%d%d",&poc,&kon,&il);
		kon--;
		normalne+=(il*(n*1LL*(kon-poc+1)-don(kon-poc)));
		//printf("%d\n",normalne);
		insert(poc,kon,il);
		}
	while(1)
		{
		x=prz();
		if(x.f>n)break;
		optymalne+=(n*1LL*(x.s-x.f+1)-don(x.s-x.f));
		insert(x.f,x.s,-1);
		}
	//printf("%lld %lld\n",normalne,optymalne);
		
	printf("%lld\n",normalne-optymalne);
	}
}


