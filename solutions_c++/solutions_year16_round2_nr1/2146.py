#include <bits/stdc++.h>
using namespace std;
const int MAXN = 2000 + 10;

char s[MAXN];
int cnt[30], ncnt[10];
int n;

int main() {
    int t;
    freopen( "A.out", "w+", stdout );
    scanf( "%d", &t );
    for( int ncas = 1; ncas <= t; ++ncas ) {
        printf( "Case #%d: ", ncas );
        memset( cnt, 0, sizeof( cnt ) );
        memset( ncnt, 0, sizeof( ncnt ) );
        scanf( "%s", s );
        int len = strlen( s );
        for( int i = 0; i < len; ++i ) ++cnt[s[i] - 'A'];
        int t = cnt['z' - 'a'];
        ncnt[0] = t;
        cnt['z' - 'a'] -= t;
        cnt['e' - 'a'] -= t;
        cnt['r' - 'a'] -= t;
        cnt['o' - 'a'] -= t;
        t = cnt['w' - 'a'];
        ncnt[2] = t;
        cnt['t' - 'a'] -= t;
        cnt['w' - 'a'] -= t;
        cnt['o' - 'a'] -= t;
        t = cnt['u' - 'a'];
        ncnt[4] = t;
        cnt['f' - 'a'] -= t;
        cnt['o' - 'a'] -= t;
        cnt['u' - 'a'] -= t;
        cnt['r' - 'a'] -= t;
        t = cnt['x' - 'a'];
        ncnt[6] = t;
        cnt['s' - 'a'] -= t;
        cnt['i' - 'a'] -= t;
        cnt['x' - 'a'] -= t;
        t = cnt['g' - 'a'];
        ncnt[8] = t;
        cnt['e' - 'a'] -= t;
        cnt['i' - 'a'] -= t;
        cnt['g' - 'a'] -= t;
        cnt['h' - 'a'] -= t;
        cnt['t' - 'a'] -= t;
        t = cnt['o' - 'a'];
        ncnt[1] = t;
        cnt['o' - 'a'] -= t;
        cnt['n' - 'a'] -= t;
        cnt['e' - 'a'] -= t;
        t = cnt['h' - 'a'];
        ncnt[3] = t;
        cnt['t' - 'a'] -= t;
        cnt['h' - 'a'] -= t;
        cnt['r' - 'a'] -= t;
        cnt['e' - 'a'] -= t;
        cnt['e' - 'a'] -= t;
        t = cnt['f' - 'a'];
        ncnt[5] = t;
        cnt['f' - 'a'] -= t;
        cnt['i' - 'a'] -= t;
        cnt['v' - 'a'] -= t;
        cnt['e' - 'a'] -= t;
        t = cnt['s' - 'a'];
        ncnt[7] = t;
        cnt['s' - 'a'] -= t;
        cnt['e' - 'a'] -= t;
        cnt['v' - 'a'] -= t;
        cnt['e' - 'a'] -= t;
        cnt['n' - 'a'] -= t;
        t = cnt['i' - 'a'];
        ncnt[9] = t;
        cnt['n' - 'a'] -= t;
        cnt['i' - 'a'] -= t;
        cnt['n' - 'a'] -= t;
        cnt['e' - 'a'] -= t;
        len = 0;
        for( int i = 0; i < 10; ++i ) {
            for( int j = 0; j < ncnt[i]; ++j ) {
                s[len++] = i + '0';
            }
        }
        s[len] = 0;
        printf( "%s\n", s );
    }
    return 0;
}
