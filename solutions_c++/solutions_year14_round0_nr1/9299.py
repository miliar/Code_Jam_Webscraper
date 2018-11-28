#include <stdio.h>
#include <iostream>
#include <fstream>
using namespace std; 

int main ()
{
	ofstream output;
	output.open ("output.txt"); 

	int i=0, j=0, k=0;
	int t=0, a1=0, a2=0, cont=0, aux=0;
	int g1[4][4];
	int g2[4][4];

	scanf ("%d", &t); 

	for (i=0; i<t; i++)
	{
		scanf("%d", &a1);
		for (j=0; j<4; j++)
		{
			for (k=0; k<4; k++)
			{
				scanf("%d", &g1[j][k]);
			}
		}
		scanf("%d", &a2);
		for (j=0; j<4; j++)
		{
			for (k=0; k<4; k++)
			{
				scanf("%d", &g2[j][k]);
			}
		}

		for (j=0; j<4; j++)
		{
			for (k=0; k<4; k++)
			{
				if (g1[a1-1][j] == g2[a2-1][k])
				{
					cont = cont+1; 
					aux = g1[a1-1][j];
				}
			}
		}

		if (cont == 1)
		{
			//printf("Case #%d: %d\n", (i+1),aux);
			output <<"Case #"<<(i+1)<<": "<<aux<<"\n";
		}
		else if (cont == 0)
		{
			//printf("Case #%d: Volunteer cheated!\n", (i+1));
			output <<"Case #"<<(i+1)<<": Volunteer cheated!\n";
		}
		else if (cont > 1)
		{
			//printf("Case #%d: Bad magician!\n", (i+1));
			output <<"Case #"<<(i+1)<<": Bad magician!\n";
		}

		cont=0; aux=0;
		j=0; k=0;
	}

	output.close();
	return 0;
}