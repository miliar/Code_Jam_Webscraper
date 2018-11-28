#include<bits/stdc++.h>
using namespace std;

map< char, int > m;
int A[4][4]={{0,1,2,3},{1,0,3,2},{2,3,0,1},{3,2,1,0}},sign[4][4]={{0,0,0,0},{0,1,0,1},{0,1,1,0},{0,0,1,1}};
int dp[100005],dp2[100005];

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("test.txt","w",stdout);
    int n,b,l,x,t,flag,j,k,i;
    m['1']=0; m['i']=1; m['j']=2; m['k']=3;
    scanf("%d",&t);
    for(b=1;b<=t;b++)
    {
        scanf("%d%d",&l,&x);
        string str;
        cin>>str;
        n=l*x;
        dp[0]=m[str[0]];
        dp2[0]=0;
        for(i=1;i<n;i++)
        {
            dp[i]=A[dp[i-1]][ m[str[i%l]] ] ;
            if((dp2[i-1]==1&&sign[dp[i-1]][m[str[i%l]]]==1)||(dp2[i-1]==0&&sign[dp[i-1]][m[str[i%l]]]==0))
                dp2[i]=0;
            else
                dp2[i]=1;
        }
        for(i=0;i<n;i++)
            if(dp[i]==1&&dp2[i]==0)
                break;
        if(i==n)
        {
            printf("Case #%d: NO\n",b);
            continue;
        }
        for(i=i+1;i<n-1;i++)
            if(dp[i]==3&&dp2[i]==0&&dp[n-1]==0&&dp2[n-1]==1)
                break;
        if(i==n-1)
            printf("Case #%d: NO\n",b);
        else
            printf("Case #%d: YES\n",b);
    }
    return 0;
}

