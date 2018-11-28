#include <iostream>

using namespace std;

const int INF = 0x3f3f3f3f;
const int MAXN = 17;

int T;
int R,C,N;
int CNT;

int Vis[MAXN][MAXN];
int Mark[MAXN][MAXN];

int Go[][2] = {-1,0,1,0,0,-1,0,1};

int GetIt(int i,int j)
{
	int ans = 0;
	for(int k=0;k<4;k++)
	{
		int dx = Go[k][0]+i;
		int dy = Go[k][1]+j;

		if(dx<0 || dx>=R || dy<0 || dy>=C)
			continue;

		if(Vis[dx][dy] == 0)
			continue;

		if(Mark[dx][dy] == 1)
			continue;

		ans++;
	}
	return ans;
}

int GetScore()/////////////////////////
{
	memset(Mark,0,sizeof(Mark));

	int s = 0;
	for(int i=0;i<R;i++)
		for(int j=0;j<C;j++)
		{
			if(Vis[i][j] == 0)
				continue;


			Mark[i][j] = 1;

			s += GetIt(i,j);
		}

	return s;
}

void DFS(int n,int cur)///////////////////////
{
	if(n == N)
	{
		CNT = min(CNT,GetScore());
		return;
	}

	

	for(int pos=cur;pos<R*C;pos++)
	{
		int dx = pos/C;
		int dy = pos%C;

		Vis[dx][dy] = 1;

		DFS(n+1,pos+1);

		Vis[dx][dy] = 0;

	}
		
}


int main()//////////////////
{
	freopen("..\\B-small-attempt0.in","r",stdin);
	freopen("..\\B-small-attempt0.out","w",stdout);
	
	cin >> T;

	for(int id =1;id<=T;id++)
	{
		CNT = INF;

		cin >> R >> C >> N;

		DFS(0,0);

		printf("Case #%d: %d\n",id,CNT);
		fprintf(stderr,"Case #%d: %d\n",id,CNT);
	}
	return 0;
}