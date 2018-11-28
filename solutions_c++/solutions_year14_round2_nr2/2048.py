#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int testcases;
	cin >> testcases;

	for(int i = 0; i < testcases; i++)
	{
		int result = 0;

		int A, B, K;
		cin >> A >> B >> K;

		for(int j = 0; j < A; j++)
		{
			for(int k = 0; k < B; k++)
			{
				if((j&k) < K) result++;
			}
		}

		cout << "Case #" <<  i + 1 << ": " << result << endl;
	}
}