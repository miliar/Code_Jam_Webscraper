#include <iostream>
#include <stdio.h>
using namespace std;


int main() {
	// your code goes here
	int a[4][4],b[4][4],first,second,count,i,j,temp,t,T=1;
	scanf("%d",&t);
	while(T<=t)
	{
		scanf("%d",&first);
		first--;
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		scanf("%d",&a[i][j]);
		scanf("%d",&second);
		second--;
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		scanf("%d",&b[i][j]);
		count=0;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[first][i]==b[second][j]) {temp=a[first][i];count++;}
			}
		}
		if(count==1)
		printf("Case #%d: %d\n",T,temp);
		else if(count==0)
		printf("Case #%d: Volunteer cheated!\n",T);
		else
		printf("Case #%d: Bad magician!\n",T);
		
		T++;
	}
	
	return 0;
}