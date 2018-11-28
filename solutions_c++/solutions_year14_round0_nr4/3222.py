#include<stdio.h>
#include<stdlib.h>
int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}
int main()
{
    FILE *fp,*fo;
	fp=fopen("D-large.in","r");
	fo=fopen("outputthirdlarge.o","w");
    int t,i,n,loss,win,j,p,q,x,y;
    float sum1,sum2,temp;
    fscanf(fp,"%d",&t);
    for(i=1;i<=t;i++)
    {
        fscanf(fp,"%d",&n);
        sum1=0;
        sum2=0;
        float a[n],b[n];
        for(int j=0;j<n;j++)
        {
            fscanf(fp,"%f",&a[j]);
        }
        if(n>1)
        {
        for(x=0;x<n;x++)
	    {
		    for(y=0;y<n-1;y++)
		    {
			    if(a[y]>a[y+1])
			    {
				 temp=a[y];
				 a[y]=a[y+1];
				 a[y+1]=temp;
			    }
		     }
	      }
        }
        for(int j=0;j<n;j++)
        {
            fscanf(fp,"%f",&b[j]);
        }
        if(n>1)
        {
        for(x=0;x<n;x++)
	    {
		    for(y=0;y<n-1;y++)
		    {
			    if(b[y]>b[y+1])
			    {
				 temp=b[y];
				 b[y]=b[y+1];
				 b[y+1]=temp;
			    }
		     }
	      }
        }
        loss=0;
        win=0;
        for(p=0,q=0;p<n;p++)
        {
            if(a[p]>b[q])
            {
                loss++;
                q++;
            }
        } 
        for(p=n-1,q=n-1;p>=0&&q>=0;p--)
        {
            if(a[p]<b[q])
            {
                win++;
                q--;
            }
        }
        fprintf(fo,"Case #%d: %d %d\n",i,loss,n-win);
    }
    return 0;
}
 
