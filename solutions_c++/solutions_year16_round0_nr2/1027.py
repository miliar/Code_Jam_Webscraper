#include <iostream>
#include <string>
using namespace std;

void run();

int main()
{
	long T;
	cin >> T;

	for (int c = 1; c <= T; ++c)
	{
		cout << "Case #" << c << ": ";
		run();
	}
}

void run()
{
	string S;
	cin >> S;
	int flips = 0;

	// Moving top down, flip befpre every change to get all pancakes the same direction
	char current = S[0];
	for (int i = 1; i < S.length(); ++i)
	{
		if (S[i] != current)
		{
			current = S[i];
			++flips;
		}
	}

	// Now all pancakes facing the same way as bottom. If bottom us sad, make it happy :)
	if (S[S.length() - 1] == '-')
		++flips;

	cout << flips << endl;
}