#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE * fp;
	fp = fopen("A-small-attempt1.in","r");
	FILE * fp2;
	fp2 = fopen("output.txt","w");

	int N,n,audience[10];
	int person = 0;
	int add = 0;

	fscanf(fp,"%d",&N);

	for(int i=0;i<N;i++)
	{
		fscanf(fp,"%d",&n);

		for(int j=0;j<n+1;j++)
			fscanf(fp,"%1d",&audience[j]);

		person = audience[0];

		for(int k=1;k<=n;k++)
		{
			if(audience[k] != 0)
			{	if(person < k)
				{
					add += k-person;
					person += (add+audience[k]);
				}
				else
					person += audience[k];
			}
		}

		fprintf(fp2,"Case #%d: %d\n",i+1,add);

		person=0;
		add=0;	
	}

	fclose(fp);
	fclose(fp2);

	return 0;
}
		

