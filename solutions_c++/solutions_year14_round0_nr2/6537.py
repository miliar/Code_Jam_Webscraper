#include<stdio.h>
#include<conio.h>
int main()
{
int i,j,k,l,m,T;
FILE *fp,*fp1;
double c,f,x,sum=0,sum1=0,sum2=0,n=(double)2,time;
fp=fopen("cook2.in","r");
fp1=fopen("anj3.txt","w");
fscanf(fp,"%d",&T);
for(i=0;i<T;i++)
{
fscanf(fp,"%lf %lf %lf",&c,&f,&x);
sum=sum1=sum2=0;
n=(double)2;
do
 {
 sum=sum2;
 sum1=(x/n)+sum;
 sum2=(c/n)+sum;
 time=(c/n)+(x/(n+f))+sum;
 n=n+f;
 }while(sum1>time);
 sum=sum1;
fprintf(fp1,"Case #%d: %.7lf\n",i+1,(double)sum);
}
fclose(fp);
fclose(fp1);
return 0;
}