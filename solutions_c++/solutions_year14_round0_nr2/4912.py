#include<stdio.h>
int main()
{
int test,k=1,m;
scanf("%d",&test);
for(m=1;m<=test;m++)
{
int v=0;
double c,f,x,j=0,ii=0,cc=0;
scanf("%lf %lf %lf",&c,&f,&x);

ii=x/2;


while(1)
{
     
           
     j+=c/(2+v*f) ;
     
     cc=j+x/(2+((v+1)*f)) ;
     
     if(cc>ii)
     break;
     
     else
     ii=cc;
      
      v++;
      
}


printf("Case #%d: %.7lf\n",k++,ii);
}

return 0;
}


