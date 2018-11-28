#include<cstdio>
#define N 4

int r[2][N*N];
int ch[2];
int main()
{
	int t;scanf("%d",&t);
	for(int i=1;i<=t;++i)
	{
		printf("Case #%d: ",i);
		for(int j=0;j<2;++j)
		{
			scanf("%d",ch+j);--ch[j];
			for(int a=0;a<N;++a)
				for(int b=0;b<N;++b)
				{
					int v;scanf("%d",&v);--v;
					r[j][v] = a;
				}
		}
		int cnt=0, v;
		for(int j=0;j<N*N;++j)
		{
			if(r[0][j] == ch[0] && r[1][j] == ch[1])
			{
				++cnt;
				v = j;
			}
		}
		if(cnt == 0)
			printf("Volunteer cheated!");
		else if(cnt == 1)
			printf("%d", v+1);
		else
			printf("Bad magician!");
		puts("");
	}
	return 0;
}
