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
    int N;
    
    cin >> N;
    
    std::vector<int> m;
    m.resize(N);
   
    
    
    BOOST_FOREACH(int n, irange(0, N))
    {
      cin >> m[n];
    }
    
    
    int mushrooms_eaten_1 = 0;
    {
    BOOST_FOREACH(int n, irange(0, N))
    {
      if (n >= 1)
      {
	int diff = m[n] - m[n-1];
	if (diff < 0)
	{
	  
	  mushrooms_eaten_1 += (-diff);
	}
      }
    }
    }
    
    
    int max_rate = 0;
    
    BOOST_FOREACH(int n, irange(0, N))
    {
      if (n >= 1)
      {
	int diff = m[n] - m[n-1];
	if (diff < 0)
	{
	  
	  if (-diff > max_rate)
	  {
	    max_rate = -diff;
	  }
	}
      }
    }
    
    int mushrooms_eaten_2 = 0;
    BOOST_FOREACH(int n, irange(0, N))
    {
      if (n >= 1)
      {
	if (m[n-1] <= max_rate)
	{
	  mushrooms_eaten_2 += m[n-1];
	}
	else
	{
	  mushrooms_eaten_2 += max_rate;
	}
      }
      
    }
    
    
    
    cout << "Case #" << (t+1) << ": " << mushrooms_eaten_1 << " " << mushrooms_eaten_2 << endl;
	  
  }
}