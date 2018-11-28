#include "stdio.h"
#include "utility"
#include "vector"
#include "algorithm"

using namespace std;

typedef pair<int,int> P;

const int INF = 1000000000;
const int MAX_N = 1010;

int dp[MAX_N];
int a[MAX_N];


int bit[MAX_N*2] , size;
void init( int s ){
  size = 1;
  while( size < s ) size *= 2;
  for( int i = 0; i < size; i++ ) bit[i] = 0;
}
void add( int k , int x ){
  while( k <= size ){
    bit[k] += x;
    k += k & -k;
  }
}
int sum( int k ){
  int res = 0;
  while( k > 0 ){
    res += bit[k];
    k -= k & -k;
  }
  return res;
}

int main(){
 
  int t;
  scanf( "%d" , &t );

  for( int tc = 1; tc <= t; tc++ ){

    int n;
    scanf( "%d" , &n );

    init( n );
    
    vector<P> all;

    for( int i = 0; i < n; i++ ){
      scanf( "%d" , &a[i] );
      all.push_back( P( a[i] , i ) );
      dp[i] = INF;
      add( i+1 , 1 );
    }


    sort( all.begin() , all.end() );

    int ans = 0;
    for( int i = 0; i < n; i++ ){
      int p = all[i].second+1;
      //printf( "%d %d %d %d\n" , p , sum(p-1) , sum(n) , sum(p) );
      ans += min( sum(p-1) , sum(n)-sum(p) );
      add( p , -1 );
    }

    printf( "Case #%d: %d\n" , tc , ans );

  }

  return 0;
}
