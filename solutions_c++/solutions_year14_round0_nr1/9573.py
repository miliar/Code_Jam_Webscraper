#include <sstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>

using namespace std;

#define VI vector<int>
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) __typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second

const double EPS = 10e-13;

void read(int fr, int* ns) {
    for(int i = 0; i < 4; ++i)
	for(int j = 0; j < 4; ++j) {
	    int v; cin >> v;
	    if(i == fr) ns[j] = v;
	}
}

int main(int argc, char *argv[]) {
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);

    int tc; cin >> tc;
    int n = 1;
    while(tc-- > 0) {
	int fr; cin >> fr;
	int r0[4];
	read(--fr, r0);
	int sr; cin >> sr;
	int r1[4];
	read(--sr, r1);

	int cards = 0; int k = -1;
	for(int i = 0; i < 4; ++i)
	    for(int j = 0; j < 4; ++j) if(r0[i] == r1[j]) {
		    ++cards; k = i;
		}

	if(cards == 1)
	    cout << "Case #" << n << ": " << r0[k] << "\n";
	else if(cards == 0)
	    cout << "Case #" << n << ": Volunteer cheated!" << "\n";
	else
	    cout << "Case #" << n << ": Bad magician!" << "\n";
	++n;
    }

    return 0;
}
