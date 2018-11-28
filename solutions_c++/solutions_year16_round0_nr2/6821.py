#include <iostream>
#include <stdint.h>
#include <string>

using namespace std;

char NotSign(char sign)
{
	if (sign == '+')
		return '-';
	return '+';
}

void Flip(string& s, uint32_t flipIndex)
{
	int32_t left = 0;
	int32_t right = flipIndex;

	while (left <= right)
	{
		char temp = NotSign(s[right]);
		s[right] = NotSign(s[left]);
		s[left] = temp;
		right--;
		left++;
	}
}

void main()
{
	unsigned int testCases;
	cin >> testCases;
	for (unsigned int t = 1; t <= testCases; t++)
	{
		string s;
		cin >> s;
		uint32_t result = 0;
		uint32_t len = s.length();
		for (;;)
		{
			uint32_t flipIndex = 0;
			bool done = true;
			for (int i = 0; i < len; i++)
			{
				if (s[i] == '-')
				{
					done = false;
					break;
				}
			}
			if (done)
				break;
			
			if (s[0] == '+')
			{
				for (int i = 0; i < len; i++)
				{
					if (s[i] == '-')
						break;
					flipIndex = i;
				}
				Flip(s, flipIndex);
				result++;
			}
			else
			{
				for (int i = 0; i < len; i++)
				{
					if (s[i] == '-')
						flipIndex = i;
				}
				Flip(s, flipIndex);
				result++;
			}
		}
		cout << "Case #" << t << ": " << result << endl;
	}
}