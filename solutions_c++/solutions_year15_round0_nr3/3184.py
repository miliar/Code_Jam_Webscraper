#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <fstream>

using namespace std;

int hs[260];
int opt[4][4];

void init(){
    hs[ '1' ] = 0, hs[ 'i' ] = 1;
    hs[ 'j' ] = 2, hs[ 'k' ] = 3;
    
    opt[0][0] = '1', opt[0][1] = 'i', opt[0][2] = 'j', opt[0][3] = 'k';
    opt[1][0] = 'i', opt[1][1] = -1 * '1', opt[1][2] = 'k', opt[1][3] = 'j' * -1;
    opt[2][0] = 'j', opt[2][1] = 'k' * -1, opt[2][2] = -1 * '1', opt[2][3] = 'i';
    opt[3][0] = 'k', opt[3][1] = 'j', opt[3][2] = 'i' * -1, opt[3][3] = -1 * '1';

}

string fin;
char str[10010];

int main(){
    freopen("C-small-attempt3.in", "r", stdin);
    freopen("C-small-attempt3.out", "w", stdout);
    int T, t;
    int i, j, k;
    int l, x;
    int cur, key;
    int pi, pk;
    init();
    scanf("%d", &T);
    for( t = 1; t <= T; t++){
        bool ok = 0;
        scanf("%d%d", &l, &x);
        scanf("%s", str);
        fin = "";
        for( i = 0; i < x; i++)
            fin += str;
        
        pi = -1;
        pk = -1;
        
        cur = '1';

        for( i = 0; i < x * l; i++){
            key = cur >= 0 ? cur : -cur;
            cur = ( cur >= 0 ? 1 : -1 ) * opt[ hs[key] ][ hs[fin[i]] ];
            if( cur == 'i' && pi == -1) pi = i;
            if( cur == 'k' ) pk = i;
        }

        if( pi != -1 && pi < pk && cur == -1 * '1' )
            ok = 1;
        
        if( ok )
            printf( "Case #%d: YES\n", t);
        else
            printf( "Case #%d: NO\n", t);
    }
    return 0;
}
