#include <cstdio>
#include <cstdint>
#include <cstring>
#include <cmath>
#include <cassert>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <iostream>
#include <sstream>

bool is_palindrom( long long num )
{
  int a[20];
  int ai = 0;
  while ( num > 0 )
  {
    a[ai++]=num%10;
    num/=10;
  }
  for ( int i = 0; i < ai/2; ++i )
  {
    if ( a[i] != a[ai-i-1] )
      return false;
  }
  return true;
}


void check( int num1, int num2, std::vector< long long >& fsquare )
{
  long long f2 = (long long)num2*num2;
  if ( is_palindrom( f2 ) )
    fsquare.push_back( f2 );
  long long f1 = (long long)num1*num1;
  if ( is_palindrom( f1 ) )
    fsquare.push_back( f1 );
}


int main( int argn, char** argv )
{

  // do preprocessing
  std::vector< long long > fsquare;

  for (int i=1;i<=9;++i)
  {
    int num1 = i * 10 + i;
    int num2 = i;
    check( num1, num2, fsquare );
  }

  for (int i=1;i<=9;++i)
    for (int j=0;j<=9;++j)
    {
      int num1 =  i * 1000 + j * 100 + j * 10 + i;
      int num2 =  i * 100 + j * 10 + i;
      check( num1, num2, fsquare );
    }
  

  for (int i=1;i<=9;++i)
    for (int j=0;j<=9;++j)
      for (int k=0;k<=9;++k)
      {
	int num1 = i * 100000 + j * 10000 + k * 1000 + k * 100 + j * 10 + i ;
	int num2 = i * 10000 + j * 1000 + k * 100 + j * 10 + i ;
	check( num1, num2, fsquare );
      }
  
  std::sort( std::begin(fsquare), std::end(fsquare) );

  int ncases;
  scanf("%d",&ncases);
  for ( int icase = 0; icase<ncases; ++icase )
  {
    long long A, B;
    scanf("%lld%lld", &A, &B );

    auto it_l = std::lower_bound( std::begin(fsquare), std::end(fsquare), A );
    auto it_r = std::lower_bound( std::begin(fsquare), std::end(fsquare), B );

    // for ( auto it = it_l; it!=it_r; ++it )
    //   printf("%lld ",*it);
    // if ( it_r != std::end(fsquare) )
    //   printf("%lld\n", *it_r );
    
    printf("Case #%d: %zd\n",icase+1,it_r-it_l+(*it_r==B));
  }
  return 0;
}
