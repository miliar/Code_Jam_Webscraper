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

int main()
{
    int t,i,j,l,n,m,k;
    //freopen("a.in","r",stdin);
    //freopen("b.out","w",stdout);
    freopen("a.in","r",stdin);
    freopen("b.out","w",stdout);

    cin(t);
    int ct=1;
    while(t--)
    {
        cin(n);
        int a[5][5],b[5][5],ma[18];
        memset(ma,0,sizeof(ma));
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                cin(a[i][j]);
                if(i==n)
                    ma[a[i][j]]++;
            }
        }
        cin(m);

        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {

                cin(b[i][j]);
                if(i==m)
                    ma[b[i][j]]++;
            }
        }
        int c=0,ans;
        for(i=1;i<=16;i++)
        {
            if(ma[i]==2)
            {
                c++;
                ans=i;
            }
        }
        cout<<"Case #"<<ct++<<": ";
        if(c==1)
        {
            cout<<ans<<"\n";
        }
        else if(c>1)
        {
            cout<<"Bad magician!\n";
        }
        else
            cout<<"Volunteer cheated!\n";
    }
    return 0;
}
