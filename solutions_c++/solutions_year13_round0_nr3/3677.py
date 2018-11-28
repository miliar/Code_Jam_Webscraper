#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<conio.h>

bool palindrom( long long a)
{
	bool palindrom = true;
	int b[100],n = 0;
	int i;
	while( a > 0 )
	{
		b[n++] = a%10;
		a = a/10;
	}
	for( i = 0; i < n;i++ )
	{
		if( b[i] != b[n-1-i] )
			palindrom = false;
	}
	return palindrom;
}

int	main()
{
	FILE *f1,*f2;
	int error;
	error = fopen_s(&f1,"C-small-attempt0.in","r");
	if(error == -1)
		printf("eroare la deschidere");
	error = fopen_s(&f2,"C-small-attempt0.out","w");
	if(error == -1)
		printf("eroare la deschidere2");

	int T,nr_faresquare;
	int fsrank = 0;
	long long i,j,N,M;

	fscanf_s(f1,"%d",&T);
	for(i = 0; i < T; i++)
	{
		nr_faresquare = 0;
		fscanf_s(f1,"%lld %lld",&N,&M);
		for(j = (long long)sqrt((long double)N); j < (long long)sqrt((long double)M)+1; j++)
		{
			if( palindrom(j) && palindrom(j*j) && (j*j >= N) )
			{
				nr_faresquare++;
			}
		}

		fprintf_s(f2,"Case #%lld: %d\n", i+1, nr_faresquare);
	}

	return 0;
}