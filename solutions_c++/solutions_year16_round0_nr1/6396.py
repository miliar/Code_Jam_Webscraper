#include <iostream>
#include <set>

int main()
{
  int T;
  long long N;

  std::cin >> T;
  for ( int t = 1; t <= T; ++t )
    {
      long long n = 1;
      std::set<int> s;
      std::cin >> N;

      if ( N != 0 )
	{
	  for ( int i = 1; s.size() < 10; ++i )
	    {
	      n = i * N;
	      long long nt = n;
	      while ( nt )
		{
		  s.insert(nt % 10);
		  nt /= 10;
		}
	    }
	  std::cout << "Case #" << t << ": " << n << std::endl;
	}
      else
	std::cout << "Case #" << t << ": " << "INSOMNIA" << std::endl;
    }
  return 0;
}
