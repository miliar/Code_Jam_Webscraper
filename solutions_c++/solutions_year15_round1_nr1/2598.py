#include<bits/stdc++.h>
#include<stdio.h>
int a[100001];
int main()
{
    int t,t1,n,i,j,r,c=0;
    scanf("%d",&t1);
    for(i=1;i<=t1;i++)
    {
        c=0;
        scanf("%d",&n);
        for(j=0;j<n;j++)
        {
            scanf("%d",&a[j]);
        }
        for(j=0;j<(n-1);j++)
        {
            t=a[j]-a[j+1];
            if(t>0)
            c=c+t;
        }
        printf("Case #%d: %d",i,c);
        r=0;
       for(j=n-1;j>0;j--)
       {
        if(r<a[j-1]-a[j])
        r=a[j-1]-a[j];
       }
        c=0;
        if(r>=0)
        for(j=0;j<(n-1);j++)
        {
            if(a[j]>=r)
            c=c+r;
            else
            c=c+a[j];
        }
        printf(" %d\n",c);
    }
}
