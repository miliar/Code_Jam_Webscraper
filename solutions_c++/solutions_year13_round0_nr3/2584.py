#include <stdio.h>
#include <math.h>
#include <string.h>

int is_sqr(int n)
{
	int r=(int)sqrt(n+0.5);
	return r*r==n;
}

void inttobig(int n,int *d)
{
	int i=0;
	for(;!i || n;d[++i]=n%10,n/=10);
	d[0]=i;
}

bool isp(int x)
{
	int d[10];
	inttobig(x,d);
	for(int i=1;i<=d[0];i++)if(d[i]!=d[d[0]+1-i])return false;
	return true;
}

bool check(int x)
{
	if(!is_sqr(x))return false;
	int r=(int)sqrt(x+0.5);
	if(!isp(r))return false;
	return isp(x);
}

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int T,TC=0;
	scanf("%d",&T);
	while(++TC<=T)
	{
		printf("Case #%d: ",TC);
		int a,b;
		scanf("%d %d",&a,&b);
		int c=0;
		for(int i=a;i<=b;i++)
		{
			if(check(i))c++;
		}
		printf("%d\n",c);
	}
	return 0;
}