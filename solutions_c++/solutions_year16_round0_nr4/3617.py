
#include <iostream>
#include <fstream>
#include <cstring>
#include <limits>
#include <vector>
#include <algorithm>


using namespace std ;


vector<int> solve(int k, int c, int s)
{
  vector<int> v ;
  
  if (k == 1)
    v.push_back(1) ;
  else if (k == 2 && c == 1)
    {
      v.push_back(1) ;
      v.push_back(2) ;
    }
  else
    {
      for (int i = 1 ; i <= k ; ++ i)
	v.push_back(i) ;
    }
  return v ;
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
      unsigned int k, c, s ;
      input >> k >> c >> s ;
      
      cout << "Case #" << i + 1 << ": " ;
      auto v = solve(k, c, s) ;
      if (v.size() <= s)
	{
	  for (auto tile: v)
	    cout << tile << " " ;
	}
      else cout << "IMPOSSIBLE" ;
      cout << "\n" ;
    }
}

