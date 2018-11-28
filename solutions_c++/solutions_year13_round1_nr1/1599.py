#include <iostream>
using namespace std;

int main()
{
	int t;
	int rad;
	int paint;
	int count;

	cin >> t;

	for(int i = 0; i < t; i++)
	{
		count = 0;

		cin >> rad >> paint;

		int black = 1, white = 0;

		while((rad + black) * (rad + black) - (rad + white) * (rad + white) <= paint)
		{
			count++;
			paint -= (rad + black) * (rad + black) - (rad + white) * (rad + white);
			black += 2;
			white += 2;
		}

		cout << "Case #" << i + 1 << ": " << count << endl;
	}

	return 0;
}