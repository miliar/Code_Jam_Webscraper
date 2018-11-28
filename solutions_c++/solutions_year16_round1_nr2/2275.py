#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int N;
		cin >> N;
		int count[2501];
		for (int j = 0; j < 2501; j++)
		{
			count[j] = 0;
		}

		int number;

		for (int j = 0; j < 2*N*N - N; j++)
		{
			cin >> number;
			count[number] += 1;
		}

		cout << "Case #" << i+1 << ": ";

		for (int j = 0; j < 2501; j++)
		{
			if (count[j] % 2 == 1)
			{
				cout << j << " ";
			}
		}

		cout << endl;
	}
}