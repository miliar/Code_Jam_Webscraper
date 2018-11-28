#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	int test_case;
	string pancakes;
	long answer;
	cin >> test_case;
	for(int i = 1; i <= test_case; ++i)
	{
		cin >> pancakes;
		answer = 0;
		bool change = false;
		for(int j = pancakes.size()-1; j >= 0; --j)
		{
			if(change == false)
			{
				if(pancakes[j] == '-')
				{
					++answer;
					change = true;
				}
			}
			else
			{
				if(pancakes[j] == '+')
				{
					++answer;
					change = false;
				}
			}
		}
		cout << "Case #" << i << ": " << answer << "\n";
	}
}
