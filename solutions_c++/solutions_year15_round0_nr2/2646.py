#include <iostream>
#include <algorithm>

#define SIZE 1000

using namespace std;

int main()
{
	int T = 0;
	cin >> T;
	for(int i = 1; i <= T; i++)
	{
		int D;
		cin >> D;
		int P[SIZE];
		int maximum = 0;
		for(int j = 0; j < D; j++)
		{
			cin >> P[j];
			maximum = max(maximum, P[j]);
		}

		int minTimeTaken = 10000;
		for(int m = 1; m <= maximum; m++)
		{
			int splits = 0;
			for(int j = 0; j < D; j++)
			{
				int s = P[j] / m;
				if((P[j] % m) == 0)
				{
					s--;
				}
				splits += s;
			}
			int timeTaken = splits + m;
			minTimeTaken = min(minTimeTaken,timeTaken);
		}
		cout << "Case #" << i << ": " << minTimeTaken << endl;
	}
}