#include <bits/stdc++.h>
 
using namespace std;
 
#define ll long long int
#define pb push_back
#define mp make_pair
#define INF (ll)(1e18)
#define inf 0x7fffffff
#define inff 100000
#define ff first
#define ss second
#define sz(x) ((int) (x).size())
#define fast cin.sync_with_stdio(0);cin.tie(0)
#define rep(i,N) for(int i = 0;i < N;i++)
#define frep(i,a,b) for(int i = a;i <= b;i++)
#define pii pair<int , int>
#define pll pair<ll , ll>
#define vii vector<int>
#define vpii vector< pii >
#define fill(A,v) memset(A,v,sizeof(A))
#define setbits(x) __builtin_popcount(x)
#define print(A,j,k) for(int ii=j;ii<=k;ii++)cout<<A[ii]<<" ";cout<<"\n"
#define all(x) (x).begin(), (x).end()
#define gcd __gcd
#define SQRT 350
#define CASES int t;cin>>t;while(t--)
#define FILE freopen("inp.txt" , "r" , stdin);
#define ld long double

const int N = 3e5 + 5;
const ll MOD = 1e9 + 7;
const ll INV2 = 500000004;

int main() {
    fast;

    freopen("gcj_input.txt" , "r" , stdin);
	freopen("gcj_output.txt" , "w" , stdout);
	int t;
    cin >> t;
    for (int ii = 1; ii <= t; ++ii) {
        cout << "Case #" << ii << ": ";
        ll k, c, s;
        cin >> k >> c >> s;
        ll kc = 1;

        frep(i , 1 , c)
        	kc *= k;
        
        kc /= k;
        
        ll x = 1;
        frep(i , 1 , s) {
            cout << x << " ";
            x += kc;
        }
        cout << '\n';
    }
    return 0;
}







