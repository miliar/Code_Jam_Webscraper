#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
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

#define SIZE(A) ((int)(A).size())
#define ALL(A) (A).begin(),(A).end()
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define NMAX 101

using namespace std ;

#define INFILE "date.in"
#define	OUTFILE "date.out"
//#define cin F
//#define cout G

ifstream F (INFILE) ;
ofstream G (OUTFILE) ;

int MAXL[NMAX] ;
int MAXC[NMAX] ;
int MAT[NMAX][NMAX] ;
int T, N, M ;

void Read() ;
void Solve() ;

int main() {
    int i ;
    cin >> T ;
    for (i = 1; i <= T ; ++i) {
        Read() ;
        cout << "Case #" << i << ": " ;
        Solve() ;
    }
	F.close() ;
    G.close() ;
	return 0;
}

void Read () {
    int i, j ;
    cin >> N >> M ;
    for (i = 1; i <= 100; ++i)
        MAXC[i] = MAXL[i] = 0 ;
    for (i = 1; i <= N; ++i) {
        for (j = 1; j <=M; ++j) {
            cin >> MAT[i][j] ;
            if (MAT[i][j] > MAXC[j])
                MAXC[j] = MAT[i][j] ;
            if (MAT[i][j] > MAXL[i])
                MAXL[i] = MAT[i][j] ;
        }
    }
}

void Solve () {
    int i, j ;
    int ok1 = 1 ;
    for (i = 1; i <= N; ++i) {
        for (j = 1; j <=M; ++j) {
            if (MAT[i][j] < MAXC[j] && MAT[i][j] < MAXL[i])
                ok1 = 0 ;
        }
    }
    if (ok1) {
        cout << "YES\n" ;
    }
    else {
        cout << "NO\n" ;
    }
}
