#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <map>

using namespace std;

char red[10000000];

int main()

{
	FILE *fi,*fo;
	

	
	char c[300];
	char ci;
	
	int i,j,t,tt;
	
	long long n,tot,ttot,zaredom,maks,total,count;
	
	bool seen[10],all;
	
	fi=fopen("A.in","r");
	fo=fopen("A.out","w");
	
	fscanf(fi,"%d\n",&t);
	
	
	for (tt=0;tt<t;tt++)
	{	
		fscanf(fi,"%lld",&n);
		tot=0;
		for (i=0;i<10;i++) seen[i]=false;
		count=0;
		while (1)
		{	
			tot+=n;
			ttot=tot;
			seen[ttot%10]=true;
			while (ttot)
			{
				seen[ttot%10]=true;
				ttot/=10;
			}			
			all=true;
			for (i=0;i<10;i++) if (!seen[i]) all=false;
			if (all) break;
			if (count>10000) break;
			
			count++;
				
		}
		
		
		
		
		if (count>10000) fprintf(fo,"Case #%d: INSOMNIA\n",tt+1);
		else fprintf(fo,"Case #%d: %lld\n",tt+1,tot);
	}
	
	fclose(fi);
	fclose(fo);

	return 0;
}
