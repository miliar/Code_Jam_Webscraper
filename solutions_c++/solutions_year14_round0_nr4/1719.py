#include<stdio.h>
#include<algorithm>
using namespace std;

int main()
{
    FILE *fp,*fp1;

    fp = fopen("D-large.in","r");
    fp1 = fopen("file3.txt","w");

    int t,k,i,ans1,ans2,n,top1,top2,min1;
    double c[1005],d[1005];
    long long int a[1005],b[1005];
    fscanf(fp,"%d",&t);
    for(k=1;k<=t;k++)
    {

        ans1=0;ans2=0;

        fscanf(fp,"%d",&n);
        top1=n,min1=1,top2=n;
        for(i=1;i<=n;i++)
            {fscanf(fp,"%lf",&a[i]);
            //a[i]=1000000*c[i];
            }
        for(i=1;i<=n;i++)
            {fscanf(fp,"%lf",&b[i]);
            //b[i]=1000000*d[i];
            }
        sort(a+1,a+n+1);
        sort(b+1,b+n+1);

        while(top2>0)
        {
            //printf("%lld  %lld\n",a[top1],b[top1]);
            if(a[top1]>b[top2])
            {
                ans1++;
                top1--;
                top2--;
            }
            else
            {
                top2--;
            }

        }
       printf("\n");
       int j;
        for(i=1,j=1;i<=n,j<=n;i++,j++)
        {
            while(a[i]>b[j] && j<=n)
                {
                    j++;
                    ans2++;
                }
        }
        fprintf(fp1,"Case #%d: %d %d\n",k,ans1,ans2);


    }
    return 0;
}
