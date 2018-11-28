#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<string.h>
#include<fstream>
#include<limits.h>
#include<math.h>
int main()
{
	FILE *f,*fp;
	f=fopen("D:\A-small-attempt2.in","r");
	fp=fopen("D:\hacker.in","w");
	int n=1,T;
	fscanf(f,"%d",&T);
	while(T--)
	{
		
		long long int P,Q;
        fscanf(f,"%lld/%lld",&P,&Q);
	    long long int i=0,j=0,count1=0,count2=0;
	    if(Q%P==0)
	    {
	    	Q=Q/P;
	    	P=1;
	    }
	    while(P>=pow(2,i))
	    {
	    	i++;
	    }
	    if(P==pow(2,(i-1)));
	    count1++;
	    while(Q>=pow(2,j))
	    {
	    	j++;
	    }
	    if(Q==pow(2,(j-1)))
	    count2++;
		if(count2!=0)
	    fprintf(fp,"Case #%d: %lld\n",n++,j-i);
	    else
	    fprintf(fp,"Case #%d: impossible\n",n++);
	}
	fclose(f);
	fclose(fp);
	return 0;
}
