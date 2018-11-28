#include<stdio.h>
#include<algorithm>
using namespace std;

int main()
{
    FILE *fi,*fo;
    fi=fopen("D-large.in","r");
    fo=fopen("output.txt","w");
    int t,k,i;
    double a[10006],b[10006];
    int pa,pb,n,count,ans_cheat,ans_opt;
    fscanf(fi,"%d",&t);
    for(k=1;k<=t;k++)
    {
        fscanf(fi,"%d",&n);
        for(i=0;i<n;i++)fscanf(fi,"%lf",&a[i]);
        for(i=0;i<n;i++)fscanf(fi,"%lf",&b[i]);
        sort(a,a+n);sort(b,b+n);
        ans_cheat=0;
        count=0;pa=n-1;pb=n-1;
        while(count<n)
        {
        	if(a[pa]>b[pb])
        	{
        		ans_cheat++;
        		pa--;pb--;
        	}
        	else
        	{
        		pb--;
        	}
        	count++;
        }
        ans_opt=0;
        count=0;pa=n-1;pb=n-1;
        while(count<n)
        {
        	if(a[pa]>b[pb])
        	{
        		ans_opt++;
        		pa--;
        	}
        	else
        	{
        		pa--;pb--;
        	}
        	count++;
        }
        fprintf(fo,"Case #%d: %d %d\n",k,ans_cheat,ans_opt);
    }
    return 0;
}
