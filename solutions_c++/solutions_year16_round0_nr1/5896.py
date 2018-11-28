// future_glimpse.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

// include c++ headers
#include <iostream>
#include <unordered_map>
#include <map>
#include <set>
#include <cstdio>
#include <string>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int t,n;
	cin >> t;

	for(int i=1; i<=t; i++)
	{
		cin >> n;

		if(n==0)
		{
			cout << "Case #" << i << ": " << "INSOMNIA" << endl;
		}
		else
		{
			set<int> s;
			int j=1;

			while(true)
			{
				int num = j*n;

				while(num)
				{
					int d = num%10;
					s.insert(d);
					num/=10;
				}

				if(s.size()==10)
				{
						break;
				}
				++j;
			}

			cout << "Case #" << i << ": " << j*n << endl;
		}
	}

	return 0;
}

