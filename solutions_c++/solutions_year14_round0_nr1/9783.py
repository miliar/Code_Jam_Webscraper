#include <cstdio>
using namespace std;

int main()
{	
	int i,j,ii,jj,m=0,mi=0,e=0;
	int fc,lc;
	int fg[15][15],lg[15][15];
	
	for(scanf ("%d", &m); mi < m ; mi++)
	{
		e=0;
		scanf ("%d",&fc);
		for(i=0;i<=3;i++)
		{
			scanf ("%d %d %d %d",&fg[i][0],&fg[i][1],&fg[i][2],&fg[i][3]);
		}
		scanf ("%d",&lc);
		for(i=0;i<=3;i++)
		{
			scanf ("%d %d %d %d",&lg[i][0],&lg[i][1],&lg[i][2],&lg[i][3]);
		}
		fc--;lc--;
		for(i=0;i<=3;i++)
		{
			for(j=0;j<=3;j++)
			{
				if( lg[lc][i] == fg[fc][j] )
				{	
					e++;
					ii=fc;jj=j;	
				}
			}
		}
		if(e == 1)printf ("Case #%d: %d\n",mi+1,fg[ii][jj]);
		else if( e == 0)printf ("Case #%d: Volunteer cheated!\n",mi+1);
		else printf ("Case #%d: Bad magician!\n",mi+1);
	}
    return 0;
}