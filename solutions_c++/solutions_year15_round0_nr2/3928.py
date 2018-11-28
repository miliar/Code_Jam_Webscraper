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
#define sc(n) scanf("%d",&n)
//#define gc getchar_unlocked
//void sc(int &x){register int c = gc();x = 0;int neg = 0;for(;((c<48 || c>57) && c != '-');c = gc());if(c=='-') {neg=1;c=gc();}for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}if(neg) x=-x;}
//#define pc(x) putchar_unlocked(x)
//void prc(int n){int N = n, rev, count = 0;rev = N;if (N == 0) { pc('0'); pc('\n'); return ;}while ((rev % 10) == 0) { count++; rev /= 10;} rev = 0;while (N != 0) { rev = (rev<<3) + (rev<<1) + N % 10; N /= 10;}while (rev != 0) { pc(rev % 10 + '0'); rev /= 10;}while (count--) pc('0');}
#define vi vector<int>
vi a(10);
map<vi,int>mp;
int solve(vi a, int s)
{
    if(s == 1)
        if(a[s] == 0)   return 0;
        else return 1;
    if(mp.find(a) != mp.end())  return mp[a];

    int t1 = s, t2 = maxx;
    vi temp = a;
    if(a[s] > 0)
    {
        a[s]--;
        int k;
        f(k,1,s)
        {
            a[k]++,a[s-k]++;
            t2 = min(t2,1 + solve(a,s));
            a[k]--,a[s-k]--;
        }
        a[s]++;
    }
    else
        t2 = solve(a,s-1);

    return mp[temp] = min(t1,t2);
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("inp.in","r",stdin);
    freopen("out.out","w",stdout);
    #endif
    int t,n,j,i,o;
    sc(t);
    f(j,0,t)
    {
        f(i,0,sz(a))
            a[i] = 0;
        sc(n);
        f(i,0,n)
            {
                sc(o);
                a[o]++;
            }
        printf("Case #%d: %d\n",j+1,solve(a,sz(a)-1));
    }
    return 0;
}
