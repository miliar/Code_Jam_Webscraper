#include <bits/stdc++.h>
#include <stdio.h>
#include <stdlib.h>
using namespace std;


typedef long long LL;



int ans[2000];
int q[2000];


int go(int from, int n)
{
   int a=from;
   int b=0;
   for(int i=0;i<n;i++)
   {
        b=(b<<1)+(1-a&1);
        a>>=1;
   }
   return (a<<n)+b;
}


void prepare()
{
    for(int i=0;i<1024;i++){ans[i]=-1;}
    ans[0]=0;

    int qb=0,qe=1;
    q[0]=0;
    while(qb!=qe)
    {
        int t = q[qb++];
        for(int j=1;j<=10;j++)
        {
            int h = go(t,j);
            if(ans[h]==-1)
            {
                ans[h]=ans[t]+1;
                q[qe++]=h;
            }
        }
    }
}

int main()
{

    prepare();
    LL T,x;


    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    cin>>T;
    string s;



    for(int i=1;i<=T;i++)
    {
        cin>>s;
        int l = s.length();
        int st=0;
        for(int j = 0;j<l;j++)
            if(s[j]=='-')
                st+=(1<<j);

        printf("Case #%d: %d\n",i,ans[st]);
    }

}
