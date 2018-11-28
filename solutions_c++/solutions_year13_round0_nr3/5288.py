#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
int isP(long long int v)
{
    long long int y=0,x=v;
    while(x!=0)
    {
        y+=x%10;
        x/=10;
        y*=10;
    }
    y/=10;
    if(v==y)
        return 1;
    else
        return 0;
}
int main()
{
    int k=0;
    long long int i;
    long long int *pal=(long long int *)malloc(1000*sizeof(long long int));
    for(i=1;i*i<=1000;i++)
    {
        if(isP(i))
        {
            if(isP(i*i))
                pal[k++]=i*i;
        }
    }
    int t,cas=1;
    cin>>t;
    int j;
    while(t--)
    {
        int a,b,ct=0;
        cin>>a>>b;
        for(j=0;j<k;j++)
        {
            if(pal[j]>=a && pal[j]<=b)
                ct++;
            if(pal[j]>b)
                break;
        }
        cout<<"Case #"<<cas++<<": "<<ct<<"\n";
    }
}
