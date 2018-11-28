#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>

using namespace std;

#define MAX 100
#define MAX_A 1000000
#define INF 1000000000
int S[MAX+10];
pair<long long, long long> dp[2][MAX+10]; //0 exclude 1 include

int find( int from, int to ){
    if( from == 1 )
        return INF;
    int moves = 0;
    while( from <= to ){
        from = from*2 - 1;
        moves++;
        //printf( "from : %d, moves : %d and to : %d\n", from, moves, to );
    }
    return moves;
}

int find_weight( int from, int to ){
    if( from == 1 )
        return INF;
    int moves = 0;
    while( from <= to ){
        from = from*2 - 1;
        moves++;
    }
    return from + to;
}

int performtest(){
    int A, N;
    scanf( "%d %d", &A, &N );
    for( int i=1; i<=N; i++ )
        scanf( "%d", S + i );
    sort( S + 1, S + 1 + N );
    dp[0][1].first = 1; dp[0][1].second = A;
    dp[1][1].first = find( A, S[1] ); dp[1][1].second = find_weight( A, S[1] );
    for( int i=2; i<=N; i++ ){
        dp[0][i] = ( dp[0][i-1].first <= dp[1][i-1].first ) ? dp[0][i-1] : dp[1][i-1];
        dp[0][i].first++;
        if( dp[0][i-1].first + find( dp[0][i-1].second, S[i] ) <= dp[1][i-1].first + find( dp[1][i-1].second, S[i] ) ){
            dp[1][i].first = dp[0][i-1].first + find( dp[0][i-1].second, S[i] );
            dp[1][i].second = find_weight( dp[0][i-1].second, S[i] );
        } else {
            dp[1][i].first = dp[1][i-1].first + find( dp[1][i-1].second, S[i] );
            dp[1][i].second = find_weight( dp[1][i-1].second, S[i] );
        }
        //printf( "dp[0][%d] : %d dp[1][%d] : %d\n", i, dp[0][i].first, i, dp[1][i].first );
    }
    return min( dp[0][N].first, dp[1][N].first );
}

int main(){
    int T;
    scanf( "%d", &T );
    for( int i=1; i<=T; i++ ){
        printf( "Case #%d: %d\n", i, performtest() );
    }
    return 0;
}
