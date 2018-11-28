#include<cstdio>
int N,M;
char board[110][110];
int dx[255];
int dy[255];
int solve()
{
	scanf("%d%d",&N,&M);
	for(int i=0;i<N;i++) scanf("%s",board[i]);
	int ans=0;
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<M;j++)
		{
			if(board[i][j]=='.') continue;
			int ii=i;
			int jj=j;
			bool avail=false;
		//	int cnt=0;
			while(true)
			{
				ii+=dx[board[i][j]];
				jj+=dy[board[i][j]];
				if(!(0<=ii && ii<N &&0<=jj && jj<M))
					break;
				if(board[ii][jj]!='.')
				{
					avail=true;
					break;
				}
			}
			if(avail) continue;
			ans++;
			avail=false;
			for(int k=0;k<4;k++)
			{
				ii=i; jj=j;
				while(true)
				{
					ii+=dx[k];
					jj+=dy[k];
					if(!(0<=ii && ii<N &&0<=jj && jj<M))
						break;
					if(board[ii][jj]!='.')
					{
						avail=true;
						break;
					}
				}
				if(avail) break;
			}
			if(!avail) return -1;
		}
	}
	return ans;
}
int main()
{
	dx[0]=1;
	dx[1]=-1;
	dy[2]=-1;
	dy[3]=1;
	dx['v']=1;
	dx['^']=-1;
	dy['<']=-1;
	dy['>']=1;
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int v=solve();
		if(v==-1) printf("Case #%d: IMPOSSIBLE\n",i);
		else printf("Case #%d: %d\n",i,v);
	}
	return 0;
}