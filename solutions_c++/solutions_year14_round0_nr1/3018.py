#include<stdio.h>

int main()
{
	int T;
	FILE *in = fopen("A-small-attempt0.in","r");
	FILE *out = fopen("output.txt","w");
	fscanf(in,"%d",&T);
	for(int testcase = 0; testcase < T; testcase++)
	{
		int first, second, garbage;
		int first_a[4], second_a[4];
		fscanf(in,"%d",&first);
		for(int i = 1; i <= 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				if(i == first) fscanf(in,"%d",&first_a[j]);
				else fscanf(in,"%d",&garbage);
			}
		}
		fscanf(in,"%d",&second);
		for(int i = 1; i <= 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				if(i == second) fscanf(in,"%d",&second_a[j]);
				else fscanf(in,"%d",&garbage);
			}
		}

		int pt = 0;
		int answer[4];
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				if(first_a[i] == second_a[j]){
					answer[pt++] = first_a[i];
					break;
				}
			}
		}

		fprintf(out,"Case #%d: ",testcase + 1);
		if(pt == 0) fprintf(out,"Volunteer cheated!\n");
		else if(pt > 1) fprintf(out,"Bad magician!\n");
		else fprintf(out,"%d\n",answer[0]);
	}
	return 0;
}