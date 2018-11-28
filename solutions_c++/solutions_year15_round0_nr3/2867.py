#include<bits/stdc++.h>
using namespace std;

map< char, int > mp;
int a[4][4]={{0,1,2,3},{1,0,3,2},{2,3,0,1},{3,2,1,0}},sgn[4][4]={{0,0,0,0},{0,1,0,1},{0,1,1,0},{0,0,1,1}};
int dp[100005],dps[100005];

int main()
{
    freopen("inp.in","r",stdin);
    freopen("out.txt","w",stdout);
    int n,t,l,x,T,flag,j,k,i;
    mp['1']=0; mp['i']=1; mp['j']=2; mp['k']=3;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d%d",&l,&x);
        string s,str;
        cin>>str;
        s="";
        for(i=1;i<=x;i++)
            s=s+str;
        n=l*x;
        dp[0]=mp[s[0]];
        dps[0]=0;
        for(i=1;i<n;i++)
        {
            dp[i]=a[dp[i-1]][ mp[s[i]] ] ;
            if((dps[i-1]==1&&sgn[dp[i-1]][mp[s[i]]]==1)||(dps[i-1]==0&&sgn[dp[i-1]][mp[s[i]]]==0))
                dps[i]=0;
            else
                dps[i]=1;
        }
        for(i=0;i<n;i++)
            if(dp[i]==1&&dps[i]==0)
                break;
        if(i==n)
        {
            printf("Case #%d: NO\n",t);
            continue;
        }
        for(i=i+1;i<n-1;i++)
            if(dp[i]==3&&dps[i]==0&&dp[n-1]==0&&dps[n-1]==1)
                break;
        if(i==n-1)
            printf("Case #%d: NO\n",t);
        else
            printf("Case #%d: YES\n",t);
    }
    return 0;
}

