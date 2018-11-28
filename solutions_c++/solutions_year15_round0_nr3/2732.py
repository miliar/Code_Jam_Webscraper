#include<bits/stdc++.h>
using namespace std;
int func(char ch)
{
    if(ch=='1')
        return 0;
    if(ch=='i')
        return 1;
    if(ch=='j')
        return 2;
    if(ch=='k')
        return 3;
}
int main()
{
    freopen("inp.in","r",stdin);
    freopen("out.txt","w",stdout);
    int n,t,l,x,c=1,flag,j,k,i,a[4][4]={{0,1,2,3},{1,0,3,2},{2,3,0,1},{3,2,1,0}},sgn[4][4]={{0,0,0,0},{0,1,0,1},{0,1,1,0},{0,0,1,1}},dp[100001],dps[100001];
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d %d",&l,&x);
        string s,str;
        cin>>str;
        s="";
        for(i=1;i<=x;i++)
            s=s+str;
        //cout<<s;
        n=l*x;
        dp[0]=func(s[0]);
        dps[0]=0;
        for(i=1;i<n;i++)
        {
            dp[i]=a[dp[i-1]][func(s[i])];
            if((dps[i-1]==1&&sgn[dp[i-1]][func(s[i])]==1)||(dps[i-1]==0&&sgn[dp[i-1]][func(s[i])]==0))
                dps[i]=0;
            else
                dps[i]=1;
        }
        for(i=0;i<n;i++)
            if(dp[i]==1&&dps[i]==0)
                break;
        if(i==n)
        {
            printf("Case #%d: NO\n",c);
            c++;
            continue;
        }
        for(i=i+1;i<n-1;i++)
            if(dp[i]==3&&dps[i]==0&&dp[n-1]==0&&dps[n-1]==1)
                break;
        if(i==n-1)
        {
            printf("Case #%d: NO\n",c);
            c++;
        }
        else
        {
            printf("Case #%d: YES\n",c);
            c++;
        }
    }
    return 0;
}
