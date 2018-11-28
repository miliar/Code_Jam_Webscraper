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
		cout << "Case #" << c << ":";
		run();
	}
}

void run()
{
	int K, C, S;
	cin >> K >> C >> S;

	if (S < ((float)K / (float)C))
	{
		cout << " IMPOSSIBLE" << endl;
		return;
	}

	
	for (int p = 0; p < K;)
	{
		unsigned long long index = 1; // output is 1-indexed
		for (int depth = 1; depth <= C && p < K; ++depth, ++p)
		{
			index += p * (unsigned long long)pow(K, C - depth);
		}
		cout << " " << index;
	}
	cout << endl;
}