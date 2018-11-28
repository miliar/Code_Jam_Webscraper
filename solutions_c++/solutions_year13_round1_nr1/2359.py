#include<iostream>
#include<stdlib.h>
using namespace std;
int main()
{
    long long int *a=(long long int *)malloc(10000*sizeof(long long int));
    int i,k=0;
    a[0]=3;
    for(i=1;i<=10000;i++)
        a[i]=a[i-1]+2;
    int r,t,n,cas=1;
    cin>>n;
    while(cas<=n)
    {
        cin>>r>>t;
        int ct=0;
        if(a[r-1]<=t)
        {
            int s=a[r-1];
            ct=1;
            for(i=r+1;s<=t;i+=2)
            {
                s+=a[i];
                if(s<=t)
                ct++;
            }
        }
        cout<<"Case #"<<cas<<": "<<ct<<"\n";
        cas++;
    }
    return 0;
}