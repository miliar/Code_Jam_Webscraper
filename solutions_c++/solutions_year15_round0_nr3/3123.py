/*
 *
 */
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

char g[256][256],u[1<<14],v[1<<14],T;
int n,m,L;
char s[1<<14],t[1 << 14];

int main() {
    int i,j,k,cs = 0,ts;
    const char *a = "IJK";

    g['1']['1'] = '1';
    g['1']['i'] = 'i';
    g['1']['j'] = 'j';
    g['1']['k'] = 'k';
    g['i']['1'] = 'i';
    g['i']['i'] = '*';
    g['i']['j'] = 'k';
    g['i']['k'] = 'J';
    g['j']['1'] = 'j';
    g['j']['i'] = 'K';
    g['j']['j'] = '*';
    g['j']['k'] = 'i';
    g['k']['1'] = 'k';
    g['k']['i'] = 'j';
    g['k']['j'] = 'I';
    g['k']['k'] = '*';

    g['*']['1'] = g['1']['*'] = '*';
    for ( i = 0; i < 3; ++i ) {
        g[a[i]]['*'] = g['*'][a[i]] = tolower(a[i]);
        g[tolower(a[i])]['*'] = g['*'][tolower(a[i])] = a[i];
        g[tolower(a[i])][a[i]] = '1';
        g[a[i]][tolower(a[i])] = '1';
        g['1'][a[i]] = g[a[i]]['1'] = a[i];
        for ( j = 0; j < 3; ++j ) {
            g[a[i]][a[j]] = g[tolower(a[i])][tolower(a[j])];
            if ( a[i] == a[j] ) continue ;
            char ch = g[tolower(a[i])][tolower(a[j])];
            assert( isalpha(ch) );
            if ( isupper(ch) )
                g[a[i]][tolower(a[j])] = g[tolower(a[i])][a[j]] = tolower(ch);
            else 
                g[a[i]][tolower(a[j])] = g[tolower(a[i])][a[j]] = toupper(ch);
        }
    }
    g['*']['*'] = '1';

    for ( scanf("%d",&ts); ts--; ) {
        scanf("%d %d %s",&L,&m,t);
        printf("Case #%d: ",++cs);
        assert( (n=m*L) <= 10000 );
        for ( k = 0, i = 0; i < m; ++i )
            for ( j = 0; j < L; ++j )
                s[k++] = t[j];
        assert( n == k );
        for ( v[0] = s[0], i = 1; i < n; ++i )
            v[i] = g[v[i-1]][s[i]];
        for ( u[n-1] = s[n-1], i = n-2; i >= 0; --i )
            u[i] = g[s[i]][u[i+1]];
        T = v[n-1];
        assert( T == u[0] );
        assert( g[g['i']['j']]['k'] == g['i'][g['j']['k']] );
        if ( T != g[g['i']['j']]['k'] ) {
            puts("NO");
            continue ;
        }
        for ( i = 0; i < n; ++i )
            if ( v[i] == 'i' ) break ;
        for ( k = n-1; k >= 0; --k )
            if ( u[k] == 'k' ) break ;
        puts(i < k?"YES":"NO");
    }
    return 0;
}

