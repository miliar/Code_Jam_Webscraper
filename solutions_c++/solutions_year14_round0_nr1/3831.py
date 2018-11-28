#include<cstdio>
int main()
{
	short int t;
	scanf("%hd",&t);
	short int c_no=0,i,j;
	while(t--)
	{
		c_no++;
		short int r1,r2,match=0,index=0,a[4][4],b[4][4];
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
		//short int match=0,index=0;
		for(i=0;i<4;i++)
		{
			short int data=a[r1][i];
			for(j=0;j<4;j++)
			{
				if(data==b[r2][j])
				{
					match++;
					index=j;
				}
			}
		}
		if(!match)
			printf("Case #%hd: Volunteer cheated!\n",c_no);
		else if(match>1)
			printf("Case #%hd: Bad magician!\n",c_no);
			else
			printf("Case #%hd: %hd\n",c_no,b[r2][index]);
	}
	return 0;
}
