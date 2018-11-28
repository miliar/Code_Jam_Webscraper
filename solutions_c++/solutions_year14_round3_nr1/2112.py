#include <iostream>
#include <stdio.h>
using namespace std;

int main() {


unsigned long int t,i,cnt,s;
unsigned long int p,q;
FILE *ftr=fopen("A-small-attempt3.in","r");
FILE *ftr1=fopen("output.txt","w");
fscanf(ftr,"%d",&t);
for(i=0;i<t;i++)
{    cnt=0;
	fscanf(ftr,"%i/%i",&p,&q);


	if((p/q)>1 || ((q%p==0)&&!( !((q/p) == 0) && !((q/p) & ((q/p) - 1)))) || ((q%p!=0)&&!( !((q) == 0) && !((q) & ((q) - 1)))))
	{
		fprintf(ftr1,"Case #%d: impossible\n",i+1);
	}

	else
	{
	if(q%p==0)
	{  s=q/p;
	   while(s!=1)
	   {
	   	 s=s/2;
	   	 cnt++;
	   }

    }
    else
    {
    	while(p%2==0)
    	     {
    	     	p=p/2;
    	        q=q/2;
    	     }
    while(q>=p)
	   {
	   	 q=q/2;
	   	 cnt++;
	   }
    }
   fprintf(ftr1,"Case #%d: %d\n",i+1,cnt);

	}

}

	return 0;
}
