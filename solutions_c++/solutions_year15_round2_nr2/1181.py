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
int dp[1000005];
int solve(int r,int c, int x)
{
    int ret = 0,i,j;
    f(i,0,r)
        f(j,0,c)
            {
                if((i > 0 && (x & (1<<(i * c + j))) && (x & (1<< ((i-1)*c + j)))))
                    ret++;
                if((j > 0 && (x & (1<<(i * c + j))) && (x & (1<< (i*c + j-1)))))
                    ret++;
            }
    return ret;
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("o.out","w",stdout);
    #endif
    int t,r,c,n,i,j,sol;
    sc(t);
    f(j,0,t)
    {
        sc(r); sc(c); sc(n);
        sol = r*c*n*(1<<7);
        f(i,1,1<<(r*c))
        {
            dp[i] = dp[i - (i& -i)] + 1;
            if(dp[i] == n)
                sol = min(sol,solve(r,c,i));
        }
        printf("Case #%d: %d\n",j+1, sol);
    }
    return 0;
}
