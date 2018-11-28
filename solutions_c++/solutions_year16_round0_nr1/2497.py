// test 1
#include "stdafx.h"
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <set>
using namespace std;  // since cin and cout are both in namespace std, this saves some text


int main()
{
	int t, n, m;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) 
	{
		cin >> n;  
	
		if (n == 0)
		{
			cout << "Case #" << i << ": " << "INSOMNIA" << endl;
		}
		else
		{
			int loops = 0;
			int original_num = n;
			std::set<int> answers;
			do
			{
				loops++;
				int num = original_num * loops;

				while (num > 0)
				{
					int d = num % 10;
					answers.insert(d);
					num /= 10;
				}
			} while (answers.size() != 10);
			cout << "Case #" << i << ": " << original_num * loops << endl;
		}
		// do sheep
		int answer = -1;

	}
    return 0;
}

