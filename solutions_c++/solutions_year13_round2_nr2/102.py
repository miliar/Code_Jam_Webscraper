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
#define eps           1e-7

using namespace std;

int tests;
int n;
int x, y;
double result;

void read_test(){
	cin >> n >> x >> y;
}

double solve_test(){
	int	total = 0;
	int side = 0;
	int S = abs(x)+abs(y);
	while (side < S){ total += 2*side+1; side+=2;}
	if (total > n) 
		return 0;
	int next = total + 2*S+1;
	if (n >= next)
		return 1;
	if (x == 0)
		return 0;
	int tosses = n-total;
	int heads = S+1-abs(x);
	if (tosses - S >= heads)
		return 1;
	if (heads > tosses)
		return 0;

	// here success means we got >= heads heads
	vector<double> pal(tosses+1,0);
	pal[0] = 1;
	REP(i,tosses)
		for(int j=tosses; j >= 1; j--)
			pal[j] = 0.5*pal[j] + 0.5*pal[j-1];
	//REP(i,tosses) cout << pal[i] << " ";
	return pal[heads];
}

void dump_sol(int i){
	cout << "Case #" << i << ": ";
	cout << result << endl;
    cout.flush();
}

int main(int argc, char *argv[]){
	cin >> tests;
	for(int i=0; i < tests; i++){
		read_test();
    		result = solve_test();
			if (result < eps)
				result = 0;
	    	dump_sol(i+1);
	}
}
