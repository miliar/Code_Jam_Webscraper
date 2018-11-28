#include <bits/stdc++.h>
using namespace std;

int N;
bool a[10];

void init()
{
	scanf("%d",&N);
}

void doit()
{
	memset(a,0,sizeof(a));
	if (!N) {puts("INSOMNIA"); return;}
	for (int i=N; ; i+=N)
	{
		for (int j=i; j; j/=10) a[j%10]=1;
		bool ok=1;
		for (int j=0; j<=9; j++) if (!a[j]) ok=0;
		if (ok)
		{
			printf("%d\n",i);
			break;
		}
	}
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
