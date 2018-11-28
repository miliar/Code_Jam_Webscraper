
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
const ULL B = 100000007; // ¹þÏ£µÄ»ùÊý¡£


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

#define MAXN 11
#define MAXM 101



int n;
char strs[MAXN][MAXM];

bool dfs(int que[], int k)
{
	int flag[26] = {0};
	char ta = 0;
	for(int i=0; i<k; ++i)
	{
		char *str = strs[que[i]];
		int len = strlen(str);
		for(int j=0; j<len; ++j){
			if(j==0 && i==0){
				ta = str[j];
			}else{
				if(ta != str[j]){
					flag[ta-'a'] = true;
					ta = str[j];
					if(flag[ta-'a']){
						return false;
					}
				}
			}
		}
	}
	return true;
}

int mysearch(int k)
{
	int cnt = 0;
	int que[MAXN];
	for(int i=0; i<k; ++i)	que[i] = i;
	if(dfs(que, k)) cnt++;
	while (next_permutation(que,que+k))
	{
		if(dfs(que, k))		cnt++;
	}
	return cnt;
}

int main()
{

	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t; cin>>t;
	for(int i=1; i<=t; ++i)
	{
		cin>>n;
		for(int j=0; j<n; ++j)
		{
			cin>>strs[j];
		}
		int cnt = mysearch(n);
		cout<<"Case #"<<i<<": "<<cnt<<endl;
	}
	return 0;
}