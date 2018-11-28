#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <vector>
#include <map>

using namespace std;

int cf(long long li)
{
	char red[200];
	int i;
	sprintf(red,"%lld",li);
	//printf("%s",red);
	for (i=0;i<strlen(red)/2;i++) if (red[i]!=red[strlen(red)-i-1])
	{
		//printf("=0\n");
		return 0;
	}
	//printf("=1\n");
	return 1;
}

int main()
{
	FILE *fi,*fo;
	
	int i,j,t,tt;
	
	vector <long long> cfs;
	
	long long a,b,li;
	for (li=0;li<100000000;li++)
	{
		if (cf(li) && cf(li*li)) 
		{
			cfs.push_back(li*li);
		}
		
	}
	
	for (i=0;i<cfs.size();i++) printf("%lld\n",cfs[i]);
	
	
	
	fi=fopen("C.in","r");
	fo=fopen("C.out","w");
	
	fscanf(fi,"%d\n",&t);
	
	long long res;
	
	
	for (tt=0;tt<t;tt++)
	{	
		fscanf(fi,"%lld%lld",&a,&b);
		res=0;
		for (i=0;i<cfs.size();i++) if (cfs[i]>=a && cfs[i]<=b) res++;
		fprintf(fo,"Case #%d: %lld\n",tt+1,res);
		
		
	}
	
	fclose(fi);
	fclose(fo);

	return 0;
}
