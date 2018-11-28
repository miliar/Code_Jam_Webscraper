#include <cstdio>
#include <iostream>
using namespace std;
int main()
{
	long long t,T,r,c,w,i,count;
	FILE * fr=fopen("A-small-attempt1.in","r");
	FILE * fw=fopen("A.out","w");
	fscanf(fr,"%lld",&t);
	T=t;
	while(t--)
	{
		fscanf(fr,"%lld %lld %lld",&r,&c,&w);
		count=(c-1)/w+(w);
		fprintf(fw, "Case #%lld: %lld\n",(T-t),count);
	}
	fclose(fr);
	fclose(fw);
}