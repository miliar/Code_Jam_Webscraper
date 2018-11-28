#include<set>
#include<iostream>
#include<cstdlib>
#include<cstdio>
using namespace std;
int main()
{
    long long t,n,a[100000],s=0,s1=0,i,x,y,max,c=1;
    FILE *fp,*fo;
    fp=fopen("A-large.in","r");
    fo=fopen("output1.txt","w");
    fscanf(fp,"%lld",&t);
    while(t--)
    {
        max=0;
        s=0;
        s1=0;
        fscanf(fp,"%lld",&n);
        for(i=0;i<n;i++)
        fscanf(fp,"%lld",&a[i]);
        s=0;
        x=a[0];
        max=0;
        for(i=1;i<n;i++)
        {
        	x=a[i-1];
            y=a[i];
            if(x-y>max)
            max=x-y;
            if(y<x)
            s+=x-y;
        }
        x=a[0];
        s1=0;
for(i=1;i<n;i++)
        {
        	x=a[i-1];
            y=a[i];
            //if(x>)
            //{
            	if(x<max)
            	s1+=x;
            	else
            	s1+=max;
            /*}
            else
            {
            	if(x>max)
            	{
            		s1+=max;
            	}
            	else
            	{
            		s1+=x;
            	}
            }*/



        }        fprintf(fo,"Case #%lld: %lld %lld\n",c++,s,s1);
    }
    return 0;
}
