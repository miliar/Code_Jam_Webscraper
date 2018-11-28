#include <bits/stdc++.h>
using namespace std;

int N,M,F[256];
bool b[4][105][105];
char a[105][105];

void init()
{
	scanf("%d%d",&N,&M);
	F['<']=0,F['>']=1,F['^']=2,F['v']=3;
	for (int i=1; i<=N; i++) scanf("%s",a[i]+1);
}

void doit()
{
	memset(b,0,sizeof(b));
	for (int i=1; i<=N; i++)
	{
		for (int j=1; j<=M; j++) if (a[i][j]!='.') {b[0][i][j]=1; break;}
		for (int j=M; j; j--) if (a[i][j]!='.') {b[1][i][j]=1; break;}
	}
	for (int i=1; i<=M; i++)
	{
		for (int j=1; j<=N; j++) if (a[j][i]!='.') {b[2][j][i]=1; break;}
		for (int j=N; j; j--) if (a[j][i]!='.') {b[3][j][i]=1; break;}
	}
	int ans=0;
	for (int i=1; i<=N; i++)
		for (int j=1,ok; j<=M; j++) if (b[F[a[i][j]]][i][j])
		{
			ans++,ok=0;
			for (int k=0; k<4; k++) if (!b[k][i][j]) ok=1;
			if (!ok) {puts("IMPOSSIBLE"); return;}
		}
	cout<<ans<<endl;
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
