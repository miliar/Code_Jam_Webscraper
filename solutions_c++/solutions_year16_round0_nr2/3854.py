#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

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
	string str;
	int tc, cnt;
	cin >> tc;
	REP(i, tc) {
		str.clear();
		cnt = 0;
		cin >> str;
		FORC(it, str) {
			if(it+1 != str.end()) {
				if(*it != *(it+1))
					cnt++;
			} else {
				if(*it == '-')
					cnt++;
			}
		}
		cout << "Case #" << i+1 << ": " << cnt << endl;
	}
	return 0;
}
