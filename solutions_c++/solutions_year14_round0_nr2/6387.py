#include<stdio.h>
#include<iostream>

using namespace std;

int main(int argc,char *argv[])
{
FILE *fp,*fp2;
fp=fopen(argv[1],"r+");
fp2=fopen(argv[argc-1],"w+");
int num,test;
fscanf(fp,"%d",&test);
num=test;
while(test--)
{
double sum=0,c,f,x;
int i=0,n;
fscanf(fp,"%lf%lf%lf",&c,&f,&x);
if(x<c)
{
	sum=x/(double)2;
	fprintf(fp2,"Case #%d: %0.6lf\n",num-test,sum);	
	continue;
}
n=(x/c-2/f);
for(i=0;i<n;i++)
	sum=sum+(c/(double)(2+i*f));
sum+=x/(double)(2+i*f);
fprintf(fp2,"Case #%d: %0.7lf\n",num-test,sum);
}
fclose(fp);
return 0;
}
