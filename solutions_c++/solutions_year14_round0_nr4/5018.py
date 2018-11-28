#include<stdio.h>
#include<algorithm>
#include<iostream>
using namespace std;
int main()
{
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        float sum1=0,sum2=0;
        int n;
        scanf("%d",&n);
        float a[n],b[n];
        for(int j=0;j<n;j++)
        {
            scanf("%f",&a[j]);
            //sum1+=a[j];
        }
        if(n>1)
        sort(a,a+n);
        for(int j=0;j<n;j++)
        {
            scanf("%f",&b[j]);
            //sum2+=b[j];
        }
        if(n>1)
        sort(b,b+n);
        int ow=0,w=0;
        for(int p=0,q=0;p<n;p++)
        //for(int q=0;q<n;q++)
        {
            //cout<<a[p]<<" "<<b[q]<<endl;
            if(a[p]>b[q])
            {
                ow++;
                q=q+1;
            }
        }
        //cout<<ow<<endl;

        for(int p=n-1,q=n-1;p>=0&&q>=0;--p)
        //for(int q=0;q<n;q++)
        {
            if(a[p]<b[q])
            {
                w++;
                q=q-1;
            }
        }
            printf("Case #%d: %d %d\n",i,ow,n-w);
    }
}
