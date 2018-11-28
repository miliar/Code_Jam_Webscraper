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
	ll n, temp, n1;
	set<int> s;
	cin >> n;
	if(n == 0)
	{
		cout << "INSOMNIA" << endl;
		return;
	}
	n1 = temp = n;
	int cnt = 0;
	while(1)
	{
		// cout << "D";
		cnt++;
		if(cnt > 1000000)
		{
			cout << "INSOMNIA" << endl;
			return;
		}	
		n = temp;
		while(n)
		{
			s.insert(n%10);
			n /= 10;
		}
		if(s.size() == 10)
		{
			cout << temp << endl;
			return;
		}
		else
		{
			temp += n1;		
		}
	}
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
