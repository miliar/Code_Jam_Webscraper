#include <stdio.h>
FILE *in = fopen("input.txt","r");
FILE *out = fopen("output.txt","w");
int board[104][104];
int check[104][104];
int xx[104],yy[104];
int ts,tt;
int n,m;
int main()
{
	int i,j,k;
	fscanf(in,"%d",&ts);
	for(tt=1;tt<=ts;tt++)
	{
		fscanf(in,"%d %d",&n,&m);
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				check[i][j]=0;
				fscanf(in,"%d",&board[i][j]);
			}
		}
		int checkk=0,minn;
		int cx,cy,ck=0;
		while(checkk<=n*m)
		{
			minn=999;
			ck=checkk;
			for(i=0;i<n;i++)
			{
				for(j=0;j<m;j++)
				{
					if(check[i][j]==0&&minn>board[i][j])
					{
						minn=board[i][j];
						cx=i;cy=j;
					}
				}
			}
			for(i=0;i<n;i++)
			{
				if(board[i][cy]>minn)
				{break;
				}
			}
			if(i==n)
			{
				for(i=0;i<n;i++)
				{
					if(check[i][cy]==0)
					{
						check[i][cy]=1;
						checkk++;
					}
				}
			}
			for(i=0;i<m;i++)
			{
				if(board[cx][i]>minn)
				{break;
				}
			}
			if(i==m)
			{
				for(i=0;i<m;i++)
				{
					if(check[cx][i]==0)
					{
						check[cx][i]=1;
						checkk++;
					}
				}
			}
			if(checkk==ck)
			{break;
			}
		}
		if(checkk!=m*n)
		{
			fprintf(out,"Case #%d: NO\n",tt);
		}
		else
		{
			fprintf(out,"Case #%d: YES\n",tt);
		}
	}
	return 0;
}