#include<stdio.h>
int main()
{
    int t,i,n,loss,win,x,y,j;
    float sum1,sum2,temp,a[10000],b[10000];
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d",&n);
        sum1=0;
        sum2=0;
        for(j=0;j<n;j++)
        scanf("%f",&a[j]);
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
        for(int j=0;j<n;j++)
        scanf("%f",&b[j]);
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
        loss=0;
        win=0;
        y=0;
        for(x=0;x<n;x++)
        {
            if(a[x]>b[y])
            {
                loss++;
                y++;
            }
        } 
        for(x=n-1,y=n-1;x>=0&&y>=0;x--)
        {
            if(a[x]<b[y])
            {
                win++;
                y--;
            }
        }
        printf("Case #%d: %d %d\n",i,loss,n-win);
    }
    return 0;
}
 
