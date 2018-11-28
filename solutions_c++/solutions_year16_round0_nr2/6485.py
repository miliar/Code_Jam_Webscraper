#include <iostream>

int main()
{
  int T;
  std::string pancakes;

  std::cin >> T;
  for ( int t = 1; t <= T; ++t )
    {
      std::cin >> pancakes;
      char last = 'n';
      int c = 0;

      for ( int i = 0; i < pancakes.size(); ++i )
	{
	  if ( pancakes[i] == '-' )
	    {
	      if ( last == '+' )
		c += 1;
	      last = '-';
	    }
	  else if ( pancakes[i] == '+' )
	    {
	      if ( last == '-' )
		c += 1;
	      last = '+';
	    }
	}
      if ( pancakes[pancakes.size() - 1] == '-' )
	c += 1;

      std::cout << "Case #" << t << ": " << c << std::endl;
    }
  return 0;
}
