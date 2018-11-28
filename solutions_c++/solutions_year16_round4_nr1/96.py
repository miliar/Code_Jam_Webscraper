#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker,"/STACK:32000000")
#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cassert>

using namespace std;

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
#define INF 0x7fffffff
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

int n,a[3];
int b[5555];
int cnt[3];

bool check(bool ignore=false)
{
	if (!ignore) REP(i,3) if (cnt[i]!=a[i]) return false;
	VI q(b,b+(1<<n));
	while (q.size() > 1)
	{
		VI qq;
		REP(i,SZ(q)/2)
		{
			int x = q[i*2];
			int y = q[i*2+1];
			if (x==y) return false;
			if (y==(x+1)%3)
				qq.pb(x);
			else
				qq.pb(y);
		}
		q=qq;
	}
	return true;
}

bool brute() {
	int pw = 1;
	REP(i,1<<n) pw*=3;
	REP(mask,pw) {
		int x=mask;
		REPD(i,1<<n) {
			b[i]=x%3;
			x/=3;
		}
		CLEAR(cnt);
		REP(i,1<<n) cnt[b[i]]++;
		if (check()) {
			return true;
		}
	}
	return false;
}

bool brute2() {
	set<VI> ans;
	int qqq=0;

	int pw = 1;
	REP(i,1<<n) pw*=3;
	REP(mask,pw) {
		int x=mask;
		REPD(i,1<<n) {
			b[i]=x%3;
			x/=3;
		}
		CLEAR(cnt);
		REP(i,1<<n) cnt[b[i]]++;
		if (check(true)) {
			ans.insert(VI(cnt,cnt+3));
			++qqq;
		}
	}
	printf("!!! %d\n",qqq);
	for (set<VI>::iterator it = ans.begin(); it!=ans.end(); ++it)
	{
		printf("%d %d %d\n",(*it)[0],(*it)[1],(*it)[2]);
	}
}

const char* order = "PRS";

string get(int n, int f)
{
	if (n==0) return string(1,f);
	string x = get(n-1,f);
	string y = get(n-1,(f+1)%3);
	if (x>y) swap(x,y);
	return x+y;
}

int main(int argc, char **argv)
{
	/*n=3;
	brute2();
	return 0;*/

	string FN = "A-large";
	if (argc>1) FN = string(argv[1]);
	int shift = 0;
	if (argc>2) sscanf(argv[2],"%d",&shift);
	freopen((FN+".in").c_str(),"r",stdin);
	freopen((FN+".out").c_str(),"w",stdout);

	int tests;
	scanf("%d",&tests);
	for (int test = 1; test<=tests; test++)
	{
		fprintf(stderr,"=== %s : %d\n", FN.c_str(), test+shift);
		printf("Case #%d: ",test+shift);
		////////////////////////////////////////////////////////////
		scanf("%d%d%d%d",&n,&a[1],&a[0],&a[2]);
		vector<string> q;
		REP(i,3) {
			string s = get(n,i);
			int cnt[3];
			CLEAR(cnt);
			REP(i,1<<n) cnt[s[i]]++;
			bool ok = true;
			REP(i,3) if (a[i]!=cnt[i]) ok =false;
			if (ok)
			{
				REP(i,SZ(s)) s[i]=order[s[i]];
				q.push_back(s);
			}
		}
		SORT(q);
		if (!q.empty()) {
			printf("%s\n", q[0].c_str());
		} else
			printf("IMPOSSIBLE\n");
	}
	fprintf(stderr,"=== %s DONE\n", FN.c_str());
	return 0;
}