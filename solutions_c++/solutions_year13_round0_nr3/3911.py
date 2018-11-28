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

int nns[40] = {0,
1,
2,
3,
11,
22,
101,
111,
121,
202,
212,
1001,
1111,
2002,
10001,
10101,
10201,
11011,
11111,
11211,
20002,
20102,
100001,
101101,
110011,
111111,
200002,
1000001,
1001001,
1002001,
1010101,
1011101,
1012101,
1100011,
1101011,
1102011,
1110111,
1111111,
2000002,
2001002};

ULL A,B;
int result;

int d[201];

int pal(ULL x){
	int p;
	for(p=0; x != 0; p++){
		d[p] = x%10;
		x /= 10;
	}
	//cout << x << " " << p << " " << d[0] << " " << d[1] << " " << d[2] << endl;
	REP(j,p/2)
		if (d[j] != d[p-1-j])
			return 0;
	return 1;
}

void read_test(){
	cin >> A >> B;
}

void solve_test(){
	result = 0;
	//cout << A << " " << B << endl;
	REP(i,40)
		if (nns[i]*nns[i] >= A && nns[i]*nns[i] <= B)
			result++;
}

void dump_sol(int i){
	cout << "Case #" << i << ": ";
	cout << result << endl;
    cout.flush();
}

int main(int argc, char *argv[]){
/*	REP(i,10000000ULL)
		if (pal(i) && pal(((ULL)i)*((ULL)i)))
			cout << i << "," << endl;
    return 0;
*/
	cin >> tests;
	for(int i=0; i < tests; i++){
		read_test();
    		solve_test();
	    	dump_sol(i+1);
	}
}
