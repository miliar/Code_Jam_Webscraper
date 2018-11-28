#include <iostream>

#include<stdio.h>

using namespace std;


int main() {


int x1,x2,i,j,a1[4][4],a2[4][4],k,temp,t,*s;


scanf("%d",&t);
s=new int[t];

for(int y=0;y<t;y++)
{
	k=0;
	scanf("%d",&x1);

	for(i=0;i<4;i++)

	{	for(j=0;j<4;j++)
			scanf("%d",&a1[i][j]);

	}



	scanf("%d",&x2);

	for(i=0;i<4;i++)

	{

		for(j=0;j<4;j++)
		
			scanf("%d",&a2[i][j]);
	
	}

	for(i=0;i<4;i++)

	{
		
		for(j=0;j<4;j++)

			{
	if(a1[x1-1][i]==a2[x2-1][j])

				{
	k=k+1;
		
					temp=a2[x2-1][j];
	
				}
			
			}

		if(k==2) break;
	
	}

	if(k==1)

		{s[y]=temp;}

	else 

	{
		if(k==0)

		s[y]=0;
		else

		s[y]=-1;
	}
}
for(i=0;i<t;i++)
{
	if(s[i]==0)
		printf("Case #%d: Volunteer cheated!\n",i+1);
	else
	{	if(s[i]==-1)
			printf("Case #%d: Bad magician!\n",i+1);
		else
			printf("Case #%d: %d\n",i+1,s[i]);
	}
}
return 0;

}