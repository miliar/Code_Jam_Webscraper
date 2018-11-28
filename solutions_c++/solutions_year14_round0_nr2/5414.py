#include <vector>
#include <map>
#include <set>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <cctype>
#include <cstring>
#include <queue>
#include <cassert>

using namespace std;

typedef long long LL;
typedef vector<string> VS;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

#define MP make_pair
#define ST first
#define ND second
#define PB push_back
#define FOR(i,a,b) for( int i=(a); i<(b); ++i)
#define FORD(i,a,b) for( int i=(a); i>(b); --i)
#define REP(i,n) for(int i=0; i<(n); ++i)
#define ALL(X) (X).begin(),(X).end()
#define SZ(X) (int)(X).size()
#define FORE(it,X) for(__typeof((X).begin()) it=(X).begin(); it!=(X).end();++it)

double c,f,x;

int main()
{
	int tn;
	cin>>tn;

	FOR(qq,1,tn+1) {
		cin>>c>>f>>x;
		printf("Case #%d: ",qq);

		double dp = 1e100;
		int p = 0;

		while (1) {
			double cur = 2.0;
			double h = 0;
			REP(i, p) {
				h += c / cur;
				cur += f;
			}
			h += x / cur;
			if (dp > h)
				dp = h;
			else
				break;

			p++;
		}

		printf("%.12f\n",dp);
	}
	return 0;
}
