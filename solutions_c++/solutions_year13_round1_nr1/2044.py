#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<conio.h>

int	main()
{
	FILE *f1,*f2;
	int error;
	error = fopen_s(&f1,"A-small-attempt0.in","r");
	if(error == -1)
		printf("eroare la deschidere");
	error = fopen_s(&f2,"A-small-attempt0.out","w");
	if(error == -1)
		printf("eroare la deschidere2");
	int T;
	int nr_of_circles,i;
	long long r,t;
	fscanf_s(f1,"%d",&T);
	for(i = 0;i<T;i++)
	{
		nr_of_circles = 0;
		fscanf_s(f1,"%lld %lld",&r,&t);
		while(t>0)
		{
			t = t - ((r+1)*(r+1)-r*r);
			if(t>=0)
			{
				nr_of_circles ++;
			}
			r=r+2;
		}
		fprintf_s(f2,"Case #%d: %d\n", i+1, nr_of_circles);
	}

	return 0;
}