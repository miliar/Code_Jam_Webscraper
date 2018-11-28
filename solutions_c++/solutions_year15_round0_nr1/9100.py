#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#define ll long long int
using namespace std;
int main()
{
    FILE *fp1,*fp2;
    fp1=fopen("in.txt","r");
    fp2=fopen("out.txt","w");
    ll maxi,t,i,avail,ans,T=0,len;
    char s[100000];
    fscanf(fp1,"%lld",&t);
    while(t--)
    {
        fscanf(fp1,"%lld%s",&maxi,s);
        len=strlen(s);
        for(i=0,avail=0,ans=0;i<len;i++)
        {
            if(avail<i)
            {
                ans+=(i-avail);
                avail=i;
            }
            avail+=(s[i]-'0');
        }
        fprintf(fp2,"Case #%lld: %lld\n",++T,ans);
    }
    return 0;
}
