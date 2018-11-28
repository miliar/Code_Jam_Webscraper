#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include <string> 
#include <vector> 
#include <queue> 
#include <set> 
#include <map> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 
#include <list>
#include <cassert>
#include <conio.h>
using namespace std; 

#define PB push_back 
#define MP make_pair 
#define SZ(v) ((int)(v).size()) 
#define FOR(i,a,b) for(int i=(a);i<(b);++i) 
#define REP(i,n) FOR(i,0,n) 
#define FORE(i,a,b) for(int i=(a);i<=(b);++i) 
#define REPE(i,n) FORE(i,0,n) 
#define FORSZ(i,a,v) FOR(i,a,SZ(v)) 
#define REPSZ(i,v) REP(i,SZ(v)) 
typedef long long ll; 


int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T;	
	cin >> T;
	cin.get();
	REP(i, T)
	{
		int lawn[100][100];
		int hormax[100], vermax[100];
		memset(lawn, 0, sizeof(int)*100*100);
		memset(hormax, 0, sizeof(int)*100);
		memset(vermax, 0, sizeof(int)*100);
		int N, M;
		cin >> N >> M;
		REP(i, N)
			REP(j, M)
			{
				cin >> lawn[i][j];
				if (lawn[i][j] > hormax[i]) hormax[i] = lawn[i][j];
				if (lawn[i][j] > vermax[j]) vermax[j] = lawn[i][j];
			}
		bool result = true;
		REP(i, N)
			REP(j, M)
				if (lawn[i][j] < hormax[i] && lawn[i][j] < vermax[j])
				{
					result = false;
					break;
				}
		cout << "Case #" << i+1 << ": ";
		if (result) cout << "YES" << endl;
		else cout << "NO" << endl;
	}
	return 0;
}