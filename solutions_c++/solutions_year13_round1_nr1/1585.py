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

void start() {

}

void doIt() {
	unsigned long long r, t;
	cin >> r;
	cin >> t;

	unsigned long long celkovaFarba = 0;
	unsigned long long pocetvykonanych = 0;
	for(unsigned long long i= r + 1; i > 0; i+=2) {
		unsigned long long A = i*i;
		unsigned long long B = (i-1)*(i-1);
		unsigned long long rozdiel = A - B;
		celkovaFarba += rozdiel;
		if(celkovaFarba > t) {
			break;
		}
		pocetvykonanych++;
	}

	cout << pocetvykonanych;
	cout << "\n";	
}

int main( int argc, const char* argv[] )
{
	ifstream in("in.in");
    cin.rdbuf(in.rdbuf());

    ofstream out("out.out");
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