#include<stdio.h>
#include<set>
#include<algorithm>
#include<string>
using namespace std;

set<long long int> all;

//FILE *pal=fopen("pal.in","w");

int isPal (long long int x)
{
	long long int y =0, z=x;
	while(z)
	{
	 y = y*10 + z%10;
	 z /= 10;
	}
	if(y == x)
		return 1;
	return 0;
}
void gen()
{
	long long int i;
	for(i=1; i<=1000; i++)
		if(isPal(i))
		{
			long long int t = i*i;
			if(isPal(t))
			{
				all.insert(t);	
				//fprintf(pal,"%lld,",t);
			}
		}
	return;
}
int main()
{
	all.clear();
	gen();
	//fclose(pal);
	//return 0;
	FILE *in=fopen("c.in","r");
	FILE *out=fopen("c.out","w");
 long long	int i,n,a,b,r;
	fscanf(in,"%lld",&n);
	for(i=1;i<=n;i++)
	{
		r = 0;
		fscanf(in,"%lld%lld",&a,&b);
		for(;a<=b;a++)
			if(all.find(a)!= all.end())
				r++;
		fprintf(out,"Case #%lld: %lld\n",i,r);
	}
	return 0;
}