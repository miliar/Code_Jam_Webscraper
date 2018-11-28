#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>

int cases, index_cases,i,j,k,value,answer;
int layout[3][4][4], row[2];
int possible[16],  n;

void main()
{

freopen("A-small-attempt1.in" , "rt" , stdin ) ;
freopen("A-small-attempt1.out" , "wt" , stdout ) ;

cases = 0;
//read the number of test cases 
scanf("%d",&cases);
//printf("Cases = %d\n",cases);

//Loop through all the cases
for (index_cases=0 ; index_cases<cases; index_cases++)
{
	memset(&possible,0, sizeof(possible));
	for (i=0;i<2;i++)
	{
		scanf("%d",&row[i]);
		for(j=0;j <4;j++)
		{
			for (k=0;k<4;k++)
			{
				scanf("%d",&layout[i][j][k]);
			}
		}
	}
	for (k=0;k<4;k++)
	{
		possible[layout[0][row[0]-1][k]-1]=1;
	//	printf("%d,
	}
	for (n=0,k=0;k<4;k++)
	{
		if(possible[layout[1][row[1]-1][k]-1]==1)
		{
			n++;
			value = layout[1][row[1]-1][k];
		}
	}
	printf("Case #%d: ",index_cases+1);
	if (n==0)
		printf("Volunteer cheated!\n");
	else if (n==1)
		printf("%d\n",value);
	else printf("Bad magician!\n");
}
fclose(stdin) ;
fclose(stdout) ;

}