
#include <iostream>
#include <fstream>
#include <cstring>
#include <limits>
#include <array>
#include <algorithm>


using namespace std ;


int solve(const char* stack, size_t idx)
{
  // if (idx == 0)
  //   return *stack == '+' ? 0 : 1 ;
  
  if (stack[idx] == '+')
    {
      while (idx != 0 && stack[idx] == '+')
	-- idx ;
      if (stack[idx] == '-')
	return solve(stack, idx) ;
      else
	return 0 ;
    }
  else
    { 
      while (idx != 0 && stack[idx] == '-')
	-- idx ;
      if (stack[idx] == '+')
	return solve(stack, idx) + 2 ;
      else
	return 1 ;
    }
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

  const int max = 1000 ;
  const int filler = '\0' ;
	
  unsigned int ncases ;
  input >> ncases ;
  input.ignore(numeric_limits<streamsize>::max(), '\n') ;

  for (unsigned int i = 0 ; i < ncases ; ++ i)
    {
      char line[max] ;
      memset(line, filler, max) ;
      input.getline(line, max) ;
      
      cout << "Case #" << i + 1 << ": " << solve(line, strlen(line) - 1) << "\n" ;
    }
}

