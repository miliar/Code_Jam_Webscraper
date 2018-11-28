// test 1
#include "stdafx.h"
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <set>
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text


int main()
{
	int t;
	std::string s;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) 
	{
		cin >> s;  

		// trim the end +'s
		s.erase(s.find_last_not_of("+") + 1);

		int a = 0;
		if (s.length() != 0)
		{
			char cur = s[0];
			a++;
			for (char c : s)
			{
				if (c != cur)
				{
					cur = c;
					a++;
				}
			}
		}

		cout << "Case #" << i << ": " << a << endl;

	}
    return 0;
}

