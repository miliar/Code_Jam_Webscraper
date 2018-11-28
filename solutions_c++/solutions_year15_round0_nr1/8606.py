#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main(void)
{
	size_t n = 0;
	cin >> n;

	for (size_t i = 0; i < n; ++i)
	{
		unsigned int max_shyness = 0;
		cin >> max_shyness;

		string s;
		cin >> s;

		unsigned int n_stand_up = s[0] - '0';
		unsigned int n_required = 0;

		for (size_t j = 1; j < s.length(); ++j)
		{
			if ((s[j] - '0') > 0 && n_stand_up < j)
			{
				n_required += j - n_stand_up;
				n_stand_up += j - n_stand_up;
			}

			n_stand_up += s[j] - '0';
		}

		printf("Case #%u: %u\n", i + 1, n_required);
	}

	fflush(stdout);

	return 0;
}