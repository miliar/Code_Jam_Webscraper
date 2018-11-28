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

typedef pair<int,int> PR;
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
typedef long long LL;

#define MAXN 10010
int s[MAXN];
void work()
{
	int ans = 0;
	int N,x;
	cin>>N>>x;
	for(int i=0;i<N;i++)
		cin>>s[i];
	sort(s,s+N);
	int k=0;// 表示<=50标记。
	for(int i=0;i<N;i++)
		if(s[i]>x/2)
		{
			k = i;break;
		}
	int l=0;
	for(int i=N-1;i>=k;i--)
	{
		if(s[l]+s[i]<=x)
		{
			l++;
		}
		ans++;
	}
	int num = k-l;
	ans += num/2;
	if(num%2==1)
		ans++;
	cout<<ans<<endl;
}

int main()
{
		freopen("a.in", "r", stdin);
		freopen("a.out", "w", stdout);

	int t2;
	cin >> t2;
	for (int t1 = 1; t1 <= t2; ++t1) {
		printf("Case #%d: ", t1);
		work();
	}

	return 0;
}