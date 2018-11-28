#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef vector<pii > vii;
typedef vector<pair<int, pair<int, int> > > viii;
typedef pair<ll,ll> pll;
typedef vector<string> vs;
typedef vector<vii> vvii;

#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define MEM(a,b) memset(a,(b),sizeof(a))
#define tr(c,it) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define all(a) a.begin(),a.end()
#define loop(x,a,b) for(int (x) = (a);(x)<(b);(x)++)
#define rep(x,n)   for(int (x)=0;(x)<(n);(x)++)
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define ain(a,n) int ((a)[(n)]); for(int i=0; i<(n); i++) cin>>((a)[i])  
#define md 1000000007
#define MAXN 200005

void solve()
{
	int n, res = 1;
	string s;
	cin >> s;
	n = s.length();
	for(int i = 1 ; i < n ; i++)
	{
		if(s[i] != s[i-1])
			res++;
	}
	if(s[n-1] == '+')
		res--;

	cout << res << endl;

}

int main()
{   
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    rep(tt,t)
    {
    	cout << "Case #" << tt+1 << ": ";
    	solve();
    }
    return 0;
}
