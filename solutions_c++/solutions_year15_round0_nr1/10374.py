#include<iostream>
#include<stdio.h>

using namespace std;
int main(){
int n,arr[1002],s,r,m,a,i,j;
FILE *fp=fopen("A-small-attempt0.in","r");
FILE *fpo=fopen("out.txt","w");
fscanf(fp,"%d",&n);
for(i=0;i<n;i++)
{
fscanf(fp,"%d",&a);
fscanf(fp,"%d",&m);
for(j=a;j>=0;j--)
	{
	arr[j]= m%10;
	m=m/10;
	}
r=0;s=0;
for(j=0;j<=a;j++)
{
	if(s<j)
        {
	r=r+j-s;
        s+=j-s;
        }

	s+=arr[j];
	   
}
fprintf(fpo,"Case #%d: %d\n",i+1,r);
}
}

