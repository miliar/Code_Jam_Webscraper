#include <bits/stdc++.h>

#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define LET(x,a) __typeof(a) x(a)
#define tr(v,it) for( LET(it,v.begin()) ; it != v.end() ; it++)
#define rtr(v,it) for( LET(it,v.rbegin()) ; it != v.rend() ; it++)
#define present(x,c) ((c).find(x) != (c).end())    //stl container find
#define cpresent(x,c) (find(all(c),x) != (c).end())       //standard library find
#define sorti(a) sort(a.begin(),a.end())
#define sortd(a) sort(a.rbegin(),a.rend())
 
#define MEM(a,b) memset(a,b,sizeof(a))
#define rep(i,st,en) for(int i=(int)st; i<=(int)en;i++)
#define rrep(i,st,en) for(int i=(int)st; i>=(int)en;i--)
#define sd(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define pf(x) printf("%s",x)
#define deb(x) cerr<<">value ("<<#x<<") : "<<x<<endl;
#define mod 1000000007

using namespace std;

ofstream fout("testout.txt");
ifstream fin("testin.txt");

typedef long long int ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;

ll func(ll base, ll up)
{
	ll ans = 0, add = 1;
	rep(i, 1, up - 1)
	{
		add *= base;
		ans += add;
	}
	return ans;
}

int main()
{
	int t;
	ll k, c, s;
	fin>>t;
	rep(j, 1, t)
	{
		fin>>k>>c>>s;
		fout<<"Case #"<<j<<": ";
		for(ll i = 1; i <= s; i++)
		{
			fout<<i + (i - (ll)1) * func(k, c)<<" ";
		}
		fout<<"\n";
	}
	return 0;
}
