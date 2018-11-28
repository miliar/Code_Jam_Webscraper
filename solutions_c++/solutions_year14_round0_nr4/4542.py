#include<cstdio>
#include<iostream>
#include<vector>
#include<cstring>
#include<algorithm>
#include<set>
#include<queue>
#include<cmath>
#include<bitset>
#include<map>
#define test(t) while(t--)
#define cin(n) scanf("%d",&n)
#define cinl(n) scanf("%lld",&n)

#define cout(n) printf("%d\n",n)
#define rep(i,a,n) for(i=a;i<=n;i++)
#define vi vector<int>
#define vii vector< vector<int> >
#define vpii vector< pair<int,int> >
#define mii map<int,int>
#define eps 1e-12
#define pb push_back
#define mp make_pair
#define imax (int) 1000000007
#define ill long long
#define gc getchar_unlocked
#include<stack>
using namespace std;
#define mod 1000000009
#define inf 10000000
#include <cstdio>
#include <algorithm>

using namespace std;

ill powe(int aa,int b)
{
    ill ans=1;
    ill a=aa*1LL;
    while(b)
    {
        if(b&1)
            ans=(ans*1LL*a)%mod;
        a=(a*1LL*a)%mod;
        b=b/2;
    }
    return ans;
}
ill modinv(int a)
{
    return powe(a,mod-2);
}
#define eps 1e-12
#define gc getchar_unlocked
//int fcin(){register int c = gc();int x = 0;for(;(c<48 || c>57);c = gc());for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}return x;}


int gcd(int i,int j)
{
    if(j==0)
        return i;

    return gcd(j,i%j);
}


/*void scanint(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}*/


bool comp(double a,double b)
{
    return (a+eps)<b;
}

int main()
{
    int n,t,i,j,l,p,m,k;
    //freopen("a.in","r",stdin);
    //freopen("c.out","w",stdout);

    cin(t);
    int ct=1;
    while(t--)
    {
        cin(n);
        //memset(dp,-1,sizeof(dp));
        double a[n+9],b[n+9];
        for(i=0;i<n;i++)
            cin>>(a[i]);
        for(i=0;i<n;i++)
            cin>>(b[i]);

        sort(a,a+n,comp);
        sort(b,b+n,comp);

        j=0;
        int ans=0,ans2=0;
        for(i=0;i<n;i++)
        {
            int fg=0;
            while(j<=(n-1))
            {
                if(a[j]>b[i])
                {
                    fg=1;
                    break;
                }
                j++;
            }
            if(fg)
                ans++;
            j++;
        }
        j=0;
        for(i=0;i<n;i++)
        {
            int fg=0;
            while(j<=(n-1))
            {
                if(b[j]>a[i])
                {
                    fg=1;
                    break;
                }
                j++;
            }
            if(!fg)
                ans2++;
            j++;
        }

        cout<<"Case #"<<ct++<<": ";
        cout<<ans<<" "<<ans2<<"\n";
    }
    return 0;
}
