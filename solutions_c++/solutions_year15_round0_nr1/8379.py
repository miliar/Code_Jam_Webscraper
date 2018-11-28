#include <iostream>
#include <string>

using namespace std;

int main()
{
	size_t T;
	size_t S_max;
	string S;
	size_t current;
	size_t needed;

	cin >> T;

	for(size_t i=0; i < T; ++i)
	{
		cin >> S_max;
		cin >> S;

		current = S[0] - '0';
		needed = 0;

		for(size_t k=1; k <= S_max; ++k)
		{
			while(current < k)
			{
				needed += 1;
				current += 1;
			}

			current += S[k] - '0';
		}

		cout << "Case #" << i+1 << ": " << needed << endl; 
	}
}