#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <fstream>
#include <string>
#include <set>
#include <vector>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

int last_num(int input)
{
	set<int> bin;
	int y = 0;

	for (int i = 1; i < 10000011; ++i)
 	{
		for (int x = (i * input); x > 0;)
	    {
	    	y = x % 10;
	    	bin.insert(y);
	    	if (bin.size() == 10)
	    		return (i * input);
	    	x = x / 10;
	    }
	}


	return input;
}

int main() 
{ 
  int t, n, m;
  
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  //cout << "Number of test cases : " << t << endl;

  for (int i = 1; i <= t; ++i) 
  {
    cin >> n;  // read n and then m.

    if (n == 0)
   		cout << "Case #" << i << ": " << "INSOMNIA" << endl;
   	else
    	cout << "Case #" << i << ": " << (last_num(n)) << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }


  return 0;
}

