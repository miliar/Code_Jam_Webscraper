#include <algorithm>
#include <string>
#include <stdio.h>
#include <iostream>
#include <vector>
#include <math.h>
using namespace std;
#define rep(i,a,b) for(int i=(a);i<(b);i++)
#define repm(i,a,b) for(int i=(a);i>(b);i--)
#define f(i,n) rep(i,0,n)
#define pin(n) printf("%d\n",n)
#define si(n) scanf("%d",&n)
#define sii(m,n) scanf("%d %d",&m,&n)
#define pb push_back
#define ff first
#define ss second
typedef long long ll;
#define mod 1000000007

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);

    int q;
    si(q);
    f(t,q)
    {
        string s;
        cin>>s;
        vector<int> a(26,0),c(10,0);
        int l=s.size();
        f(i,l)
        {
            a[s[i]-65]++;
        }
        c[2]=a[22];
        c[4]=a[20];
        c[6]=a[23];
        c[8]=a[6];
        c[0]=a[25];
        a[14]-=c[2]+c[4]+c[0];
        a[7]-=c[8];
        a[5]-=c[4];
        a[18]-=c[6];
        c[1]=a[14];
        c[3]=a[7];
        c[5]=a[5];
        c[7]=a[18];
        c[9]=a[8]-c[5]-c[6]-c[8];
        cout<<"Case #"<<t+1<<": ";
        f(i,10)
        f(j,c[i])
        cout<<i;
        cout<<endl;
    }
}


































