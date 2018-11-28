#include<iostream>
#include<string.h>
using namespace std;

bool num[1100];

bool palind(int n)
{
	int m=0;;
	int tem=n;
	while (tem)
	{
		m=m*10+tem%10;
		tem=tem/10;
	}
	return (m==n);
}


void initer()
{
	int n=1000;
	int i;
	memset(num,false,sizeof(num));
	for (i=0;i<=32;i++)
	{
		if (palind(i)&&(i*i<=1000)&&palind(i*i)) num[i*i]=true;
	}
}

int main()
{
	int t,a,b,i,j,x;
	freopen("a.txt","r",stdin);
	freopen("b.txt","w",stdout);
	initer();
	scanf("%d",&t);
	for (i=0;i<t;i++)
	{
		scanf("%d %d",&a,&b);
		x=0;
		for (j=a;j<=b;j++) if (num[j]) x++;
		printf("Case #%d: %d\n",i+1,x);
	}
	return 0;
}