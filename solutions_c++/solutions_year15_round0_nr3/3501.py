#include<iostream>
#include<algorithm>
#include<cstdio>
#include<string.h>
#include<climits>
#include<map>
using namespace std;
#define FOR(i,n) for(i=0;i<n;i++)
#define sint(i) scanf("%d",&i)
#define ss(s) scanf("%s",s)
#define pii pair<int,int>
#define ll long long
#define MAX 1000000000
#define MOD 1000000007
int main()
{
    freopen("test.in", "r", stdin);
freopen("file.out", "w", stdout);
    int test;
    sint(test);
    int l,x;
    char arr[10010];
    char s[10010];
    pii dp[10010];
    int mat[5][5]={0,0,0,0,0,0,1,2,3,4,0,2,-1,4,-3,0,3,-4,-1,2,0,4,3,-2,-1};
    map<char,int> mymap;
    mymap['i']=2;
    mymap['j']=3;
    mymap['k']=4;
    int top,i,j,last;
    for(int t=1;t<=test;t++)
    {
        sint(l);
        sint(x);
        ss(s);
        top=0;
        for(i=0;i<x;i++)
        {
            for(j=0;s[j];j++)
            {
                arr[top++]=s[j];
            }
        }
        dp[0].first=1;
        dp[0].second=1;
        last=0;
        for(i=1;i<=top;i++)
        {
            dp[i].first=mat[dp[i-1].first][mymap[arr[i-1]]]*dp[i-1].second;
            if(dp[i].first<0)
            {
                dp[i].first=dp[i].first*(-1);
                dp[i].second=-1;
            }
            else
            dp[i].second=1;
            if(dp[i].first*dp[i].second==4)
            {
                last=i;
            }
           // cout<<arr[i-1]<<" "<<dp[i].first*dp[i].second<<"\n";
        }
        if(dp[top].first*dp[top].second!=-1)
        {
            printf("Case #%d: NO\n",t);
            continue;
        }
        for(i=1;i<last;i++)
        {
            if(dp[i].first*dp[i].second==2)
            {
                printf("Case #%d: YES\n",t);
                goto out;
            }
        }
        printf("Case #%d: NO\n",t);
        out:
        ;
    }
    return 0;
}
