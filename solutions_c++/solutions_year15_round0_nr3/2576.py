#include <cstdio>

const int MAXS = 51000;

char str[MAXS];
int tree[MAXS];
int arr[MAXS];
bool leftBound[MAXS], rightBound[MAXS];

inline int left( int x ) { return (x<<1); }
inline int right( int x ) { return (x<<1)+1; }

inline int mult( int a, int b )
{
    int signal = 1 - 2 * int(a*b < 0);
    if ( a < 0 ) a = -a;
    if ( b < 0 ) b = -b;
    if ( a == 1 ) return signal * b;
    if ( b == 1 ) return signal * a;
    if ( a == 2 ) return signal * ( b == 2 ? -1 : b == 3 ? 4 : -3 );
    if ( a == 3 ) return signal * ( b == 2 ? -4 : b == 3 ? -1 : 2 );
    if ( a == 4 ) return signal * ( b == 2 ? 3 : b == 3 ? -2 : -1 );
}

void init()
{
    for ( int i = 0; i < MAXS; i++ ) tree[i] = 1;
}

void update( int node, int from, int to, int pos, int val )
{
    if ( from == to and from == pos )
        tree[node] = val;
    else if ( pos >= from and pos <= to )
    {
        int mid = (from+to)/2;
        update( left(node), from, mid, pos, val );
        update( right(node), mid+1, to, pos, val );
        tree[node] = mult( tree[left(node)], tree[right(node)] );
    }
}

int query( int node, int from, int to, int a, int b )
{
    if ( from >= a and to <= b ) return tree[node];
    if ( a > to or b < from ) return 1;
    int mid = (from+to)/2;
    return mult( query( left(node), from, mid, a, b ), query( right(node), mid+1, to, a, b ) );
}

int main()
{
    int T, L, X;
    scanf( "%d", &T );
    for ( int t = 1; t <= T; t++ )
    {
        scanf( "%d %d", &L, &X );
        scanf( "%s", str );
        init();
        for ( int i = 0; i < X; i++ )
            for ( int j = 0; j < L; j++ )
                switch (str[j])
                {
                    case '1': arr[i*L+j] = 1; break;
                    case 'i': arr[i*L+j] = 2; break;
                    case 'j': arr[i*L+j] = 3; break;
                    case 'k': arr[i*L+j] = 4; break;
    
                }
        L *= X;
        for ( int i = 0; i < L; i++ ) update( 1, 0, L-1, i, arr[i] );
        int curr = 1;
        for ( int i = 0; i < L; i++ )
        {
            curr = mult(curr,arr[i]);
            leftBound[i] = ( curr == 2 );
        }
        curr = 1;
        for ( int i = L-1; i >= 0; i-- )
        {
            curr = mult(arr[i],curr);
            rightBound[i] = ( curr == 4 );
        }

        bool possible = false;
        for ( int i = 0; i < L and not possible; i++ )
            for ( int j = L-1; j > 0 and not possible; j-- )
                if ( leftBound[i] and rightBound[j] and j-i >= 2 )
                    if ( query( 1, 0, L-1, i+1, j-1 ) == 3 ) possible = true;
        printf( "Case #%d: ", t );
        if ( possible ) printf( "YES\n" );
        else printf( "NO\n" );
    }
    return 0;
}
