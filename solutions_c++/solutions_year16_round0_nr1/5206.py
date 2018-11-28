
#include <iostream>
#include <fstream>
#include <cstring>
#include <limits>
#include <array>
#include <algorithm>


using namespace std ;


int64_t solve(int64_t n)
{
  if (n == 0)
    return -1 ;

  array<int, 10> counter ;
  counter.fill(0) ;

  for (auto candidate = n ; candidate <= max(100L, n)*n ; candidate += n)
    {
      auto p = candidate ;
      while (true)
	{
	  int64_t rem = p / 10 ;
	  int digit = p - rem*10 ;
	  p = rem ;
	  if (counter[digit] == 0)
	    counter[digit] = 1 ;
	  if (rem == 0)
	    break ;
	} 
      if (find(begin(counter), end(counter), 0) == counter.end())
	return candidate ;
    }
  
  return -1 ;
}


int main(int argc, char* argv[])
{
  if (argc != 2)
    exit(1) ;

  ifstream input(argv[1]) ;
  if (input.fail())
    {
      cerr << "Could not open file " << argv[1] << "\n" ;
      exit(1) ;
    }

  unsigned int ncases ;
  input >> ncases ;
  input.ignore(numeric_limits<streamsize>::max(), '\n') ;

  for (unsigned int i = 0 ; i < ncases ; ++ i)
    {
      int64_t n ;
      input >> n ;
		
      cout << "Case #" << i + 1 << ": " ;
      int result = solve(n) ;
      if (result == -1)
	cout << "INSOMNIA\n" ;
      else
	cout << result << "\n" ;
    }
}

