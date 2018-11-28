#include <bits/stdc++.h>
using namespace std;
#define PB push_back
#define MP make_pair
#define FST first
#define SEC second
#define SZ(a) (int)(a.size())
#define CLR(a) a.clear()
#define SET(a,b) memset(a,b,sizeof(a))
#define LET(x,a) __typeof(a) x(a)
#define TR(v,it) for( LET(it,v.begin()) ; it != v.end() ; it++)
#define REP(i,n) for(int i=0; i<(int)n;i++)
#define si(n) scanf("%d",&n)
#define sll(n) scanf("%lld",&n)
#define pi(n) printf("%d",n)
#define piw(n) printf("%d ",n)
#define pin(n) printf("%d\n",n)
#define SORT(a) sort(a.begin(),a.end())
#define all(a) a.begin(),a.end()
#define endl "\n"

#define TRACE

#ifdef TRACE
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

#else

#define trace1(x)
#define trace2(x, y)
#define trace3(x, y, z)
#define trace4(a, b, c, d)
#define trace5(a, b, c, d, e)
#define trace6(a, b, c, d, e, f)

#endif


typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector< PII > VPII;


int solve()
{
	int m;
	cin>>m;
	string s;
	cin>>s;
	int standCount = 0;
	int res = 0;
	REP(i, s.length())
	{
		if( (s[i]-'0') == 0 ) continue;
		if(standCount >= i)
		{
			standCount += (s[i] - '0');
			continue;
		}
		int diff = (i - standCount);
		// trace3(i, standCount, diff);
		res += diff;
		// cout<<"adding "<<(i - standCount)<<endl;
		standCount += diff;
		standCount += ( s[i] - '0');
	}
	return res;
}


int main()
{
	ios::sync_with_stdio(false);
	//cin.tie(NULL);
	int ite;
	cin >> ite;
	REP(tt, ite)
	{
		// printf("Case #%d: %d\n", tt, solve());
		cout<<"Case #"<<tt+1<<": "<<solve()<<endl;
	}	    
    return 0;
}
