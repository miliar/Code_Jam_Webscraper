#include <stdio.h>
#include <stdlib.h>
#include <math.h>

bool isPosible( int * lawn, int width, int height )
{
  int current;
  int left;
  int right;
  int up;
  int down;

  bool horizontalBlocked = false;
  bool verticalBlocked = false;

  for ( int jj = 0; jj < height; ++jj )
  {
    for ( int ii = 0; ii < width; ++ii )
    {
      horizontalBlocked = false;
      verticalBlocked   = false;
      current = lawn[ ii + ( jj * width ) ];

      for ( int index = ii + 1; index < width; ++index )
      {
        right = lawn[ ( index ) + ( jj * width ) ];
        if ( right > current )
        {
          horizontalBlocked = true;
          break;
        }
      }
      for ( int index = 0; index < ii; ++index )
      {
        left = lawn[ ( index ) + ( jj * width ) ];
        if ( left > current )
        {
          horizontalBlocked = true;
          break;
        }
      }
      for ( int index = jj; index < height; ++index )
      {
        down = lawn[ ( ii ) + ( index * width ) ];
        if ( down > current )
        {
          verticalBlocked = true;
          break;
        }
      }
      for ( int index = 0; index < jj; ++index )
      {
        up = lawn[ ( ii ) + ( index * width ) ];
        if ( up > current )
        {
          verticalBlocked = true;
          break;
        }
      }

      if ( horizontalBlocked && verticalBlocked )
      {
        return false;
      }
    }
  }

  return true;
}

int main( void )
{
  int    numCases = 0;
  FILE * input  = fopen( "C:\\Users\\Tiago\\Dropbox\\GoogleCodeJam2013\\QualificationRound\\ProblemB\\input.txt", "rt" );
  FILE * output = fopen( "C:\\Users\\Tiago\\Dropbox\\GoogleCodeJam2013\\QualificationRound\\ProblemB\\output.txt", "wt" );

  int * lawn = NULL;
  int width, height;

  fscanf( input, " %d", &numCases );

  for ( int ii = 1; ii <= numCases; ++ii )
  {
    fscanf( input, " %d %d", &height, &width );

    lawn = ( int * ) calloc( width * height, sizeof( int ) );

    for ( int index = 0; index < width * height; ++index )
    {
      fscanf( input, " %d", &( lawn[ index ] ) );
    }

    fprintf( output, "Case #%d: %s\n", ii, ( isPosible( lawn, width, height ) ) ? "YES" : "NO" );
  }
}