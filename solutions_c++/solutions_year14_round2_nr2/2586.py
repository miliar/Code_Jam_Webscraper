#include<iostream>
#include<cstdio>
#include<cmath>
#define  ll long long
using namespace std;
int main()
{
  freopen( "input.txt", "r", stdin );
  freopen( "output.txt", "w", stdout );
    
    
    int t;
    scanf("%d",&t);
    int i,j,k;
    for(k=1;k<=t;k++)
    {
                     int a,b,l;
                     cin>>a>>b>>l;
                     ll count=0;
                     for(i=0;i<a;i++)
                     for(j=0;j<b;j++)
                     if((i&j)<l)
                     count++;
                     printf("Case #%d: %lld\n",k,count);
                     
    }
}                                          
    
