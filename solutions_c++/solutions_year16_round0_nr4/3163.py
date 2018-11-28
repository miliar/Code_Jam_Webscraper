#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
#define ZERO(x) memset(x,0,sizeof(x))
#define FOR(v,p,k) for(int v=p;v<k;++v)
#define FORE(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define FORC(i,c) for(__typeof(c.begin()) i=(c.begin());i!=(c).end();++i)
#define ALL(c) c.begin(),c.end()
//cout <<  __func__ << " : " << __LINE__ << endl;

int main(void)
{
	int tc, k, c, s;
	cin >> tc;
	REP(i, tc) {
		cin >> k >> c >> s;
		cout << " Case #" << i+1 << ":";
		REP(i,k)
			cout << " " << i+1; 
		cout << endl;
	}
	return 0;
}
