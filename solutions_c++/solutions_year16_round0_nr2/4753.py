#include <bits/stdc++.h>
using namespace std;

int N;
char a[105];
bool b[105];

void init()
{
	scanf("%s",a+1);
	N=strlen(a+1);
	for (int i=1; i<=N; i++) b[i]=a[i]=='+';
}

void doit()
{
	bool k=0;
	int ans=0;
	for (int i=N; i; i--) if (!(b[i]^k)) ans++,k^=1;
	printf("%d\n",ans);
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
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
