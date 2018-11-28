#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <utility>
#define inf 2000000000
#define ll long long
#define Max

using namespace std;

int n,m,mx,mxc,dp[1200];
string str[10];

int calc(int mask)
{
    if(dp[mask]!=-1) return dp[mask];

    map<string,bool> mymap;
    mymap.clear();
    string now;

    int i,j,k,r=1;

    for(i=0;i<m;i++)
    {
        if(mask & (1<<i))
        {
            now="";

            for(j=0;j<str[i].length();j++)
            {
                now+=str[i][j];

                if(mymap[now]==0)
                {
                    mymap[now]=1;
                    r++;
                }
            }

        }
    }

    return dp[mask]=r;
}

void work(int x,vector<int> v)
{
    if(x==m)
    {
        int i,j,k;

        for(i=0;i<v.size();i++)
        {
            if(v[i]==0) return;
        }

        for(k=0,i=0;i<v.size();i++)
        {
            k+=calc(v[i]);
        }

        if(k>mx)
        {
            mx=k;
            mxc=1;
        }

        else if(k==mx)
        {
            mxc++;
        }




        return;
    }

    int i,j,k;

    for(i=0;i<n;i++)
    {
        j=v[i];

        v[i]|=(1<<x);

        work(x+1,v);

        v[i]=j;
    }
}



int main()
{
    int i,j,k,T,cas,ret=0;

    freopen("D-small-attempt0(2).in","r",stdin);
    freopen("d-small.txt","w",stdout);

    scanf("%d",&T);

    for(cas=1;cas<=T;cas++)
    {
        scanf("%d %d",&m,&n);

        for(i=0;i<m;i++) cin>>str[i];

        vector <int> v;

        for(i=0;i<n;i++) v.push_back(0);

        mx=mxc=0;

        memset(dp,-1,sizeof(dp));

        work(0,v);

        printf("Case #%d: %d %d\n",cas,mx,mxc);
    }

    return 0;
}
