#include <iostream>
#include <string>
using namespace std;

int main()
{
	int T; cin >> T;
	for (int t = 0; t < T; t++)
	{
		int S;
		string audience;

		cin >> S >> audience;

		int current_peeps = 0;
		int peeps_needed = 0;
		for (int i = 0; i <= S; i++)
		{
			int x = audience[i] - '0';
			
			if (i > current_peeps)
			{
				peeps_needed += (i - current_peeps);
				current_peeps += (i - current_peeps);
			}
			current_peeps += x;
		}

		cout << "Case #" << t + 1 << ": " << peeps_needed << '\n';
	}

	return 0;
}