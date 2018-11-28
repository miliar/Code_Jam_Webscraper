#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int T,N,M;
int m[100][100];
bool nf[100][100];

int find(int x)
{
	int p = 0;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++) p+=(m[i][j]==x);
	return p;
}

int main()
{
	scanf("%d",&T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d%d",&N,&M);
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++) scanf("%d",&m[i][j]);
		}
		bool ha = true;
		for (int c = 0; c <= 100; c++)
		{
			if (find(c)==0) continue;
			memset(nf,0,sizeof(nf));
			for (int i = 0; i < N; i++)
			{
				bool fl = true;
				for (int j = 0; j < M; j++) if (m[i][j]!=c) fl=false;
				if (fl) for (int j = 0; j < M; j++) nf[i][j]=true;
			}
			for (int i = 0; i < M; i++)
			{
				bool fl = true;
				for (int j = 0; j < N; j++) if (m[j][i]!=c) fl=false;
				if (fl) for (int j = 0; j < N; j++) nf[j][i]=true;
			}
			for (int i = 0; i < N; i++)
			{
				for (int j = 0; j < M; j++) if(nf[i][j]) m[i][j]=c+1;
			}
			if (find(c)!=0)
			{ha = false; break;}
		}
		printf("Case #%d: %s\n",t,ha?"YES":"NO");
	}
}