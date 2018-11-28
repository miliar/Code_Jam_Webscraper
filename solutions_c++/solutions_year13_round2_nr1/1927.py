#include<iostream>
using namespace std;

int compare (const void * a, const void * b)
{
  return ( *(long*)a - *(long*)b );
}

long compute (long A, long N, long value[]) {
	long curcount = 0;
	long mincount = 0;
	long tempA = A;
	long tempN = N;
	long i = 0, j = 0;
	long tempi = 0;
	long k = 0;
	long tempcount = 0;
	qsort(value, N, sizeof(long), compare);

	for (i = 0;i <= N ; i++) {
		if (i != 0) {
			if (tempA - 1 == 0) {
				return mincount;
			}
			tempA += tempA - 1;
			
			curcount++;
			tempcount = curcount;
		}
		for (j = N - i; j >= 0 || k == tempN; j--) {
			while (k < tempN && tempA > value[k]) {
				tempA += value[k];
				k++;	
				//j--;
				//tempi++;
			}
			if (k == tempN) {
				if (mincount == 0 && curcount > mincount)
					mincount = curcount;
				else if (curcount <= mincount)
					mincount = curcount;
				break;
				//return mincount;
			}
			else {
				tempN--;
				curcount++;							
			}

		}
		tempN = N;
		curcount = tempcount;
		i = k;
		//tempA += tempA - 1;
		//curcount++;
		
	}
	return mincount;
}

long main()
{
	long A,N, result;
	long value[110];
	long i;
	FILE *in;
	FILE *out;
	in = fopen("A-large.in","r");
	out = fopen("out.txt","w");
	long T;
	long Case = 1;
	fscanf(in,"%d",&T);
	while(Case <=T)
	{
		fscanf(in,"%d%d",&A,&N);
		for(i=0;i<N;i++)
		{
			fscanf(in,"%d",&value[i]);
		}
		result = compute(A, N, value);
		fprintf(out,"Case #%d: %d\n",Case,result);
		Case ++;
	}
	fclose(out);
	return 0;
}