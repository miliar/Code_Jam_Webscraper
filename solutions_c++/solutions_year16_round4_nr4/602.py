#include<bits/stdc++.h>
using namespace std;
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define ll long long
#define pli pair<ll,int>
#define pil pair<int,ll>
#define pll pair<ll,ll>
#define all(v) v.begin(),v.end()
#define inf 1000000000
int a[100][100],b[100][100];
vector< vector<int> >s;
int func(int x,int y,int n)
{
    vector<int>v,v1;
    int i,j;
    for(i=0; i<n; i++)
        if(i!=x)
            v.pb(i);
    for(i=0; i<n; i++)
        if(i!=y)
            v1.pb(i);

    for(i=0; i<s.size(); i++)
    {
        for(j=0; j<s[i].size(); j++)
        {
            if(!b[v[s[i][j]]][v1[j]])
                break;
        }
        if(j==s[i].size())
            return 0;
    }
    return 1;
}
int check(int n)
{
    int i,j,k;
    for(i=0; i<n; i++)
    {
        for(j=0; j<n; j++)
        {
            if(b[i][j]==0)
            {
                //cout<<i<<" "<<j<<" "<<func(i,j,n)<<endl;
                if(!func(i,j,n))
                    return 0;
            }
        }
    }
    for(i=0; i<n; i++)
    {
        int c=0;
        for(j=0; j<n; j++)
            c+=b[i][j];
        if(c==0)
            return 0;
    }
    for(i=0; i<n; i++)
    {
        int c=0;
        for(j=0; j<n; j++)
            c+=b[j][i];
        if(c==0)
            return 0;
    }

    return 1;
}
int dp[200][200];
int check1(int n)
{
    int i,j,k,l;
    for(i=0; i<s.size(); i++)
    {
        for(j=0; j<(1<<n); j++)
            dp[0][j]=0;
        dp[0][0]=1;
        for(j=0; j<n; j++)
        {
            for(k=0;k<(1<<n);k++)
                dp[j+1][k]=0;
            for(k=0; k<(1<<n); k++)
            {
                if(dp[j][k]==0)
                    continue;
                int c=0;
                for(l=0; l<n; l++)
                {
                    //cout<<i<<" "<<j<<" "<<l<<" "<<k<<" "<<c<<" "<<(k&(1<<l))<<endl;
                    if(b[s[i][j]][l]==1&&((k&(1<<l))==0))
                        c=1,dp[j+1][k|(1<<l)]=1;
                }
                if(c==0)
                    return 0;
            }
//            printf("%d %d\n",i,j);
//            for(k=0;k<(1<<n);k++)
//                printf("%d ",dp[j+1][k]);
//            printf("\n");
        }
    }
    return 1;
}
vector< pii >v;
int main()
{
    freopen("1.in","r",stdin);
    freopen("1-out.txt","w",stdout);
    int t,cs=1;
    scanf("%d",&t);
    while(t--)
    {
        int n,i,j,k,c=0;
        scanf("%d",&n);
        for(i=0; i<n; i++)
        {
            string s;
            cin>>s;
            for(j=0; j<n; j++)
                if(s[j]=='0')
                    a[i][j]=0;
                else
                    c=1,a[i][j]=1;
        }
        if(c==0)
        {
            printf("Case #%d: %d\n",cs,n);
            cs++;
            continue;
        }
        vector<int>v1;
        for(i=0; i<n; i++)
            v1.pb(i);
        s.clear();
        do
        {
            s.pb(v1);
        }
        while(next_permutation(all(v1)));
        v.clear();
        for(i=0 ;i<n; i++)
        {
            for(j=0; j<n; j++)
                if(a[i][j]==0)
                    v.pb(mp(i,j));
        }
        int sz=v.size(),ans=sz;
        for(i=0; i<(1<<sz); i++)
        {
            for(j=0; j<n; j++)
                for(k=0; k<n; k++)
                    b[j][k]=a[j][k];
            for(j=0; j<sz; j++)
                if((i>>j)&1)
                    b[v[j].f][v[j].s]=1;
//            if(i==0)
//            {
//                for(int i=0;i<n;i++)
//                {
//                    for(int j=0;j<n;j++)
//                        printf("%d ",b[i][j]);
//                    printf("\n");
//                }
//            }
            if(check1(n))
                ans=min(ans,(int)__builtin_popcount(i));
        }
        printf("Case #%d: %d\n",cs,ans);
        cs++;
    }
    return 0;
}
