#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <cmath>

#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )
using namespace std;
int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }

template <class T> void out( T a, T b ) { bool first = true; for( T i = a; i != b; ++ i ) { if( !first ) printf( " " ); first = false; cout << * i; } printf( "\n" ); }
template <class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }
typedef long long ll;

char s[1002];
int smax;
int reqd;
int i;

void fun()
{
    int standing = s[0];
    fo(i,1,smax+2)
    {
        if(standing < i)
        {
            reqd += i - standing;
            standing += i - standing;
        }
        standing += s[i];
    }
}

void init()
{
    reqd = 0;
    smax = ni();
    cin>>s;
    fi(smax + 2)
    {
        s[i] -= '0';
    }
}

void output(int i)
{
    printf("Case #%d: %d\n", i, reqd);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("myoutput.txt", "w", stdout);
    int j,t;
    t = ni();
    fj(t)
    {
        init();
        fun();
        output(j+1);
    }
}


