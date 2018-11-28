#include <bits/stdc++.h>
using namespace std;
#define MEM(a) memset(a,0,sizeof(a))
#define rp(i,a,n) for ( i=a;i<n;i++)
#define pr(i,a,n) for ( i=n-1;i>=a;i--)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x).size())
#define F first
#define S second
#define IT(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define MAX 105000
typedef vector<int> vi;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<pii> vii;
typedef vector<ll> vll;
const ll mod=1000000007;
int dr[8] = {1,1,0,-1,-1,-1, 0, 1};
int dc[8] = {0,1,1, 1, 0,-1,-1,-1};
int dh[4] = {0, 1, 0, -1};
int dv[4] = {-1, 0, 1, 0};
int t[500][500];
void solve(int pp)
{
    int n,i,j;
    cin>>n;
    vector<int> v(10,0);vector<int> t(10,1);
    rp(i,1,1001)
    {
        int p=i*n;
        do
        {
            v[p%10]=1;
            p=p/10;
        }
        while(p);
        if(v==t) break;
    }
    if(i>1000) cout<<"Case #"<<pp<<": INSOMNIA"<<endl;
    else cout<<"Case #"<<pp<<": "<<i*n<<endl;
}
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;cin>>t;
    int qq; rp(qq,1,t+1)
    {
        solve(qq);
    }
    return 0;
}
