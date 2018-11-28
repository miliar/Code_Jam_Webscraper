#include <iostream>
#include <string>
#include <vector>
#include <list>

#include <boost/unordered_set.hpp>
#include <boost/foreach.hpp>
#include <boost/range/irange.hpp>

using namespace boost;
using namespace std;

int main(int argc, char **argv)
{
  int T;
  
  cin >> T;
  
  BOOST_FOREACH(int t, irange(0, T))
  {
    int S_max;
    cin >> S_max;
    
    string S;
    cin >> S;
    
    int people_standing = 0;
    int shyness = 0;
    int friends = 0;
    
    
    BOOST_FOREACH(char c, S)
    {
      int new_friends = 0;
      unsigned char S_i = (c - '0');
      
      if (people_standing >= shyness)
      {
	people_standing += S_i;
      }
      else
      {
	new_friends += shyness - people_standing;
	people_standing += new_friends + S_i;
      }
      
      shyness += 1;
      friends += new_friends;
    }
    
    cout << "Case #" << (t+1) << ": " << friends << endl;
    
  }
  
  
    return 0;
}
