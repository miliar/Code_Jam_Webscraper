#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define vi vector<int>
#define pii pair<int,int>
#define vii vector<pii>
#define rep(i,n) for(int i = 0; i < n; i++)
#define rp(i,a,n) for(int i=a;i<=int(n);i++)
#define IT(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define all(x) (x).begin(), (x).end()
#define ll long long
#define sc(x) scanf("%d", &x)
#define oo 1000
#define fill(a,b) memset(a,b,sizeof a)
#define F first
#define S second
#define mod 1000000007
#define N 10005
int dh[4] = {0, 1, 0, -1};
int dv[4] = {-1, 0, 1, 0};
using namespace std;

ll n,i,ok,a[20];
void check(int x)
{
    while(x)
    {
        a[x%10]=1;
        x/=10;
    }
    int ind=1;
    rep(i,10) if(!a[i]) ind=0;
    ok=ind;
}
int main()
{
    freopen("lol.in","r",stdin);
    freopen("lol.out","w",stdout);
    int t;
    cin >> t;
    rp(tt,1,t)
    {
        cin >> n ;
        if(n==0) { printf("Case #%d: INSOMNIA\n",tt);;continue; }
        rep(i,20) a[i]=0;ok=0;i=0;
        while(!ok)
        {
            i++;
            check(i*n);
        }
        printf("Case #%d: %lld\n",tt,(ll)i*n);
    }


}
