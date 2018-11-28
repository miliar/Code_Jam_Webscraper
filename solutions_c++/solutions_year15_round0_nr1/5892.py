#include <bits/stdc++.h>

using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;
typedef long long LL;
#define MOD 1000000007

int main()
{
	ifstream fin("input.in");
	ofstream fout("output.txt");
	int t;
	fin>>t;
	REP(j,t)
	{
		int n;
		string a;
		fin>>n>>a;
		int claps=a[0]-'0',ans=0;;
		FOR(i,1,SZ(a))
		{
			if(claps<i)
			{
				ans+=(i-claps);
				claps=i;
			}
			claps+=a[i]-'0';
		}
		fout<<"Case #"<<j+1<<": "<<ans<<endl;
	}
	return 0;
}
