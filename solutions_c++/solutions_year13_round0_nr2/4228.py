#include <vector>
#include <iostream>
#include <sstream>
#include <math.h>
#include <sys/time.h>
#include <cstdlib>
#include <algorithm>
#include <cassert>
#include <cstring>

#define FOR(i,a,b)  for(__typeof(b) i=(a);i<(b);++i)
#define REP(i,a)    FOR(i,0,a)
#define FOREACH(x,c)   for(__typeof(c.begin()) x=c.begin();x != c.end(); x++)
#define ALL(c)      c.begin(),c.end()
#define CLEAR(c)    memset(c,0,sizeof(c))
#define SIZE(c) (int) ((c).size())

#define PB          push_back
#define MP          make_pair
#define X           first
#define Y           second

#define ULL         unsigned long long
#define LL          long long
#define LD          long double
#define II         pair<int, int>
#define DD         pair<double, double>

#define VI          vector<int>
#define VVI         vector<VI >
#define VD                      vector<double>
#define VS          vector<string >
#define VII        vector<II >
#define VDD         vector< DD >

#define DUMP(a)       cerr << #a << ": " << a << endl;
using namespace std;

int tests;

int n, m;
int lawn[100][100];
int result;

void read_test(){
    cin >> n >> m;
    REP(i,n)
		REP(j,m)
        	cin >> lawn[i][j];
}

void solve_test(){
	vector<pair<int,pair<int,int> > > q;
	q.reserve(n*m);
	REP(i,n) REP(j,m)
		q.PB(MP(lawn[i][j],MP(i,j)));
	sort(ALL(q));

	vector<int> blockedR(n,0);
	vector<int> blockedC(m,0);

	FOREACH(e,q){
		int v = e->X;
		int x = (e->Y).X;
		int y = (e->Y).Y;
		if (blockedR[x] || blockedC[y])
			continue;
		int row=1,col=1;
		REP(i,n)
			if (!blockedR[i] && lawn[i][y] != v)
				col=0;
		if (col)
			blockedC[y] = 1;
		REP(j,m)
			if (!blockedC[j] && lawn[x][j] != v)
				row=0;
		if (row)
			blockedR[x] = 1;
		if (row==0 && col==0){
			result = 0;
			return;		
		}		
		
	}
	result = 1;
	return;
}

void dump_sol(int i){
	cout << "Case #" << i << ": ";
	if (result)
		cout << "YES";
	else
		cout << "NO";
	cout << endl;
    cout.flush();
}

int main(int argc, char *argv[]){
	cin >> tests;
	for(int i=0; i < tests; i++){
		read_test();
    		solve_test();
	    	dump_sol(i+1);
	}
}
