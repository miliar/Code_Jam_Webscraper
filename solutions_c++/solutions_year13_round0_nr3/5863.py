#include <stdio.h>
#include <math.h>

bool isPalindrom(long long a)
{
	int d[20];
	int i=-1;
	while(a>0)
	{
		i++;
		d[i]=a%10;
		a /= 10;
	}

	bool p = true;
	int n=i+1;
	for(i=0; i<(n+1)/2;i++)
		if(d[i]!=d[n-1-i])
		{
			p=false;
			break;
		}

	return p;
}

int main()
{
	FILE* fin = fopen("C-small-attempt0.in", "r");
	FILE* fout = fopen("out.txt", "w");

	int n;
	fscanf(fin, "%d", &n);

	for(int i=1; i<=n; i++)
	{
		fprintf(fout, "Case #%d: ", i);

		long long A,B; int m=0;
		fscanf(fin, "%I64d %I64d", &A, &B);

		long long A1 = (long long)sqrt((double)A),B1=(long long)sqrt((double)B);

		for(long long k = A1; k<=B1; k++)
		{
			long long ksq = k*k;
			if((ksq>=A) && (ksq<=B) && isPalindrom(k) && isPalindrom(ksq))
				m++;
		}

		fprintf(fout, "%d\n", m);
	}

}