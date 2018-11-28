#include <stdio.h>
#include <stdlib.h>
#include <string.h>
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
	
	char red[1000];
	
	int i,j,t,tt;
	char last;
	
	long long n,tot,ttot,zaredom,maks,total,count;
	
	bool seen[10],all;
	
	fi=fopen("B.in","r");
	fo=fopen("B.out","w");
	
	fscanf(fi,"%d\n",&t);
	
	
	for (tt=0;tt<t;tt++)
	{	
		fscanf(fi,"%s",red);
		
		count=0;
		while (red[0]!=0 && red[strlen(red)-1]=='+') red[strlen(red)-1]=0;
		if (red[0]==0) 
		{
			fprintf(fo,"Case #%d: %lld\n",tt+1,count);
			continue;
		}
		
		count=1;
		last=red[0];
		for (i=1;red[i];i++)
		{
			if (last!=red[i])
			{
				count++;
				last=red[i];
			}
		}
		
		//if (count>10000) fprintf(fo,"Case #%d: INSOMNIA\n",tt+1);
		//else 
		fprintf(fo,"Case #%d: %lld\n",tt+1,count);
	}
	
	fclose(fi);
	fclose(fo);

	return 0;
}
