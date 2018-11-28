#include <stdio.h>
#include <string.h>
#include <stdlib.h>


#include <iostream>
#include <algorithm>

using namespace std;


int main()
{
	int t,a;
	scanf("%d",&t);

	


	int i,j;
	int possiveis,carta;
	int x[5][5],y[5][5];
	int resp1,resp2;

	for(a=1;a<=t;a++)
	{
		possiveis = 0; 
		carta = 0;

		scanf("%d",&resp1);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				scanf("%d ",&x[i][j]);
			

		scanf("%d",&resp2);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				scanf("%d ",&y[i][j]);



		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				if(y[resp2][j] == x[resp1][i]){	possiveis++; carta = y[resp2][j];}
				
	
		/*for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
				printf("%d ",x[i][j]);
			cout << endl;
		}
			
		cout << endl;
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
				printf("%d ",y[i][j]);
			cout << endl;
		}
		cout << endl;*/

		//printf("possiveis %d carta %d\n",possiveis,carta);

		printf("Case #%d: ",a);
		if(!possiveis)	printf("Volunteer cheated!\n");
		else			
			if(possiveis == 1)	printf("%d\n",carta);
			else				printf("Bad magician!\n");

	}



	return 0;
}
