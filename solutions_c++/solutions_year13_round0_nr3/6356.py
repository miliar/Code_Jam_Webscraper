#include <stdlib.h>
#include <stdio.h>
#include <math.h>

char check(long a)
{
	long b = 0, tmp = a;
	
	do{
	  b *= 10;
	  b += a % 10;
	} while (a /= 10);
	
	return (char)((tmp==b) ? 1 : 0);
}

int main()
{
	long i = 0, ncases = 0;
   	FILE *fin, *fout;
	
	fin = fopen("in.txt", "r");
	if(!fin)
		return 1;
	
	fout = fopen("out.txt", "w");
	if(!fout)
		return 1;    
	
	fscanf(fin, "%d\n", &ncases);

	for(long n=0; n<ncases; n++)
	{
		long a=0, b = 0, nres = 0, i =0;
		fscanf(fin, "%d %d\n", &a, &b);

		for(i = (long)sqrt(a); i<= (long)sqrt(b); i++)
		{
		   if ((i == (long)sqrt(a)) && (a != (i*i)))
		       continue;

		   if (check(i) && check(i*i))
		      nres++;

	    }
		fprintf(fout, "Case #%d: %d\n", n+1, nres);
	}
	
	fclose(fin); fclose(fout);
}