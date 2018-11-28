


#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <string>
#include <cstdio>
#include <algorithm>
#include <numeric>
#include <functional>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
#include <numeric>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
const ULL B = 100000007; // 哈希的基数。


#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define REPD(i,n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define CLEAR(x) memset(x,0,sizeof x);
#define CLEARA(x) memset(&x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);
#define FILLA(x,v) memset(&x,v,sizeof x);

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()
#define MP make_pair
#define eps 1.0e-11
const double pi = acos(-1.0);

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;

#define N 105
string s[N];
string s1[N];
int len;
int cnt[N][N];
int res[N];
void work()
{
	memset(cnt,0,N*N*sizeof(cnt[0][0]));
	memset(res,0,sizeof(res));
 	int n; cin>>n;
	REP(i,n)
	{
		cin>>s[i];
		s1[i] = s[i];
		s1[i].erase(unique(s1[i].begin(),s1[i].end()),s1[i].begin());
		len = s1[i].length();
	}
	bool flag = true;
	REP(i,n-1)
	{
		if(s1[i]!=s1[i+1])
		{
			flag = false; break;
		}
	}
	if(!flag)
	{
		cout<<"Fegla Won";
		return;
	}
	else
	{
		REP(i,n) //处理s[i]
		{
			int t = 0; //t<len
			cnt[i][0] = 1;
			FOR(j,1,s[i].length())
			{
				if(s[i][j]==s[i][j-1])
					cnt[i][t]++;
				else
				{
					t++;
					cnt[i][t]++;
				}
			}
		}

// 		REP(i,n)
// 			REP(j,len)
// 		{
// 			cout<<s1[i][j]<<" "<<cnt[i][j]<<endl;
// 		}

		REP(j,len)
		{
			
			int minn = INF;
			FOR(k,1,100)
			{
				int sm = 0;
				FOR(i,0,n-1)
				{	
					sm += abs(cnt[i][j] - k);
				}
				if(sm<minn)
					minn = sm;
			}
			res[j] = minn;
//			cout<<res[j]<<endl;
		}
		int ans = 0;
		REP(i,len)
			ans += res[i];
		cout<<ans;
	}
}

int main()
{
	freopen("a2.in", "r", stdin);
	freopen("a2.out", "w", stdout);
	
	int t2;
	cin >> t2;
	for (int t1 = 1; t1 <= t2; ++t1) {
		printf("Case #%d: ", t1);
		work();
		printf("\n");
	}

// 	string s; cin>>s;
// 	s.erase(unique(s.begin(),s.end()),s.begin());
// 	cout<<s<<endl;
// 	return 0;
}

