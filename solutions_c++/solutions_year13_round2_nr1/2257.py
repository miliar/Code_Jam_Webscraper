#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>

unsigned int minChagesToSove( unsigned int arminMoteSize, std::vector< unsigned int > otherMotesSizes )
{
  if ( otherMotesSizes.size( ) == 1 )
  {
    if ( arminMoteSize > otherMotesSizes[ 0 ] ) 
    {
      return 0;
    } else
    {
      return 1;
    }    
  }

  std::sort( otherMotesSizes.begin( ), otherMotesSizes.end( ) );

  if ( arminMoteSize > otherMotesSizes[ 0 ] )
  {
    return minChagesToSove( arminMoteSize + otherMotesSizes[ 0 ],
                            std::vector< unsigned int >( otherMotesSizes.begin( ) + 1, otherMotesSizes.end( ) ) );
  } else
  {
    unsigned int minChangesAdd = ( arminMoteSize > 1 ) ? minChagesToSove( arminMoteSize + arminMoteSize - 1, otherMotesSizes ) : UINT_MAX;
    unsigned int minChangesRem = minChagesToSove( arminMoteSize,
                                                  std::vector< unsigned int >( otherMotesSizes.begin( ) + 1, otherMotesSizes.end( ) ) );

    return 1 + ( ( minChangesAdd < minChangesRem ) ? minChangesAdd : minChangesRem );
  }
}

int main( void )
{
  int    numCases = 0;
  FILE * input    = fopen( "input.txt" , "rt" );
  FILE * output   = fopen( "output.txt", "wt" );

  /* Problem variables. */
  unsigned int arminMoteSize;
  unsigned int moteCount;
  unsigned int temp;
  std::vector< unsigned int > otherMotesSizes;

  fscanf( input, " %d", &numCases );

  for ( int caseID = 1; caseID <= numCases; ++caseID )
  {
    /* Read inputs. */
    fscanf( input, " %u %u", &arminMoteSize, &moteCount );
    otherMotesSizes.clear( );
    otherMotesSizes.reserve( moteCount );
    for ( unsigned int ii = 0; ii < moteCount; ++ii )
    {
      fscanf( input, " %u", &( temp ) );
      otherMotesSizes.push_back( temp );
    }

    /* Generate output. */
    fprintf( output, "Case #%d: %u\n", caseID, minChagesToSove( arminMoteSize, otherMotesSizes ) );
  }
}