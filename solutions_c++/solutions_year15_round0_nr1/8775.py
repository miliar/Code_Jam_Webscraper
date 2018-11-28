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
#define pr(a) cout<<#a<<" = "<<(a)<<endl
#define sz(a) int((a).size())
#define all(a) a.begin(),a.end()
#define loop(x,a,b) for(int (x) = (a);(x)<(b);(x)++)
#define rep(x,n)   for(int (x)=0;(x)<(n);(x)++)
#define tr(c,it) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define prc(a) tr(a, it) cout<<*(it)<<" "; cout<<endl
#define pra(a,n) for(int i=0; i<(n); i++) cout<<((a)[i])<<" "; cout<<"\n"
#define prdd(a,r,c) for(int i=0;i<(r);i++) { for(int j = 0;j<(c);j++) cout<<a[i][j]<<" "; cout<<endl; } cout<<endl; 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define ain(a,n) int ((a)[(n)]); for(int i=0; i<(n); i++) cin>>((a)[i])  
#define md 1000000007
#define MAXN 200005

int pain()
{
	int num = 0, sum = 0, smax;
	vi a;
	string str;
	cin>>smax;
	cin>>str;
	rep(i,str.length())
		a.pb((int)(str[i] - '0'));
	rep(i,smax+1)
	{
		if(sum < i)
		{
			num += (i-sum);
			a[i] += (i-sum);
		}
		sum += a[i];
	}

	return num;


}

int main()
{   
    ios::sync_with_stdio(false);
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int t;	
	cin>>t;
	rep(i,t)
		cout<<"Case #"<<i+1<<": "<<pain()<<"\n";
    return 0;
}
