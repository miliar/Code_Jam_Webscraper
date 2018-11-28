#include <stdio.h>
#include <math.h>

int reverseNumber( int number )
{
  int reverse = 0;
  while ( number != 0 )
  {
    reverse *= 10;
    reverse += number % 10;
    number /= 10;
  }

  return reverse;
}

bool isFair( int number )
{
  return ( number == reverseNumber( number ) );
}

int countFairAndSquare( int min, int max )
{
  int count = 0;
  int sq;
  for ( int index = min; index <= max; ++index )
  {
    sq = ( int ) sqrt( ( float )index );
    if ( sq * sq == index )
    {
      if ( isFair( index ) && isFair( sq ) )
      {
        ++count;
      }
    }
  }

  return count;
}

int main( void )
{
  int    numCases = 0;
  FILE * input  = fopen( "C:\\Users\\Tiago\\Dropbox\\GoogleCodeJam2013\\QualificationRound\\ProblemC\\input.txt", "rt" );
  FILE * output = fopen( "C:\\Users\\Tiago\\Dropbox\\GoogleCodeJam2013\\QualificationRound\\ProblemC\\output.txt", "wt" );

  int min, max;

  fscanf( input, " %d", &numCases );

  for ( int ii = 1; ii <= numCases; ++ii )
  {
    fscanf( input, " %d %d", &min, &max );
    fprintf( output, "Case #%d: %d\n", ii, countFairAndSquare( min, max ) );
  }
}