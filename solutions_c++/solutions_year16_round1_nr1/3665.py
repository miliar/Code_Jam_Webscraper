#include <iostream>
#include <string>
#include <algorithm>
#include <list>

using namespace std;

int main()
{
	int test_case;
	string input,output;
	cin >> test_case;
	for(int t = 1; t <= test_case; ++t)
	{
		cin >> input;
		int len = input.size();
		output.resize(len);
		output[0] = input[0];
		for(int i = 1; i < len; ++i)
		{
				if(input[i] < output[0])
					output[i] = (input[i]);
				else
				{
					for(int j = i; j > 0; --j)
					{
						output[j] = output[j-1];
					}
					output[0] = input[i];
				}					
		}
		cout << "Case #" << t << ": " << output << "\n";
	}
}
