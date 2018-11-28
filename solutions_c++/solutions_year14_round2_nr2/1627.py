#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <cstdio>
#include <algorithm>
#include <unistd.h>

#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )

using namespace std;
int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }


int main()
{
    int i, j, k;
    int nbTestCases = 0;
    freopen ("B-small-attempt0.in","r",stdin);
    freopen ("B-small-attempt0.out","w",stdout);
    cin >> nbTestCases;

    fi(nbTestCases) {
        long long A = nll(), B = nll(), K = nll();
        int waysToWin = 0;
        fj(A) {
            fk (B) {
                //cout << j << " " << k << " " << (j&k) << endl;
                if ((j&k)<K) {
                    waysToWin++;
                }
            }
        }
        cout << "Case #" << i+1 << ": " << waysToWin << endl;
    }
    return 0;
}
