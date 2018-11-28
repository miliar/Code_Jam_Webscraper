#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int N,X,a[10005];

void init()
{
	scanf("%d%d",&N,&X);
	for (int i=1; i<=N; i++) scanf("%d",&a[i]);
}

void doit()
{
	sort(a+1,a+N+1);
	int s=0;
	for (int i=1,j=N; i<=j;)
	{
		if (i==j) {s++; break;}
		if (a[i]+a[j]<=X) s++,i++,j--;
		else s++,j--;
	}
	printf("%d\n",s);
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=1; i<=T; i++)
	{
		init();
		printf("Case #%d: ",i);
		doit();
	}
	return 0;
}

