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
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	int T;	
	cin >> T;
	cin.get();
	REP(i, T)
	{
		int cards[17];
		memset(cards, 0, sizeof(int)*17);
		int c, n;
		cin >> c;
		REP(i, 4)
			REP(j, 4)
			{
				cin >> n;
				if (i+1 == c) ++cards[n];
			}
		cin >> c;
		REP(i, 4)
			REP(j, 4)
			{
				cin >> n;
				if (i+1 == c) ++cards[n];
			}
		int count = 0, result;
		REP(i, 17) if (cards[i] == 2) 
		{
			++count;
			result = i;
		}

		cout << "Case #" << i+1 << ": ";
		if (count == 0) cout << "Volunteer cheated!" << endl;
		else if (count == 1) cout << result << endl;
		else cout << "Bad magician!" << endl;
	}
	return 0;
}