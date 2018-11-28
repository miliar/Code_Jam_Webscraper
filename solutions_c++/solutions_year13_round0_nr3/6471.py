#include<stdio.h>
#include<iostream>
#include<math.h>

using namespace std;

int ans[1001];

int p(int tem)
{
	int i,dig[10],ji=0;
	while(0 != tem)
	{
		dig[ji++]=tem%10;
		tem/=10;
	}
	for(i=0;i<ji;i++)
		if(dig[i] != dig[ji-1-i])
			return 0;
	return 1;
}

int check(int tem)
{
	int f=sqrt((double)tem)+0.5;
	if(f*f != tem)
		return 0;
	if(1 == p(tem) && 1 == p(f))
		return 1;
	return 0;
}

void init()
{
	int i;
	for(i=1;i<=1000;i++)
		ans[i]=check(i);
}

int main()
{
	int f,a,b,sum;
	int i,cas;
//	freopen("D:\\C-small-attempt1.in","r",stdin);
//	freopen("D:\\in.txt","w",stdout);
	init();
	scanf("%d",&cas);
	for(i=0;i<cas;i++)
	{
		scanf("%d%d",&a,&b);
		sum=0;
		for(f=a;f<=b;f++)
			sum+=ans[f];
		printf("Case #%d: %d\n",i+1,sum);
	}
	return 0;
}