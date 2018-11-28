#include<iostream>
#include<algorithm>

using namespace std;

int Dcmp (const void * a, const void * b)
{
	double re;
	re = *(double*)a - *(double*)b;
	if(re>0.0)
		return 1;
	else if(re == 0.0)
		return 0;
	else return -1;
}

int main()
{
	int T,n;
	double *N,*K;
	int win_Dw,win_w;
	FILE *fp1,*fp2;

	fp1=fopen("D-large.in","r");
	fp2=fopen("D-large.out","w+");

	fscanf(fp1,"%d",&T);

	for(int i=0; i < T; i++)
	{
		win_Dw = win_w = 0;

		fscanf(fp1,"%d",&n);

		N=(double*)malloc(sizeof(double)*n);
		K=(double*)malloc(sizeof(double)*n);

		for(int c=0; c<n; c++)
			fscanf(fp1,"%lf",&N[c]);
		for(int c=0; c<n; c++)
			fscanf(fp1,"%lf",&K[c]);

		qsort(N,n,sizeof(double),Dcmp);
		qsort(K,n,sizeof(double),Dcmp);

		int j=0;
		for(int t=0; t<n; t++)
			if( K[j] < N[t])
			{
				win_Dw++;
				j++;
			}

		j=0;

		for(int t=0; t<n; t++)
			if( N[j] < K[t])
			{
				win_w++;
				j++;
			}

		fprintf(fp2,"Case #%d: %d %d\n",i+1,win_Dw,n-win_w);
		free(K);
		free(N);
	}
	fclose(fp1);
	fclose(fp2);


	return 0;
}