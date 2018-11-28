#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <iomanip>
#include <fstream>
#include <stdlib.h> 
#include  <iterator>
#include <stdexcept>
#include <algorithm>
#include <sstream>

using namespace std;

template<typename T> T from_str(std::string key)
{
      std::stringstream ss(key);
      T convertedValue;
      if ( ss >> convertedValue ) return convertedValue;
      else throw std::runtime_error("conversion failed");
}



int main()
{
  string line;
  ifstream input ("A-large.in");
  ofstream output ("A-large.out");
  unsigned int nb_test;
  unsigned int max_shy;
  std::vector<unsigned int> shy;
  unsigned int nb_clap = 0;
  unsigned int added;

  if (input.is_open())
    {
      
      getline(input,line);
      nb_test = from_str<unsigned int>(line);
      for(unsigned int kk=1; kk <= nb_test; ++kk)
	{
	  nb_clap = 0;
	  added = 0;
	  shy.clear();
	  getline(input,line);
	  int nb_space = line.find_first_of(" ");
	  max_shy = from_str<unsigned int>(line.substr(0,line.find_first_of(" ")));
	  for(unsigned int ll=0; ll <= max_shy; ++ll)
	    {
	      shy.push_back(from_str<unsigned int>(line.substr(ll+1+nb_space,1)));
	    }

	  for(unsigned int ll=0; ll <= max_shy; ++ll)
	    {
	      if(ll <= nb_clap)
		{
		  nb_clap += shy[ll];
		}
	      else
		{
		  added += ll - nb_clap;
		  nb_clap += shy[ll] + ll - nb_clap;
		}
	    }
	  if(output.is_open())
	    {
	      output << "Case #" << kk << ": " << added << endl;

	    }
	}

      input.close();
      output.close();
    }
}



