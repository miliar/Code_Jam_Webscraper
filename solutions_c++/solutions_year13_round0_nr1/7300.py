// Pre-written
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cstdlib>

#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>

#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

#define ALL(x) (x).begin(),(x).end()
#define FOR(i,a,b) for(i=a;i<=(b);i++)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define ZERO(x,s) memset(x,0,sizeof(s))
// Pre-written

char gStav[16];

void start() {

}

int vyhralNaPoziciach(char a, char b, char c, char d) {
	if( (a == 'X' || a == 'T') && 
		(b == 'X' || b == 'T')  && 
		(c == 'X' || c == 'T')  && 
		(d == 'X' || d == 'T') ) return 0;
	if( (a == 'O' || a == 'T') && 
		(b == 'O' || b == 'T')  && 
		(c == 'O' || c == 'T')  && 
		(d == 'O' || d== 'T') ) return 1;
	return 2;
}

int vyhral() {
	int x;
	x = vyhralNaPoziciach(gStav[0], gStav[1], gStav[2], gStav[3]);
	if(x != 2 ) return x;
	x = vyhralNaPoziciach(gStav[4], gStav[5], gStav[6], gStav[7]);
	if(x != 2 ) return x;
	x = vyhralNaPoziciach(gStav[8], gStav[9], gStav[10], gStav[11]);
	if(x != 2 ) return x;
	x = vyhralNaPoziciach(gStav[12], gStav[13], gStav[14], gStav[15]);
	if(x != 2 ) return x;

	x = vyhralNaPoziciach(gStav[0], gStav[4], gStav[8], gStav[12]);
	if(x != 2 ) return x;
	x = vyhralNaPoziciach(gStav[1], gStav[5], gStav[9], gStav[13]);
	if(x != 2 ) return x;
	x = vyhralNaPoziciach(gStav[2], gStav[6], gStav[10], gStav[14]);
	if(x != 2 ) return x;
	x = vyhralNaPoziciach(gStav[3], gStav[7], gStav[11], gStav[15]);
	if(x != 2 ) return x;

	x = vyhralNaPoziciach(gStav[0], gStav[5], gStav[10], gStav[15]);
	if(x != 2 ) return x;
	x = vyhralNaPoziciach(gStav[12], gStav[9], gStav[6], gStav[3]);
	if(x != 2 ) return x;
	return 2;
}

void doIt() {
	char c;
	int i, x;
	bool empty = false;

	for(i=0; i < 16; i++) {
		cin >> c;
		gStav[i] = c;
		if(c == '.') empty = true;
	}

	int vysledok = vyhral();
	if(vysledok == 0) {
		cout << "X won\n";
		return;
	}
	if(vysledok == 1) {
		cout <<  "O won\n";
		return;
	}
	if(empty) {
		cout <<  "Game has not completed\n";
	} else {
		cout << "Draw\n";
	}
}

int main( int argc, const char* argv[] )
{
	ifstream in("A-small-attempt0.in");
    cin.rdbuf(in.rdbuf());

    ofstream out("out.txt");
    cout.rdbuf(out.rdbuf());
	
	int n;
	cin >> n;
	start();
	for (int i = 1; i <= n; ++i) {
		cout << "Case #" << i << ": ";
		doIt();
	}
	return 0;
}