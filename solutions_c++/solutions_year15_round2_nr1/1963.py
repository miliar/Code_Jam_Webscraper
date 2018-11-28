#include <iostream>
#include <cstdio>
#include <bits/stdc++.h>

#define MOD 1000000007
#define sz 1000005
using namespace std;

int minim[sz];

int flag=0;
int reversemin(int i)
{
    if(i%10==0)
    {
        flag=1;
    }
    string s="";
    int temp =i;
    while(temp>0)
    {
        s+=temp%10+'0';

        temp = temp/10;
    }
    int slen = s.length();

    int ans=0;
    for(int i=0;i<slen;i++)
    {
        ans = ans*10+(s[i]-'0');
    }
    return ans;
}
int main()
{
    minim[0]=0;
    for(int i=1;i<sz;i++)
    {
        flag=0;
        int u =reversemin(i);
        if(u<i && flag==0)
        {
            minim[i] = min(minim[i-1]+1,minim[u]+1);
        }
        else
        {
            minim[i] = minim[i-1]+1;
        }

    }
    freopen("A-small2.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int iter=1;iter<=T;iter++)
    {
        int x;
        scanf("%d",&x);
        printf("Case #%d: %d\n",iter,minim[x]);
    }


}
