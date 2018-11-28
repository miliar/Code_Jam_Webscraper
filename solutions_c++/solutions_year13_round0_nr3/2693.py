#include<cstdio>
#include<cmath>
#include<cstring>

#define num int
#define format d
#define N 1001

bool tab[N];
num a,b;
int t;
bool isHui(num a);
void btab()
{
	tab[0]=false;
	int i;
	for(i=1;i<=N;i++)if(isHui(i))tab[i]=true;else tab[i]=false;
}

bool isHui(num a)
{
	char str[50];
	sprintf(str,"%d",a);
	int len=strlen(str);
	int i;
	for(i=0;i<len/2;i++)
		if(str[i]!=str[len-1-i])return false;
	return true;
}

num cnt(num a,num b)
{
	num ret=0;
	num i;
	for(i=a;i<=b;i++)if(tab[i]&&tab[i*i])ret++;
	return ret;
}

int main()
{
//	FILE* fin=freopen("1.in","r",stdin);
	btab();
	scanf("%d",&t);
	int cas;
	for(cas=1;cas<=t;cas++)
	{
		scanf("%d %d",&a,&b);
		num be=(num)(sqrt(a)+0.5f);
		num end=(num)(sqrt(b)+0.5f);
		if(be*be<a)be++;
		if(end*end>b)end--;
		num ret=cnt(be,end);
		printf("Case #%d: %d\n",cas,ret);
	}
	return 0;
}
