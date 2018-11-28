#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>

int main()
{
int i,t,j,l,count;
int ax[4][5],ao[4][5];
char ch;
freopen("ain.txt","r",stdin);
freopen("aout.txt","w",stdout);
scanf("%d",&t);
for(i=1;i<=t;i++)
{
	count=0;
	for(l=0;l<=3;l++)
	{	
		for(j=0;j<4;j++)
		{ 
			scanf("%c",&ch);
			while((ch=='\n'))
			{
				scanf("%c",&ch);
			}
			if(ch=='T')
			{
					ax[l][j]=1;
					ao[l][j]=1;
			}
			else if(ch=='X')
			{
						ax[l][j]=1;
						ao[l][j]=0;
			}
			else if(ch=='O')
			{
						ax[l][j]=0;
						ao[l][j]=1;
				
			}
			
			else
			{
						ax[l][j]=0;
						ao[l][j]=0;
						count++;
			}
		
		}
	
	}
		
	if((ax[0][0]==1 && ax[0][1]==1 && ax[0][2]==1 && ax[0][3]==1) || (ax[1][0]==1 &&ax[1][1]==1 &&ax[1][2]==1 &&ax[1][3]==1) ||  (ax[2][0]==1 &&ax[2][1]==1 &&ax[2][2]==1 &&ax[2][3]==1) || (ax[3][0]==1 &&ax[3][1]==1 &&ax[3][2]==1 &&ax[3][3]==1))
	{
		printf("Case #%d: X won\n",i);
		continue;
	}
	if((ax[0][0]==1 &&ax[1][0]==1 &&ax[2][0]==1 &&ax[3][0]==1) || (ax[0][1]==1 &&ax[1][1]==1 &&ax[2][1]==1 &&ax[3][1]==1) ||  (ax[0][2]==1 &&ax[1][2]==1 &&ax[2][2]==1 &&ax[3][2]==1) || (ax[0][3]==1 &&ax[1][3]==1 &&ax[2][3]==1 &&ax[3][3]==1))
	{
		printf("Case #%d: X won\n",i);
		continue;
	}
	if((ax[0][0]==1 && ax[1][1]==1 &&ax[2][2]==1 &&ax[3][3]==1) || (ax[0][3]==1 &&ax[1][2]==1 &&ax[2][1]==1 &&ax[3][0]==1))
	{
		printf("Case #%d: X won\n",i);
		continue;
	}
	if((ao[0][0]==1 && ao[0][1]==1 && ao[0][2]==1 && ao[0][3]==1) || (ao[1][0]==1 &&ao[1][1]==1 &&ao[1][2]==1 &&ao[1][3]==1) ||  (ao[2][0]==1 &&ao[2][1]==1 &&ao[2][2]==1 &&ao[2][3]==1) || (ao[3][0]==1 &&ao[3][1]==1 &&ao[3][2]==1 &&ao[3][3]==1))
	{
		printf("Case #%d: O won\n",i);
		continue;
	}
	if((ao[0][0]==1 &&ao[1][0]==1 &&ao[2][0]==1 &&ao[3][0]==1) || (ao[0][1]==1 &&ao[1][1]==1 &&ao[2][1]==1 &&ao[3][1]==1) ||  (ao[0][2]==1 &&ao[1][2]==1 &&ao[2][2]==1 &&ao[3][2]==1) || (ao[0][3]==1 &&ao[1][3]==1 &&ao[2][3]==1 &&ao[3][3]==1))
	{
		printf("Case #%d: O won\n",i);
		continue;
	}
	if((ao[0][0]==1 && ao[1][1]==1 &&ao[2][2]==1 &&ao[3][3]==1) || (ao[0][3]==1 &&ao[1][2]==1 &&ao[2][1]==1 &&ao[3][0]==1))
	{
		printf("Case #%d: O won\n",i);
		continue;
	}
	if(count>1)
	{
		printf("Case #%d: Game has not completed\n",i);
		continue;
	}
	printf("Case #%d: Draw\n",i);
}

return 0;
}