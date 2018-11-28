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

using namespace std ;

#define INFILE "date.in"
#define	OUTFILE "date.out"
//#define cin F
//#define cout G

ifstream F (INFILE) ;
ofstream G (OUTFILE) ;

unsigned long long S, D, T ;

void Read() ;
void Solve() ;
long long pal(long long x) ;

int main() {
    int i ;
    cin >> T ;
    for (i = 1; i <= T ; ++i) {
        Read() ;
        cout << "Case #" << i << ": " ;
        Solve() ;
    }
	F.close() ;
    F.close() ;
	G.close() ;
	return 0;
}

void Read() {
    cin >> S >> D ;
}

void Solve() {
    long long i, nr = 0, root, ri ;
    for (i = S; i <= D; ++i) {
        root = sqrt (i) ;
        if (root * root == i) {
            ri = pal(i) ;
            if (ri == i) {
                ri = pal(root) ;
                if (ri == root)
                    ++ nr ;
            }
        }
    }
    cout << nr << '\n' ;
}

long long pal(long long x)  {
    long long y = 0, c ;
    while(x) {
        c = x % 10 ;
        y = y * 10 + c ;
        x /= 10 ;
    }
    return y ;
}
