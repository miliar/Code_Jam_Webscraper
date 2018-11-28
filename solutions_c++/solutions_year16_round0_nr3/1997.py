#include<bits/stdc++.h>
using namespace std;

#define pb push_back
#define ff first
#define ss second
#define mpr make_pair
#define all(a) a.begin(),a.end()
#define Sz(a) a.size()
#define ii pair<int,int>


#define ll long long
#define inf 1000000009
#define mod 1000000007

#define rep(i,n)    for(i=0;i<(n);i++)
#define foro(i,n)   for(i=1;i<=(n);i++)
#define repe(i,a,b) for(i=(a);i<=(b);i++)
#define repr(i,a,b) for(i=(a);i>=(b);i--)
int cs,n,m,ans;

int main()
{
    int i,j,k,T,u,v;
     //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-large.in","r",stdin);
    freopen("16qCout.txt","w",stdout);
    ll pow[11][20];
    for(i=2;i<=10;i++)pow[i][0]=1;
    for(i=2;i<=10;i++)
        for(j=1;j<17;j++)
            pow[i][j]=pow[i][j-1]*i;
    scanf("%d",&T);
    string s="00000000";s+=s;s+=s;
    int cnt=0,h=16,hh=32,tot=500;
    while(T--)
    {
        //cin>>n>>v;
        printf("Case #%d:\n",++cs);
        //n=16;j=50;

        for(i=1;i<h-2;i++)
        for(j=i+1;j<h-1;j++)
        for(k=j+1;k<h;k++)
        {
            for(u=0;u<hh;u++)s[u]='0';
            s[0]='1';s[hh-1]='1';

            s[i]='1';
            s[j]='1';
            s[k]='1';
            s[hh-1-k]='1';
            s[hh-1-k+i]='1';
            s[hh-1-k+j]='1';

            reverse(s.begin(),s.end());
            cout<<s<<" ";
            for(u=2;u<11;u++)printf("%lld ",pow[u][i]+pow[u][j]+pow[u][k]+1);
            puts("");
            cnt++;
            if(cnt>=tot){i=j=k=h;}
        }
        //for(i=1;i<h-2;i++)
        for(j=1;j<h-1;j++)
        for(k=j+1;k<h;k++)
        {
            for(u=0;u<hh;u++)s[u]='0';
            s[0]='1';s[hh-1]='1';

           // s[i]='1';
            s[j]='1';
            s[k]='1';
            s[hh-1-k]='1';
            //s[hh-1-k+i]='1';
            s[hh-1-k+j]='1';

            reverse(s.begin(),s.end());
            cout<<s<<" ";
            for(u=2;u<11;u++)printf("%lld ",pow[u][j]+pow[u][k]+1);
            puts("");
            cnt++;
            if(cnt>=tot){k=j=h;}
        }


    }
    return 0;

}