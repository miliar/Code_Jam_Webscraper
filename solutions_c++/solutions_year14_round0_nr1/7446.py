#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <cstring>
#include <string>
#include <stack>
using namespace std;

typedef long long LL;
typedef long double LD;
#define ST first 
#define ND second
#define PB push_back
#define MP make_pair
#define SIZE(v) ((int)(v).size())
#define REP(i,n) for(typeof(n)i=0;i<(n);++i)
#define FOR(i,a,b) for(typeof(a)i=(a);i<=(b);++i)
#define FORD(i,a,b) for(typeof(a)i=(a);i>=(b);--i)
#define FOREACH(it,v) for(typeof((v).begin())it=(v).begin();it!=(v).end();++it)
#define ALL(v) (v).begin(),(v).end()

const int MX = 10;
LL N = 4, x[MX][MX], y[MX][MX], n, k;

int main()
{
	int q;
	cin >> q;

	FOR(i,1,q)
	{
		cout << "Case #"<<i<<": ";

		cin >> n; 
		REP(i,N) REP(j,N) cin >> x[i][j];
		cin >> k;
		REP(i,N) REP(j,N) cin >> y[i][j];

		vector<LL> v;
		REP(i,N) v.PB(x[n-1][i]);
		REP(i,N) v.PB(y[k-1][i]);

		sort(ALL(v));
		
		LL cnt = 0LL, rem;
		FOR(i,1,SIZE(v)-1)
			if(v[i] == v[i-1])
			{	
				++ cnt;
				rem = v[i];
			}

		if(cnt == 0LL)
			cout << "Volunteer cheated!\n";
		if(cnt == 1LL)
			cout << rem << endl;
		if(cnt > 1LL)
			cout << "Bad magician!\n";
	}

	return 0;
}
