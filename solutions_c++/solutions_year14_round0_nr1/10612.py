#include <cstdio>
#include <cstring>
int T,N;
int d[10][10],s[120];
int dee[10],deg;

int main()
{
	freopen("at.out","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		memset(d,0,sizeof(d));
		memset(s,0,sizeof(s));
		memset(dee,0,sizeof(dee));
		scanf("%d",&N);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&d[i][j]);
		for(int i=0;i<4;i++)
			s[d[N-1][i]]++;
		scanf("%d",&N);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&d[i][j]);
		for(int j=0;j<4;j++)
		{
			if(s[d[N-1][j]])
			{
				dee[N-1]++;
				deg=d[N-1][j];
			}
		}
		printf("Case #%d: ",t);
		if(dee[N-1] == 1)
			printf("%d\n",deg);
		else if(dee[N-1] == 0)
			printf("Volunteer cheated!\n");
		else if(dee[N-1] > 1)
			printf("Bad magician!\n");
	}

	return 0;
}
