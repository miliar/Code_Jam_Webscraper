#include<cstdio>
int main()
{
	short int t;
	scanf("%hd",&t);
	short int cnt=0,i,j;
	while(t--)
	{
		cnt++;
		short int r1,r2,a[4][4],b[4][4],match=0,col=0;
		scanf("%hd",&r1);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%hd",&a[i][j]);
		scanf("%hd",&r2);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%hd",&b[i][j]);
		r1--;
		r2--;
		for(i=0;i<4;i++)
		{
			int ans=a[r1][i];
			for(j=0;j<4;j++)
			{
				if(ans==b[r2][j])
				{
					match++;
					col=j;
				}
			}
		}
		if(!match)
			printf("Case #%hd: Volunteer cheated!\n",cnt);
		else if(match>1)
			printf("Case #%hd: Bad magician!\n",cnt);
			else
			printf("Case #%hd: %hd\n",cnt,b[r2][col]);
	}
	return 0;
}
