#include <iostream>
#include <cmath>
#define ULL unsigned long long
using std::cin;
using std::cout;
using std::endl;
using std::pow;
using std::sqrt;


inline int is_prime( ULL n )
{
  for (int x = sqrt(n); x > 1; --x )
      if ( n % x == 0 ) return x;
  return -1;
}


inline ULL expand ( int x )
{
  ULL a = 0;
  int cnt = 0;
  while ( x > 0 )
    {
      a = a + pow(10, cnt) * ( x % 2 );
      x >>= 1;
      ++ cnt;
    }
  // cout << cnt << " " << endl;
  if (cnt == 16 and a % 2 == 1)
    return a;
  return -1;
}


int sol2( ULL a)
{
  ULL p, t;
  int cnt, div;
  int d[10];
  for ( int base = 2; base <= 10; ++ base)
    {
      p = 0;
      t = a;
      cnt = 0;
      while ( t > 0 )
        {
          if ( t % 10 == 1 )
            p += pow(base, cnt);
          t /= 10;
          ++ cnt;
        }
      // cout << p << endl;
      div = is_prime(p);
      if ( div != -1 ) d[base] = div;
      else return 0;
    }
  cout << a << " ";
  for ( int base = 2; base <= 10; ++ base )
    {
      cout << d[ base ];
      if ( base == 10 ) cout << endl;
      else cout << " ";
    }
  return 1;
}


void sol()
{
  // int cnt = 0;
  int ans = 0;
  for ( int x = (1 << 15); x < (1 << 16); ++ x )
  // for ( int x = 9; x < 10; ++ x )
    {
      ULL a = expand(x);
      if ( a != -1 )
        {
          // cnt += 1;
          ans += sol2(a);
          if (ans == 50) return ;
          // cout << s << " "<< x << endl;
        }
    }
  return ;
}


int main()
{
  cout << "Case #1:" << endl;
  sol();
  return 0;
}
