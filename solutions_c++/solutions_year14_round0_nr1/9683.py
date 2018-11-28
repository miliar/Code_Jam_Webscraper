#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int read()
{
  int x=0;
  int c=0;
  while( c<'0' || c>'9' )
    c = getc(stdin);

  while( c>='0' && c<='9' )
    {
      x = x*10 + c - '0';
      c = getc(stdin);
    }

  return x;
}

void write( int x )
{
  printf("%d\n",x);
}


void readrow( int row, int &a, int &b, int &c, int &d )
{
  char buff[256];

  for ( int i=1; i<=4; i++ )
    if ( i==row )
      {
	scanf( "%d %d %d %d\n", &a, &b, &c, &d );
      }
    else
      {
	gets(buff);
      }

}

void doprob( int n )
{
  int row = read();

  int a, b, c, d;
  readrow( row, a, b, c, d );

  char cards[16+1];
  memset( cards, 'N', 16+1 );

  cards[a] = 'Y';
  cards[b] = 'Y';
  cards[c] = 'Y';
  cards[d] = 'Y';

  row = read();
  readrow( row, a, b, c, d );
 
  int numhits = 0;
  int what;

  if ( cards[a] == 'Y' )
    {
      numhits++;
      what = a;
    }

  if ( cards[b] == 'Y' )
    {
      numhits++;
      what = b;
    }

  if ( cards[c] == 'Y' )
    {
      numhits++;
      what = c;
    }

  if ( cards[d] == 'Y' )
    {
      numhits++;
      what = d;
    }

  if ( numhits == 0 )
    printf( "Case #%d: Volunteer cheated!\n", n );
  else if ( numhits == 1 )
    printf( "Case #%d: %d\n", n, what );
  else
    printf( "Case #%d: Bad magician!\n", n );
}

int main(int argc, char **argv )
{
  int T = read();
  for(int i=1; i<=T; i++ )
    doprob(i);
}
