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

int main()
{
	int n, ans;
	string str;
	vector<int> vec;
	fin>>n;
	rep(i, 0, n-1)
	{
		fin>>str;
		vec.clear();
		rep(i, 0, sz(str) - 1)
		{
			if(i != 0)
			{
				if(str[i] == '+' && str[i-1] == '-')
					vec.pb(1);
				else
					if(str[i] == '-' && str[i-1] == '+')
						vec.pb(0);
			}
			else
			{
				if(str[i] == '+')
					vec.pb(1);
				else
					vec.pb(0);
			}
		}

		ans = 0; 
		if(vec[0] == 0)
			ans++;
		rep(i, 0, sz(vec) - 2)
		{
			if(vec[i] == 1 && vec[i+1] == 0)
				ans += 2;
		}

		fout<<"Case #"<<i+1<<": "<<ans<<"\n";
	}
	return 0;
}
