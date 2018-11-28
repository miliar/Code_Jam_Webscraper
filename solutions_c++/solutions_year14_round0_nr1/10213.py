#include<stdio.h>

int main()
{
	int i, j, k, l;
	int n;
	int ans;
	int result[100];
	int count=0;
	int tempAns[4];
	int arr[4][4];
	FILE *f = fopen("A-small-attempt1.in", "r");
	fscanf(f, "%d\n", &n);

	for(i=0; i<n; i++)
	{
		for(l=0; l<2; l++)
		{
			fscanf(f, "%d\n", &ans);
			ans--;
			for(j=0; j<4; j++)
			{
				for(k=0; k<4; k++)
					fscanf(f, "%d ", &arr[j][k]);
				fscanf(f, "\n");
			}

			if(l==0)
			{
				for(j=0; j<4; j++)
					tempAns[j] = arr[ans][j];
			}
			else
			{
				int answer;
				count = 0;
				for(j=0; j<4; j++)
				{
					for(k=0; k<4; k++)
						if(tempAns[j] == arr[ans][k])
						{
							answer = tempAns[j];
							count++;
						}
				}
				if(count==1)
					result[i] = answer;
				else if(count==0)
					result[i] = -1;
				else
					result[i] = -2;
			}
		}
	}

	fclose(f);
	f = fopen("output.out", "w");

	for(i=0; i<n; i++)
	{
		fprintf(f,"Case #%d: ", i+1);
		if(result[i] == -1)
			fprintf(f,"Volunteer cheated!\n");
		else if(result[i] == -2)
			fprintf(f,"Bad magician!\n");
		else
			fprintf(f,"%d\n", result[i]);
	}	
	fclose(f);
	getchar();
	return 0;
}