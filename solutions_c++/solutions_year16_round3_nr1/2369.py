#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <cstdio>
#include <cstring>

using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
#define ZERO(x) memset(x,0,sizeof(x))
#define FOR(v,p,k) for(int v=p;v<k;++v)
#define FORE(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define FORC(i,c) for(__typeof(c.begin()) i=(c.begin());i!=(c).end();++i)
#define ALL(c) c.begin(),c.end()
//cout <<  __func__ << " : " << __LINE__ << endl;
//#define DEBUG
#ifdef DEBUG
#define D(x) x 
#else
#define D(x)
#endif

vector <pair <int, int> > S;
int N;
int main(void)
{
	int tc, tmp_in;
	cin >> tc;
	REP(i, tc) {
		S.clear();
		cin >> N;
		REP(ii, N) {
			cin >> tmp_in;
			S.push_back(make_pair(tmp_in, ii));
		}
		printf("Case #%d: ", i+1);
		while(1) {
			sort(ALL(S));
			if (S.size() == 2 and S[0].first == S[1].first) {
				cout <<(char)( 'A'+S[0].second) << (char)('A'+S[1].second) << " ";
				S[0].first -= 1;
				S[1].first -= 1;
				if (S.back().first == 0)  {
					S.pop_back();
					S.pop_back();
				}
				if (S.size() == 0)
					break;
			} else {
				cout <<(char)( 'A'+S.back().second) << " ";
				S.back().first -= 1;
				if (S.back().first == 0) 
					S.pop_back();
				if (S.size() == 0)
					break;
			}
		}
		cout << endl;
	}
	return 0;
}
