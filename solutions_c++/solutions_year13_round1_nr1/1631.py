#include <vector>           // push_back(), erase()
#include <list>             // front(), back(), push/pop_front(), push/pop_back()
#include <map>              // insert(), erase(), clear(), find()
#include <set>              // insert(), erase(), clear(), find()
#include <deque>            // front(), back(), push(), pop()
#include <stack>            // top(), push(), pop()
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define ULL unsigned long long
#define UI unsigned int
#define USI unsigned short int
#define UC unsigned char
#define SIZE(A) ((int)(A).size())
#define ALL(A) (A).begin(),(A).end()
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define NMAX OOOOOO
#define MMAX OOOOOO

using namespace std ;

#define INFILE "date.in"
#define	OUTFILE "date.out"
//#define cin F
//#define cout G

ifstream F (INFILE) ;
ofstream G (OUTFILE) ;

int T ;

void Solve() ;

int main() {
    int i ;
    cin >> T ;
    for (i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": " ;
        Solve() ;
        cout << '\n' ;
    }
	F.close() ;
	G.close() ;
	return 0;
}

void Solve() {
    int r, t, i, x ;
    int nr = 0 ;
    cin >> r >> t ;
    for (i = r; t >0; i += 2) {
        x = (i + 1) * 2 - 1 ;
        t -= x;
        ++ nr ;
    }
    if (0 > t) {
        -- nr ;
    }

    cout << nr ;

}
