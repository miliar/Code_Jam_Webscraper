#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<iostream>
using namespace std;
double a[1005];
double b[1005];
double c[1005];
int you(int n)
{
    int i,j,s=0;
    j=0;
    for(i=0;i<n;i++)
    {
        while(j<n&&a[j]<b[i])
            j++;
        if(j==n)
            break;
        j++;
        s++;
    }
    return s;
}
int cmp(double a,double b)
{
    return a<b;
}
int main()
{
    int i,n,m,t,k,N;
    freopen("D-large.in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    N=t;
    while(t--)
    {
        cin>>n;
        for(i=0;i<n;i++)
            scanf("%lf",&a[i]);
        for(i=0;i<n;i++)
            scanf("%lf",&b[i]);
        sort(a,a+n,cmp);
        sort(b,b+n,cmp);
        m=you(n);
        for(i=0;i<n;i++)
        {
            c[i]=a[i];
            a[i]=b[i];
            b[i]=c[i];
        }
        k=you(n);
        printf("Case #%d: %d %d\n",N-t,m,n-k);
    }
    return 0;
}