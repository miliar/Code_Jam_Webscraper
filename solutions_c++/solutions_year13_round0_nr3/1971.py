# include <iostream>
# include <fstream>
# include <sstream>
# include <algorithm>
# include <cstdio>
# include <cmath>
# include <numeric>
# include <cstdlib>
# include <cstring>
# include <vector>
# include <list>
# include <set>
# include <map>
# include <stack>
# include <queue>
# include <cctype>
# include <climits>
# include <complex>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,PII> TRI;
typedef vector<string> VS;

#define GI ({int t;scanf("%d",&t);t;})
#define REP(i,a,b) for(int i=a;i<b;i++)
#define FOR(i,n) REP(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define bitcount(x) __builtin_popcount(x)
#define pb push_back
#define mp make_pair
#define mt(a,b,c) mp(a,mp(b,c))
#define EPS (double)(1e-9)
#define INF 1000000000
#define MOD 1000000007
#define PI (double)(3.141592653589793)

inline int ni()
{
	register int r=0,c;
	for(c=getchar_unlocked();c<=32;c=getchar_unlocked());
	if(c=='-')
		return -ni();
	for(;c>32;r=(r<<1)+(r<<3)+c-'0',c=getchar_unlocked());
	return r;
}

LL ans[]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};

/*
bool ispalin(LL n)
{
	stringstream ss;
	string s;
	ss << n; ss >> s;
	REP(i,0,s.size())
		if(s[i] != s[s.size()-i-1])
			return false;
	return true;
}

void preprocess()
{
	for(LL i = 1; i <= 10000000; i++)
	{
		if(!ispalin(i)) continue;
		if(ispalin(i*i))
			ans.pb(i*i);
	}
}
*/

int main()
{
	int t,tcase,cnt;
	LL a,b;

	freopen("C-large-1.in","r",stdin);
	freopen("output.txt","w",stdout);

	t = GI;
	//preprocess();

	REP(tcase,1,t+1)
	{
		scanf("%lld %lld", &a, &b); cnt = 0;

		REP(i,0,39)
		{
			if(ans[i] >= a && ans[i] <= b)
				cnt++;
		}

		printf("Case #%d: %d\n", tcase, cnt);
	}
		
	return 0;
}

