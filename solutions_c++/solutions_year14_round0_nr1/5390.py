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

int dr[4][4],dc[4][4];
int r,c;

int main()
{
	int tn;
	cin>>tn;

	FOR(qq,1,tn+1) {
		cin>>r;
		REP(i,4) REP(j,4)
			cin>>dr[i][j];
		cin>>c;
		REP(i,4) REP(j,4)
			cin>>dc[i][j];
		r--,c--;

		VI chk(20,0);
		REP(j,4) chk[dr[r][j]]++;
		REP(i,4) chk[dc[c][i]]++;

		int ds = 0;
		int it = -1;
		FOR(i,1,17) if (chk[i] == 2) {
			ds++;
			it = i;
		}

		printf("Case #%d: ",qq);
		if (ds == 0) cout<<"Volunteer cheated!"<<endl;
		else if (ds >= 2) cout<<"Bad magician!"<<endl;
		else
			cout<<it<<endl;
	}
	return 0;
}
