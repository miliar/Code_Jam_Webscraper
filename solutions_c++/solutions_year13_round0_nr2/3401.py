#include <cstdio>
#include <cstdint>
#include <cstring>
#include <cassert>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <iostream>
#include <sstream>

int main( int argn, char** argv )
{
  int ncases;
  scanf("%d",&ncases);
  for ( int icase = 0; icase<ncases; ++icase )
  {
    int N, M;
    scanf("%d%d", &N, &M );
    
    std::vector<bool> moaned( N*M );
    std::vector<int> height( N*M );

    for ( int i = 0; i < N; ++i )
      for ( int j = 0; j < M; ++j )
	scanf("%d", &height[i*M+j] );

    // left to right / right to left
    for ( int h = 100; h >= 1; --h )
    {
      for ( int i = 0; i < N; ++i )
      {
	bool possibru = true;
	for ( int j = 0; j < M; ++j )
	{
	  if ( height[ i*M+j ] > h )
	  {
	    possibru = false;
	    break;
	  }
	}
	if ( possibru )
	{
	  for ( int j = 0; j < M; ++j )
	  {
	    if ( height[ i*M+j ] == h )
	    {
	      moaned[ i*M+j ] = true;
	    }
	  }
	}
      }
    }

    // top to bottom / bottom to top
    for ( int h = 100; h >= 1; --h )
    {
      for ( int i = 0; i < M; ++i )
      {
	bool possibru = true;
	for ( int j = 0; j < N; ++j )
	{
	  if ( height[ i+j*M ] > h )
	  {
	    possibru = false;
	    break;
	  }
	}
	if ( possibru )
	{
	  for ( int j = 0; j < N; ++j )
	  {
	    if ( height[ i+j*M ] == h )
	    {
	      moaned[ i+j*M ] = true;
	    }
	  }
	}
      }
    }

    
    printf("Case #%d: %s\n",icase+1,
      std::find( std::begin(moaned), std::end(moaned), false ) == std::end(moaned) ?
      "YES" : "NO"
	   );
  }
  return 0;
}
