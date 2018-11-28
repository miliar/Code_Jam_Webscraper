#include<stdio.h>
#include<math.h>

int counter=0;
long long int solve( long long int rr, long long int tt)
{	
	long long int ret;
	long long int a;
	long long int r = rr;
	long long int t = tt;
	a = (r+1) * (r+1) - r*r;
	t = t-a;
	for(ret=0; t>=0; ret++)
	{
		a = a+4;
		t = t-a;
	}
	//printf("%d\n", ret);
	return ret;
}
int main()
{
	FILE *inp, *out;
	int T;
	long long int r, t;
	int i;
	long long retval=0;
	inp = fopen("c:\\download\\A-small-attempt4.in","r");
	//inp = fopen("c:\\download\\sample.txt","r");
	out = fopen("c:\\download\\out.txt","w");

	fscanf(inp,"%d\n",&T);
	for(i=0;i<T;i++)
	{
		fscanf(inp, "%lld %lld\n", &r, &t);
		retval = solve(r,t);
		if(retval == 0)
			fprintf(out,"Case #%d: 1\n", ++counter);
		else
			fprintf(out,"Case #%d: %lld\n", ++counter, retval);
	}
	fclose(inp);
	fclose(out);

	return 0;
}