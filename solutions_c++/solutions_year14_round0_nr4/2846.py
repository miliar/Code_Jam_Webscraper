#include<stdio.h>

int main(void)
{
	FILE *in = fopen("D-large.in","r");
	FILE *out = fopen("output.txt","w");
	int testcase;
	fscanf(in,"%d",&testcase);
	for(int T = 1; T <= testcase; T++)
	{
		int n;
		double naomi[1001], ken[1001];
		fscanf(in,"%d",&n);
		for(int i = 0; i < n; i++)
			fscanf(in,"%lf",&naomi[i]);
		for(int i = 0; i < n; i++)
			fscanf(in,"%lf",&ken[i]);

		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < n; j++)
			{
				if(naomi[i] < naomi[j]){
					double swap = naomi[i];
					naomi[i] = naomi[j];
					naomi[j] = swap;
				}
			}
		}

		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < n; j++)
			{
				if(ken[i] < ken[j]){
					double swap = ken[i];
					ken[i] = ken[j];
					ken[j] = swap;
				}
			}
		}

		int i = 0, j = 0;
		naomi[n] = 2; ken[n] = 2;
		double inter[2002];
		int owner[2002]; // 1: Naomi 2:Ken
		int next_N[2002];
		int next_K[2002];
		int prev_N[2002];
		int prev_K[2002];
		int tprev_N = 0;
		int tprev_K = 0;
		int pt = 0;
		/*
		if(naomi[0] <= ken[0]){
			prev_N = 0;
			prev_K = 1;
		}
		else{
			prev_N = 1;
			prev_K = 0;
		}
		*/
		while(1){
			if(i == n && j == n) break;
			next_N[pt] = 0;
			next_K[pt] = 0;
			if(naomi[i] <= ken[j]){
				inter[pt] = naomi[i++];
				owner[pt] = 1;
				next_N[tprev_N] = pt;
				tprev_N = pt;
				pt++;
			}
			else if(naomi[i] > ken[j]){
				inter[pt] = ken[j++];
				owner[pt] = 2;
				next_K[tprev_K] = pt;
				tprev_K = pt;
				pt++;
			}
		}		

		int war = 0;
		int d_war = 0;
		int stN,stK;
		pt = -1;
		for(i = 0; i < 2 * n; i++)
		{
			prev_N[i] = -1;
			prev_K[i] = -1;
		}
		for(i = 2 * n - 1; i >= 0; i--)
		{
			if(owner[i] == 1){
				if(pt == -1){
					stN = i;
					pt = i;
				}
				else{
					prev_N[pt] = i;
					pt = i;
				}
			}
		}
		pt = -1;
		for(i = 2 * n - 1; i >= 0; i--)
		{
			if(owner[i] == 2){
				if(pt == -1){
					stK = i;
					pt = i;
				}
				else{
					prev_K[pt] = i;
					pt = i;
				}
			}
		}
		/*
		for(int i = 0; i < 2 * n; i++)
			printf("%lf ",inter[i]);
		printf("\n");
		for(int i = 0; i < 2 * n; i++)
			printf("%d ",owner[i]);
		printf("\n");
		for(int i = 0; i < 2 * n; i++)
			printf("%d ",prev_N[i]);
		printf("\n");
		for(int i = 0; i < 2 * n; i++)
			printf("%d ",prev_K[i]);
		printf("\n");
		*/
		for(i = stN, j = stK; i >= 0; i--)
		{
			if(owner[i] == 1){
				while(j > i) j = prev_K[j];
//				printf("j = %d\n",j);
				if(i > j && j != -1) d_war++;
				if(j != -1) j = prev_K[j];				
				else break;
			}
		}
		for(i = stK, j = stN; i >= 0; i--)
		{
			if(owner[i] == 2){
				while(j > i){
				//	printf("j = %d\n",j);
					j = prev_N[j];
				}
			//	printf("j = %d\n\n",j);
				if(i > j && j != -1) war++;
				if(j != -1) j = prev_N[j];
				else break;
			}
		}

		fprintf(out,"Case #%d: %d %d\n",T,d_war, n - war);
//		printf("%d %d\n",d_war, n - war);
	}
	fclose(in);
	fclose(out);
	return 0;
}