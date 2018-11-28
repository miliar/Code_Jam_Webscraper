#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define dbg(x) cout<<#x<<": "<<x<<endl
#define dbgv(x,i) cout<<#x<<"["<<i<<"]: "<< x[i]<<endl
#define maxx 99999999
#define minn -99999999
#define PB push_back
#define MP make_pair
#define ff first
#define ss second
#define mod 1000000007
#define f(i,a,b) for(i = a; i < b; i++)
#define sz(a) int((a).size())
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define pii pair< int,int >
#define sc(n) scanf("%lld",&n)
//#define gc getchar_unlocked
//void sc(int &x){register int c = gc();x = 0;int neg = 0;for(;((c<48 || c>57) && c != '-');c = gc());if(c=='-') {neg=1;c=gc();}for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}if(neg) x=-x;}
//#define pc(x) putchar_unlocked(x)
//void prc(int n){int N = n, rev, count = 0;rev = N;if (N == 0) { pc('0'); pc('\n'); return ;}while ((rev % 10) == 0) { count++; rev /= 10;} rev = 0;while (N != 0) { rev = (rev<<3) + (rev<<1) + N % 10; N /= 10;}while (rev != 0) { pc(rev % 10 + '0'); rev /= 10;}while (count--) pc('0');}
ll arr[5][5]={0,0,0,0,0,0,1,2,3,4,0,2,-1,4,-3,0,3,-4,-1,2,0,4,3,-2,-1};
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("inp.in","r",stdin);
    freopen("out3.out","w",stdout);
    #endif
    ll t,j,l,x,an,tot;
    sc(t);
    char s[10005];
    f(j,0,t)
    {
        ll t1 = 0, t2 = 0, t3 = 0, n = 0;
        sc(l);sc(x);
        tot = l * x;
        scanf("%s",s);
        ll i,k;
        an = s[0] - 'i' + 2;
        if(an < 0)  {an = -an; if(!n) n = 1; else n = 0;}
        if(an == 2 && !t1 && !n)    {t1 = 1; an = 1;}
        f(i,1,tot)
        {
            k = i % l;
            an = arr[an][s[k]-'i'+2];
            if(an < 0)  {an = -an; if(!n) n = 1; else n = 0;}
            if(an == 2 && !t1 && !n)    {t1 = 1;an =1;}
            else if(an == 3 && t1 == 1 && !t2 && !n)    {t2 = 1; an = 1;}
            else if(an == 4 && t1 == 1 && t2 == 1 && !t3 && !n)   {t3 = 1;i++;an = 1; break;}
        }
        if(t3 == 1)
        {
            an = 1;
            for(;i < tot;i++)
            {
                k = i % l;
                an = arr[an][s[k] - 'i' + 2];
                if(an < 0)  {an = -an; if(!n) n = 1; else n = 0;}
            }
            if(an == 1 && !n) printf("Case #%lld: YES\n",j+1);
            else    printf("Case #%lld: NO\n",j+1);
        }
        else
            printf("Case #%lld: NO\n",j+1);
    }
    return 0;
}
