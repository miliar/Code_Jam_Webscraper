/*
Try Try & Try until you solve the problem...
Nothing is impossible for the problem solvers... :)
*/
/*

*/
#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <utility>
#include <numeric>

#include <cmath>
#include <cstdio>

#define IP(n) for(i=0;i<n;i++)
#define JP(n) for(j=0;j<n;j++)
#define KP(n) for(k=0;k<n;k++)

#define vi vector<int>
#define vi2 vector<vector<int>>
#define vs vector<string>

#define pb push_back
#define TC int t,check=1;cin>>t;while(check<=t)
#define FORIT(i,m) for(__typeof((m).begin()) i=(m).begin();i!=(m).end();i++)
#define ms(x,a) memset(x,a,sizeof(x))
#define read(a) freopen(a,"r",stdin)
#define write(a) freopen(a,"w",stdout)

using namespace std;

int dp[(1<<20)+10];

int open[25];
vector< vector<int> > got(25);

vector<int> ans;

int n,k,mask;

void reset()
{
    ms(dp,-1);
    ans.clear();

    for(int i=0;i<25;i++)
    got[i].clear();

    mask=0;
    for(int i=0;i<n;i++)
    mask|=(1<<i);
}

int lock(int p,int i)
{
    return p&(1<<i);
}

int calc(int a,vector<int> key,vector<int> ord)
{
    if(dp[a]!=-1) return dp[a];

    if(!a)
    {
        if(!ans.size())
        {
            for(int i=0;i<ord.size();i++)
            {
                ans.pb(ord[i]);
            }
        }
        return 1;
    }

    int ret=0;

    for(int i=0;i<n && !ret;i++)
    {
        if(lock(a,i))
        {
            //cout<<"Lock "<<i<<endl;
            int op=open[i];

            if(key[op]>0)
            {
                key[op]--;


                for(int j=0;j<got[i].size();j++)
                {
                    key[got[i][j]]++;
                }

                ord.pb(i+1);

                ret|=calc(a^(1<<i),key,ord);

                //cout<<"Return at "<<i<<endl;

                for(int j=0;j<got[i].size();j++)
                {
                    key[got[i][j]]--;
                }

                ord.pop_back();

                key[op]++;
            }
        }
    }

    dp[a]=ret;

    return ret;
}

int main()
{
    read("Ds.in");
    write("Ds.txt");

    int t,check=1;
    scanf("%d",&t);

    while(t--)
    {
        vector<int> key(205);
        vector<int> as;
        int x,y;
        scanf("%d %d",&k,&n);

        reset();

        for(int i=0;i<k;i++)
        {
            scanf("%d",&x);
            key[x]++;
        }

        for(int i=0;i<n;i++)
        {
            scanf("%d %d",&open[i],&x);

            for(int j=0;j<x;j++)
            {
                scanf("%d",&y);
                got[i].pb(y);
            }
        }

        printf("Case #%d:",check++);

        int res=calc(mask,key,as);
        if(res)
        {
            for(int i=0;i<ans.size();i++)
            printf(" %d",ans[i]);

            printf("\n");
        }
        else
        {
            printf(" IMPOSSIBLE\n");
        }
    }

    return 0;
}
