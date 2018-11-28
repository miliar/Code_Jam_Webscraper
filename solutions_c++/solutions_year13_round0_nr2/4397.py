#include <stdio.h>
int N,M;
int H[15][15];
int C[15][15];
void check(int sy,int sx,int dy,int dx)
{
	int uni=0;
	for (int y=sy,x=sx;y>=0 && y<N && x>=0 && x<M;y+=dy,x+=dx)
		uni |= (1<<H[y][x]);
	if (uni!=2) return;	
	for (int y=sy,x=sx;y>=0 && y<N && x>=0 && x<M;y+=dy,x+=dx)
		C[y][x]=1;
}
int main()
{
	int T;
	scanf("%d",&T);
	for (int kase=1;kase<=T;++kase)
	{
		scanf("%d %d",&N,&M);		
		for (int q=0;q<N;++q) for (int w=0;w<M;++w)
		{
			scanf("%d",&H[q][w]);
			C[q][w] = 0;
		}
		for (int q=0;q<N;++q) check(q,0,0,1);
		for (int q=0;q<M;++q) check(0,q,1,0);
		int err=0;
		for (int q=0;q<N;++q) for (int w=0;w<M;++w)
			if (H[q][w]==1 && C[q][w]==0)
				err=1;
		printf("Case #%d: %s\n",kase,err?"NO":"YES");
	}
	return 0;
}
