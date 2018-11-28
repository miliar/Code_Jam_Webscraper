#include<stdio.h>
#include<string>
#include<math.h>
#include<errno.h>
#include<ctype.h>
#include<limits>
#include<stdlib.h>
#include<valarray>
#include<conio.h>
#include<iterator>
#include<numeric>
#include<iomanip>
#include<set>
#include<iostream>
#include<algorithm>
#include<vector>
#include<conio.h>
using namespace std;

int a1[4][4],a2[4][4],row1[4],row2[4],mat[4];
int t,c=1,ans1,ans2,i,j,temp,match;
char bad[20] = "Bad magician!";
char cheat[20] = "Volunteer cheated!";

int main(int argc,char* argv[])
{
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&ans1);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(i!=(ans1-1))
					scanf("%d",&a1[i][j]);
				else
					scanf("%d",&row1[j]);
			}
		}
		scanf("%d",&ans2);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(i!=(ans2-1))
					scanf("%d",&a2[i][j]);
				else
					scanf("%d",&row2[j]);
			}
		}
		match=0;
		for(i=0;i<4;i++)
		{
			temp = row1[i];
			for(j=0;j<4;j++)
			{
				if(temp==row2[j])
				{
					mat[match]=temp;
					match++;
				}
			}
		}
		if(match==1)
			printf("Case #%d: %d\n",c,mat[0]);
		else if(match==0)
			printf("Case #%d: %s\n",c,cheat);
		else
			printf("Case #%d: %s\n",c,bad);
		c++;
	}
	//getch();
	return 0;
}	