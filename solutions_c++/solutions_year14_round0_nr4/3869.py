#include <iostream>
#include<algorithm>
#include<vector>
#include<cstdio>
using namespace std;
float a[1005],b[1005],mini;
int binsrch(float x,int n)
{
    int low=0,high=n,mid=int((low+high)/2);
    while(low<mid)
    {
        if(x<a[mid])
        high=mid;
        else
        low=mid;
        mid=int((low+high)/2);
    }
    if(a[mid]<x)
    return mid;
    else
    return mid-1;
}
int m,T,cnt,i,j,l,n,t,lo,hi;
int main()
{
    freopen("inp2.txt","r",stdin);
    freopen("out3.txt","w",stdout);
    scanf("%d",&T);
    t=T;
    while(T--)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
        scanf("%f",&a[i]);
        for(i=0;i<n;i++)
        scanf("%f",&b[i]);
        sort(a,a+n);
        sort(b,b+n);
        lo=0;
        for(i=0;i<n;i++)
        {
            if(a[i]>b[lo])
            lo++;
        }
        printf("Case #%d: ",t-T);
        printf("%d ",lo);

        //optimal
        hi=n-1;
        lo=0;
        for(i=n-1;i>=0&&lo<=hi;i--)
        {
            if(a[i]>b[hi])
            lo++;
            else
            hi--;
        }
        printf("%d\n",lo);
    }
    return 0;
}
