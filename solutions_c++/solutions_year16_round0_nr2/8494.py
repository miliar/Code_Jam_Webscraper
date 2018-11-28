#include <iostream>
#include <string>

using namespace std;

void main()
{
	int T;
	cin >> T;

	for (int i = 0; i < T; ++i)
	{
		string pancake_happiness;
		cin >> pancake_happiness;

		int num_maneuvers = 0;

		const int length = pancake_happiness.length();

		bool top_is_happy = pancake_happiness[0] == '+';

		for (int j = 1; j < length; ++j)
		{
			if ((pancake_happiness[j] == '+') != top_is_happy)
			{
				++num_maneuvers;
				top_is_happy = !top_is_happy;
			}
		}

		if (!top_is_happy)
		{
			++num_maneuvers;
		}

		cout << "Case #" << i + 1 << ": " << num_maneuvers << endl;
	}
}
