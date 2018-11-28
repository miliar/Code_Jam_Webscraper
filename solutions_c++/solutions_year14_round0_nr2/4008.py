#include<stdio.h>
using namespace std;
int main()
{
    FILE *fi,*fo;
    fi= fopen("B-large.in","r");
    fo = fopen("output.txt","w");

    int t,k;
   double c,f,x,time,rate;
    fscanf(fi,"%d",&t);
    for(k=1;k<=t;k++)
    {
    	
        fscanf(fi,"%lf%lf%lf",&c,&f,&x);
        time=0.0000000;
        rate=2.0000000;
        while(1)
        {
        	if(x/rate<c/rate+x/(rate+f))
        	{
        		time+=x/rate;
				break;
        	}
        	else
        	{
        		time+=c/rate;rate+=f;
        	}
        }
        fprintf(fo,"Case #%d: %.7f\n",k,time);
    }
    return 0;
}
