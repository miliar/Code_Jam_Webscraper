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

int R,C,m;
int dt[12];
int ch[12][12];
bool end;
int goal;

void f(int r, int last)
{
	if (r == R) {
		REP(i,R) REP(j,C) ch[i][j]=0;

		REP(i, r) REP(j, dt[i]) {
			ch[i][j] = 1;
			ch[i+1][j] = 2;
			ch[i][j+1] = 2;
			ch[i+1][j+1] = 2;
		}
		int cnt = 0;
		REP(i, R) REP(j, C) if (ch[i][j] == 0)
			cnt++;

		if (cnt == goal)
			end = true;
		return;
	}

	REP(i, last+1) {
		if (r == 0 && i == 0) continue;

		dt[r]= i;
		f(r+1,i);
		if (end)
			return;
	}
}

int main()
{
	int tn;
	cin>>tn;

	FOR(qq,1,tn+1) {
		cin>>R>>C>>m;
		cout<<"Case #"<<qq<<":"<<endl;
		if (m == 0 || m == R*C-1) {
			REP(i, R) {
				REP(j, C) {
					if (i == 0 && j == 0) cout<<"c";
					else {
						if (m == 0)
							cout<<".";
						else
							cout<<"*";
					}
				}
				cout<<endl;
			}
			continue;
		}
		end = false;
		goal = m;

		f(0, C);

		if (!end) {
			cout<<"Impossible"<<endl;
			continue;
		}
		
		REP(i, R) {
			REP(j, C) {
				if (i == 0 && j == 0) cout<<"c";
				else if (ch[i][j]) cout<<".";
				else cout<<"*";
			}
			cout<<endl;
		}
	}
	return 0;
}
