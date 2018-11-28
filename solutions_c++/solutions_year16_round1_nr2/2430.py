#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<cmath>
#define mem(a) memset( a, 0, sizeof(a) )
using namespace std;

struct node
{
    int c[55];
}p[105], q[105];
int vis[105];
int n, ans[55];

int ff[55][55];

bool cmp( node a, node b )
{
    int i;
    for( i = 1; i <= n; i ++ ){
        if( a.c[i] < b.c[i] ) return 1;
        if( a.c[i] > b.c[i] ) return 0;
    }
    return 1;
}

int same( node a, node b )
{
    int i, fl = 0;
    for( int i = 1; i <= n; i ++ ){
        if( a.c[i] > b.c[i] ){
            fl = 1;
            break;
        }
        if( a.c[i] < b.c[i] ){
            fl = -1;
            break;
        }
    }
    return fl;
}

int small( node a, node b )
{
    int i, fl = 1;
    for( i = 1; i <= n; i ++){
        if( a.c[i] >= b.c[i] ){
            fl = 0;
            break;
        }
    }
    return fl;
}

int dfs( int id, int cnt )
{
    int i, j, k, s;
    node tmp, res;
    if( cnt == n ){
        int fl = 0;
        for( i = 1; i <= n; i ++ ){
            for( j = 1; j <= n; j ++ ){
                tmp.c[j] = p[ans[j]].c[i];
            }
            for( j = 1; j <= 2*n-1; j ++ ){
                if( vis[j] ) continue;
                if( same( tmp, p[j] ) != 0 ) continue;
                else{
                    vis[j] = 2;
                    break;
                }
            }
            if( j == 2*n ){
                fl ++;
                if( fl >= 2 ){
                    for( j = 1; j <= 2*n-1; j ++ )
                        if( vis[j] == 2 )vis[j] = 0;
                    return 0;
                }
                else res = tmp;
            }
            }
//        p[2*n] = res;
        for( i = 1; i <= n; i ++ )
            if( i == n )printf("%d \n", res.c[i]);
            else printf("%d ", res.c[i]);
//        for( i = 1; i <= n; i ++ ){
//            for( j = 1; j <= n; j ++ )
//                ff[i][ j ] = p[ans[i]].c[j];
//        }
        return 1;
    }
    for( i = id+1; i <= 2*n-1; i ++ ){
        if( !vis[i] && small( p[id], p[i] ) ){
            vis[i] = 1;
            ans[cnt+1] = i;
            if( dfs( i, cnt+1 ) ) return 1;
            vis[i] = 0;
        }
    }
    return 0;
}

int main()
{
    int i, j, m;
    int T, cas = 1;
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("out.txt", "w", stdout );
    scanf("%d", &T);
    while( T -- ){
        scanf("%d", &n);
        for( i = 1; i <= 2*n-1; i ++ )
            for( j = 1; j <= n; j ++ )scanf("%d", &p[i].c[j]);
        sort( p+1, p+2*n, cmp );
//        if( cas == 30 ){
//        printf("%d\n", n);
//        for( i = 1; i <= 2*n-1; i ++ ){
//            for( j = 1; j <= n; j ++ )
//                printf("%d ", p[i].c[j]);
//            puts("");
//        }
//        }
        mem( vis );
        ans[1] = vis[1] = 1;
        printf("Case #%d: ", cas++);
        if( dfs( 1, 1 ) == 0 ){
            mem( vis );
            ans[1] = 2;
            vis[2] = 1;
            dfs( 2, 1 );
        }
//        int cnt = 1;
//        node tmp;
//        for( i = 1; i <= n; i ++ ){
//            for( j = 1; j <= n; j ++ )
//                tmp.c[j] = ff[i][j];
//            q[cnt++] = tmp;
//        }
//        for( i = 1; i <= n; i ++ ){
//            for( j = 1; j <= n; j ++ )
//                tmp.c[j] = ff[j][i];
//            q[cnt++] = tmp;
//        }
//        sort( p+1, p+2*n+1, cmp );
//        sort( q+1, q+2*n+1, cmp );
//        int fl = 0;
//        for( i = 1; i <= 2*n; i ++ ){
//            if( same( p[i], q[i] ) != 0 ){
//                fl = 1;
//                break;
//            }
//        }
//        printf("%d\n", fl);
    }
}
