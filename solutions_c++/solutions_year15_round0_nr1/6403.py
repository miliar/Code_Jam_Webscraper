#include<iostream>
#include <string>
using namespace std;

int main()
{
	int T, *audience, max_shy, total_clapping;
	string s;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int num_friends = 0;

		cin >> max_shy >> s;

		total_clapping = 0;

		for (int j = 0; j < s.length(); j++)
		{
			int temp_friends = 0;
			if (total_clapping < j)
			{
				temp_friends = j - total_clapping;
				num_friends += temp_friends;
			}

			total_clapping += (s[j] - 48) + temp_friends;
		}
		cout << "Case #" << i + 1 << ": " << num_friends << endl;
	}
	return 0;
}