#include<stdio.h>
#include<algorithm>
using namespace std;
int k[1000],t,i,j,a,b,m;
int f(int n)
{
	if(n>=m)return n;
	int i,j,qwer=99999999;
	for(i=m;i;i--)
	{
		if(k[i])break;
	}
	for(j=2;j<=i/2;j++)
	{
		k[i]--;
		k[i-j]++;
		k[j]++;
		qwer=min(qwer,f(n+1));
		k[i-j]--;
		k[j]--;
		k[i]++;
	}
	return min(n+i,qwer);
}

int main()
{
	freopen("inputqwertyui.txt","r",stdin);
	freopen("outputqwertyui.txt","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		for(j=0;j<=m;j++)k[j]=0;
		m=0;
		scanf("%d",&a);
		for(j=0;j<a;j++)
		{
			scanf("%d",&b);
			k[b]++;
			m=b>m?b:m;
		}
		printf("Case #%d: %d\n",i,f(0));
	}
}
