#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

#define FOR(i,l,h) for(int i=(l);i<=(h);++i)

bool b[10];
int count;

void take_apart(int n)
{
	while (n)
	{
		int d=n%10;
		if (!b[d]) count++;
		b[d]=true;
		n/=10;
	}
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	int T;
	scanf("%d",&T);
	FOR(Tcase,1,T)
	{
		printf("Case #%d: ",Tcase);
		int n;
		scanf("%d",&n);
		if (n==0)
		{
			printf("INSOMNIA\n");
			continue;
		}
		memset(b,0,sizeof(b));
		count=0;
		int i=1;
		for(;count<10;i++)
			take_apart(i*n);
		printf("%d\n",(i-1)*n);
	}
	return 0;
}

