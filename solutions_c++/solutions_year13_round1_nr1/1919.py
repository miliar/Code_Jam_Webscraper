#define _local

// codejam_r1a.cpp : Defines the entry point for the console application.
//

/*
#include <stdio.h>

#define pb push_back


int main(int argc, char* argv[])
{
#ifdef local
 freopen("a.in", "r", stdin);
#endif
	return 0;
}
*/

/// A ///

#define _USE_MATH_DEFINES 
#include <stdio.h>
#include <cmath>

#define pb push_back

int T;
long long r,t;

int areac(int r)
{
 return r*r;
}

int pintura(int r)
{
 return (areac(r+1) - areac(r));
}

long long paint(long long n)
{
 return n*(2*r+1)+2*n*(n-1);
}

int main(int argc, char* argv[])
{
#ifdef local
 freopen("as.in", "r", stdin);
 freopen("as.out", "w", stdout);
#endif
 scanf("%d", &T);
 for(int _t=0;_t<T;_t++)
 {
  printf("Case #%d: ", _t+1);
  scanf("%I64d %I64d", &r, &t);

  long long n0 = 1;
  long long n1 = 1000000000;

  long long m;
  bool ledi = false;

  while(n1>n0+1)
  {
   m = (n0+n1)/2;
   long long p = paint(m);
   if(p < t) n0 = m;
   else if(p > t) n1 = m;
   else // ==
   {
    ledi = true;

    break;
   }
  }

  if(!ledi){
   long long p0 = paint(n0);
   long long p1 = paint(n1);
   if(p1<=t) m = n1;
   else m = n0;
  }

  printf("%I64d\n", m);
 }
	return 0;
}
