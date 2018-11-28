#include<iostream>
#include<string>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;

bool sync_with_stdio( bool sync = false );

int tot;
char s[ 102 ];
int n, m, cnt;
int cc[ 102 ], mx[ 102 ];

void dfs( int q, int p )
{
  if( q > m )
    return ;
  else if( p > m )
    {
      //for( int i = q + 1; i < m ; ++ i )
      //cc[ i ] = 0;
      cc[ q ] = 0;
      mx[ q ] = 0;
      dfs( q + 1, q + 1 );
    }
  else
    {
      if( s[ p ] not_eq 'a' &&
          s[ p ] not_eq 'e' &&
          s[ p ] not_eq 'i' &&
          s[ p ] not_eq 'o' &&
          s[ p ] not_eq 'u')
        cc[ p ] = cc[ p - 1 ] + 1;
      else
        cc[ p ] = 0;
      mx[ p ] = max( cc[ p ] , mx[ p - 1 ] );
      //for( int i = q ; i <= m ; ++ i ) cout<<cc[ i ]<<" "; cout<<"\n";
      if( mx[ p ] >= n ) 
        {
          //cout<<q<<" "<<p<<"\n";
          //for( int i = q ; i <= m ; ++ i ) cout<<cc[ i ]<<" "; cout<<"\n";
          ++ cnt;
        }
      dfs( q , p + 1 );
    }
  return ;
}

int main()
{
  int t = 0;
  cin>>tot;
  while( t ++ < tot )
    {
      cin>>s+1>>n;
      cnt = 0;
      m = strlen( s + 1);
      memset( cc , 0 , sizeof( cc ) );
      memset( mx , 0 , sizeof( mx ) );
      dfs( 1 , 1 );
      
      cout<<"Case #"<<t<<": "<<cnt<<"\n";
    }
  return 0;
}
