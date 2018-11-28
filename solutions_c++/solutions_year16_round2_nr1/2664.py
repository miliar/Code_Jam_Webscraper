#include <iostream>
#include <fstream>
#include <list>
#include <stack>
#include <deque>
#include <utility>
#include <queue>
#include <set>
#include <map>
#include <ext\hash_set>
#include <bitset>
#include <vector>
#include <cmath>
#include <string>
#include <algorithm>
#include <iomanip>
#include <ctime>
#include <iterator>
#include <cstdio>
#include <cstring>
#include <cstdlib>


using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

#define f first
#define s second
#define pb push_back
#define mp make_pair

const int maxn = 10000;
const int inf = 2e9;
const double eps = 1e-8;
const int base = 1073676287;

char t[maxn];
int letters[180];
vector < int > a;

void init() {
    for ( int j = 0; j < 180; j++ )
        letters[j] = 0;
}

void calc0() {
    letters['E'] -= letters['Z'];
    letters['R'] -= letters['Z'];
    letters['O'] -= letters['Z'];
    while ( letters['Z']-- )
        a.pb( 0 );
}

void calc1() {
    while ( letters['O']-- )
        a.pb( 1 );
}

void calc2() {
    letters['T'] -= letters['W'];
    letters['O'] -= letters['W'];
    while ( letters['W']-- )
        a.pb( 2 );
}

void calc3() {
    letters['T'] -= letters['R'];
    letters['H'] -= letters['R'];
    letters['E'] -= letters['R'];
    letters['E'] -= letters['R'];
    while ( letters['R']-- )
        a.pb( 3 );
}

void calc4() {
    letters['F'] -= letters['U'];
    letters['O'] -= letters['U'];
    letters['R'] -= letters['U'];
    while ( letters['U']-- )
        a.pb( 4 );
}

void calc5() {
    letters['I'] -= letters['F'];
    letters['V'] -= letters['F'];
    letters['E'] -= letters['F'];
    while ( letters['F']-- )
        a.pb( 5 );
}

void calc6() {
    letters['S'] -= letters['X'];
    letters['I'] -= letters['X'];
    while ( letters['X']-- )
        a.pb( 6 );
}

void calc7() {
    letters['E'] -= letters['S'];
    letters['E'] -= letters['S'];
    letters['V'] -= letters['S'];
    letters['N'] -= letters['S'];
    while ( letters['S']-- )
        a.pb( 7 );
}

void calc8() {
    letters['E'] -= letters['G'];
    letters['I'] -= letters['G'];
    letters['H'] -= letters['G'];
    letters['T'] -= letters['G'];
    while ( letters['G']-- )
        a.pb( 8 );
}

void calc9() {
    letters['N'] -= letters['I'];
    letters['N'] -= letters['I'];
    letters['E'] -= letters['I'];
    while ( letters['I']-- )
        a.pb( 9 );
}

int main()
{
    srand( time( 0 ) );
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );
//    ios_base::sync_with_stdio(false);
    int q;
    scanf ( "%d\n", &q );
    for ( int j = 1; j <= q; j++ ) {
        a.clear();
        gets( t );
        init();
        int n = strlen( t );
        for ( int i = 0; i < n; i++ )
            letters[t[i]]++;
        calc0();
        calc2();
        calc4();
        calc3();
        calc5();
        calc6();
        calc7();
        calc8();
        calc9();
        calc1();
        sort( a.begin(), a.end() );
        n = a.size();
        printf ( "Case #%d: ", j );
        for ( int i = 0; i < n; i++ )
            printf ( "%d", a[i] );
        printf ( "\n" );
    }
    return 0;
}
