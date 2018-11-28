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
   //  freopen("B-small-attempt0.in","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("16qBout.txt","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        string s;
        cin>>s;u=1;
        v=s.length();
        for(i=0;i+1<v;i++)
            if(s[i]!=s[i+1])u++;
        j=s[0]=='+'?0:1;
        if(u==1)
        {
            if(j==0)ans=0;
            else ans=1;
        }
        else{
            if(u%2==0)
            {
                if(j==0)ans=u;
                else ans=u-1;
            }
            else
            {
                if(j==1)ans=u;
                else ans=u-1;
            }
        }
        printf("Case #%d: %d\n",++cs,ans);
    }
    return 0;

}