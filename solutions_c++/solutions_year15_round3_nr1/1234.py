#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
#include<iostream>
using namespace std;
#define ll long long

int main()
{
    int t;
    cin>>t;
    int res=0;
    while(t--)
    {
        res++;
        int r,c,w;
        cin>>r>>c>>w;
        int ans=0;
        if(r!=1)
        {
            ans+=(r-1)*(c/w);
        }
        if(c%w==0)
            ans+=c/w-1+w;
        else
            ans+=c/w+w;
        printf("Case #%d: %d\n",res,ans);
    }
}
