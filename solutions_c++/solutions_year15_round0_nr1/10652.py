
#include <stdio.h>
#include <stdlib.h>



FILE *fin, *fout;
void algo(int num);


int main()
{

	int n=0;


	fopen_s(&fin,"C:\\Users\\Hyunsik\\Desktop\\A-small-attempt0.in","r");
	fopen_s(&fout,"C:\\Users\\Hyunsik\\Desktop\\output","wt");
	fscanf_s(fin,"%d", &n);

	


	//printf("test case = %d\n", n);

	
	for (int test = 0; test<n; test++)
	{
		algo(test);
	}

	
	fclose(fin);
	fclose(fout);

	return 0;
}

void algo(int num){

	int ans=0;

	int smax = 0 ;
	fscanf_s(fin,"%d", &smax);
	//printf("smax = %d\n", smax);
	

	int s[1002];



	for (int k = 0; k < smax + 1; k++)
	{
		fscanf_s(fin,"%1d", &s[k]);
		//printf("%d : %d\n", k, s[k]);
	}
	


	//printf("\n");
	
	int sum = 0;

	for (int i = 0; i < smax + 1; i++)
	{
		if (i == 0)
			sum += s[i];
		else
		{
			if (i > sum)
			{
				int temp = i - sum;

				ans += temp;
				sum += temp;
			}
			
			sum += s[i];
		}


	}

	
	

	fprintf(fout, "Case #%d: %d\n", num+1 , ans);

	
	
}
