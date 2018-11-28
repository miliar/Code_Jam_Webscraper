/*
 * a.cpp
 *
 *  Created on: May 12, 2013
 *      Author: firat
 */

#include <iostream>

#include <string>
using namespace std;

bool isvowel(char c)
{
	return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';

}

bool contain(const string& s, long k, long m, long L)
{
	long t = 0;
	bool started = false;
	for(long i = k; i <= m; i++)
	{
		if(!isvowel(s[i]))
		{
			started = true;
			t = t + 1;
			if(t == L)
			{
				return true;
			}
		}
		else
		{
			if(started)
			{
				if(t >= L)
				{
					return true;
				}
				t = 0;
				started = false;
			}
			else
			{
				t = 0;
				started = false;
			}
		}
	}
	return false;
}

int main()
{
	int T;
	cin >> T;
	for(int i = 0; i < T; i++)
	{
		string s;
		cin >> s;
		long L;
		cin >> L;
		long N = s.length();
		long count = 0;

		for(long k = 0; k < N; k++)
		{
			for(long m = k; m < N; m++)
			{
				if(contain(s, k, m, L))
				{
					count = count + N - m;
					break;
				}
			}
		}
		cout << "Case #" << i+1 << ": " <<  count << endl;


	}
	return 0;
}
