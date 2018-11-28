//
//  Pancakes.cpp
//  
//
//  Created by Laszlo Majer on 09/04/16.
//
//

#include <iostream>
#include <string>


using namespace std;


int main()
{
	int T = 0;
	
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		unsigned long long result = 0;
		char prev;
		char curr;
		cin >> prev;
		
		while ((curr = cin.get()) != '\n' && !cin.eof())
		{
			if (curr != prev)
				++result;

			prev = curr;
		}
		
		if (prev == '-')
			++result;
		
		cout << "Case #" << i + 1 << ": " << result << endl;
	}
}

