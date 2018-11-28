#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <string>

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


std::map<std::string,double> cache;

double solve( double C, double speed, double F, double X )
{
  if ( speed / (speed+F) > ( X-C )/X )
    return X/speed;
  else
    return C/speed + solve(C,speed+F,F,X);
}

int main(int argc, char **argv )
{
  int T = read();

  for( int i=1; i<=T; i++ )
    {
      char buff[256];
      gets(buff);
      double C, F, X;
      sscanf(buff, "%lf %lf %lf\n", &C, &F, &X);

      double t = solve(C,2,F,X);
      printf( "Case #%d: %.7lf\n", i, t );
    }

}
