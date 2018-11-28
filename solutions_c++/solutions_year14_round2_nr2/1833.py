#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
	unsigned TCs = 0;
	cin >> TCs;
	for(unsigned i = 0; i < TCs; i++)
	{
		unsigned A, B, K;
		cin >> A >> B >> K;

		unsigned long answer = 0;
		for(unsigned j = 0; j < A; j++)
		{
			for(unsigned k = 0; k < B; k++)
			{
				if ((j & k) < K)
				{
					answer++;
				}
			}

		}

		cout << "Case #" << (i + 1) << ": " << answer << "\n";
	}

	return 0;
}