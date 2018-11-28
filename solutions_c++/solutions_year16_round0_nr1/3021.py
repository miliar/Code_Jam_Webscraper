#include <iostream>


unsigned digits(unsigned x)
{
  if ( x == 0 )
    return 1;
  unsigned r = 0;
  while ( x > 0 )
  {
    r |= 1U << (x%10);
    x /= 10;
  }
  return r;
}


unsigned count(unsigned x)
{
  unsigned m = 0;
  unsigned ix = 0;
  do
  {
    ix += x;
    m |= digits(ix);
  } while ( m != 1023 );
  return ix;
}


int main()
{
  int T;
  std::cin >> T;
  for ( int t = 1; t <= T; ++t )
  {
    unsigned N;
    std::cin >> N;
    std::cout << "Case #" << t << ": ";
    if ( N == 0 )
      std::cout << "INSOMNIA\n";
    else
      std::cout << count(N) << '\n';
  }
  return 0;
}
