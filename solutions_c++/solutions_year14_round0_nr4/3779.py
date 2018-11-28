//0000000000000000000000000000//
//%%%%   Archit Srivastava %%%//
//        NIT Durgapur        //
//0000000000000000000000000000//
#include<bits/stdc++.h>
using namespace std;
#define PB push_back
#define MP make_pair
#define clr(x) x.clear()
#define sz(x) ((int)(x).size())
#define F first
#define S second
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,b) for(i=0;i<b;i++)
#define rep1(i,b) for(i=1;i<=b;i++)
#define mod 1000000007
#define pi(n) printf("%d",n)
#define pin(n) printf("%d\n",n)
#define piw(n) printf("%d ",n)
#define pll(n) printf("%lld",n)
#define plln(n) printf("%lld\n",n)
#define pllw(n) printf("%lld ",n)
#define sll(n) scanf("%lld",&n)
#define ss(s) scanf("%s",s)
#define ps(s) printf("%s",s)
#define psn(s) printf("%s\n",s)
#define psw(s) printf("%s ",s)
#define si(n) scanf("%d",&n)
#define pn printf("\n")
#define pw printf(" ")
#define PI (3.141592653589793)
#define MAX_SIZ 1000005
/*
inline int ri()
{
    int n=0;char c;
    while(1)
    {
        c=getchar_unlocked();
        if(c=='\n'||c==' '||c==EOF)break;
        n=(n<<3) + (n<<1) +c-48;
    }
    return n;
}
inline long long rll()
{
    long long n=0;
    char c;
    while(1)
    {
        c=getchar_unlocked();
        if(c=='\n'||c==' '||c==EOF)break;
        n=(n<<3) + (n<<1) + c - 48;
    }
    return n;
}
*/
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

int main()
{
    int t,z;
    si(t);
    z=t;
    while(t--)
    {
        int n,i;
        si(n);
        double a[1005],b[1005];
        rep(i,n)
        {
            cin>>a[i];
        }
        rep(i,n)
        {
            cin>>b[i];
        }
        sort(a,a+n);sort(b,b+n);
        int an1=0,an2=0,j=0,ind1=0,ind2;
        for(i=0,j=0;i<n&&j<n;)
        {
            if(b[i]<a[j])
            {
                an1++;
                i++;
                j++;
            }
            else
            {
                j++;
            }
        }
        j=0;
        for(i=0,j=0;i<n&&j<n;)
        {
            if(a[i]<b[j])
            {
                an2++;
                i++;
                j++;
            }
            else
            {
                j++;
            }
        }
        printf("Case #%d: ",z-t);
        piw(an1);pin(n-an2);
    }
}
