#include <fstream>
#include <iostream>
#include <vector>
#include <bitset>
#include <string.h>
#include <algorithm>
#include <iomanip>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <deque>

using namespace std;

const char infile[] = "input.in";
const char outfile[] = "output.out";

ifstream fin(infile);
ofstream fout(outfile);

const int MAXN = 100005;
const int oo = 0x3f3f3f3f;

typedef vector<int> Graph[MAXN];
typedef vector<int> :: iterator It;

const inline int min(const int &a, const int &b) { if( a > b ) return b;   return a; }
const inline int max(const int &a, const int &b) { if( a < b ) return b;   return a; }
const inline void Get_min(int &a, const int b)    { if( a > b ) a = b; }
const inline void Get_max(int &a, const int b)    { if( a < b ) a = b; }

int a[MAXN];
multiset <int> s;

#define cin fin
#define cout fout

int main() {
	int T;
	cin >> T;
	for (int test = 1; test <= T ; ++ test) {
		int N, X;
		int ans = 0;
		multiset <int> :: iterator it;

		cin >> N >> X;

        s.clear();
        memset(a, 0, sizeof(a));

		for (int i = 0 ; i < N ; ++ i) {
			cin >> a[i];
			s.insert (a[i]);
		}
		sort (a, a   +   N, greater <int>() );
		for (int i = 0 ; i < N ; ++ i) {
			it = s.find( a[ i ] );
			if ( it == s.end() )
                continue;
			s.erase( it );
			it = s.upper_bound( X - a[i] );
			if (it != s.begin()) {
				-- it;
				s.erase (it);
			}
			++ ans;
		}

		cout << "Case #" << test << ": " << ans << '\n';
	}
	return 0;
}
