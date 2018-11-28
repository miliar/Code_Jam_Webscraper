#include<cstdio>
#include<conio.h>
using namespace std;
int main()
{
	int t,k;
	FILE *f1,*f2;
    f1=fopen("B-large.in","r");
    f2=fopen("output.txt","w");
    //fscanf(f1,"%d\n",&t);
    fscanf(f1,"%d",&t);
    double ans=0,l,c,f,x;
	for(k=1;k<=t;k++)
	{
              ans=0;
              l=2.0;
	  	fscanf(f1,"%lf%lf%lf",&c,&f,&x);
	  	if(double(c)>=double(x))
	  	{fprintf(f2,"Case #%d: %.7llf\n",k,x/2.0); continue;}
	    while(1){
                 ans+=(double)c/l;
                // printf("$");
                 if((double)(x-c)/l>=(double)x/(l+f))
                 {
                                                     l=l+f;
                                                     continue;}
                  ans=ans+ (double)(x-c)/l;
                  break;
                  }
                  fprintf(f2,"Case #%d: %.7llf\n",k,ans);                              
                                                 
                                                 }
                                                 getch();
                                                 }    
                 
		
		
		
		
		
		
	
