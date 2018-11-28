#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <algorithm>

#include <boost/unordered_set.hpp>
#include <boost/foreach.hpp>
#include <boost/range/irange.hpp>

using namespace boost;
using namespace std;

int main(int argc, char * argv[])
{
  
    int T;
  
  cin >> T;
  
  BOOST_FOREACH(int t, irange(0, T))
  {
    int D;
    cin >> D;
    
    std::vector<int> P;
    P.resize(D);
    BOOST_FOREACH(int d, irange(0, D))
    {
      cin >> P[d];
    }
    
    /*int P_size = P.size();
    BOOST_FOREACH(int i, irange(0, (int)(1000 - P.size())))
    {
      P.push_back(P[i % P_size]);
    }*/
    
    // std::sort(P.rbegin(), P.rend());
    
    /*int P_max = *max_element(P.begin(), P.end());
    
    std::vector<int> counts;
    counts.resize(P_max);
    
    BOOST_FOREACH(int P_i, P)
    {
      counts[P_i-1]++;
    }*/
    
    
    int best_minutes = 1000;
    
    for (int normal_minutes = 1; normal_minutes < 1000; normal_minutes++)
    {
      int special_minutes = 0;
      BOOST_FOREACH(int P_i, P)
      {
	if (P_i > normal_minutes)
	{
	  special_minutes += P_i / normal_minutes;
	  
	  if (P_i % normal_minutes == 0)
	  {
	    special_minutes--;
	  }
	}
      }
      
      if (normal_minutes + special_minutes < best_minutes)
      {
	best_minutes = normal_minutes + special_minutes;
      }
      
    }
    
    
    cout << "Case #" << (t+1) << ": " << best_minutes << endl;
	  
  }
}