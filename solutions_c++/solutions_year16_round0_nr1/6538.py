#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	int testCases;
	long long int N, K; //Starting variables
	string a, b; //Starting variables
	cin >> testCases;

	int t = 1;
	while (testCases--)
	{
		cin >> N;
		if (N == 0)
			cout << "Case #" << t << ": " << "INSOMNIA" << endl;
		else
		{
			long long int i = 1;
			int digitCount = 0;
			int count[10] = { 0 };
			while (true)
			{
				K = i * N;
				while (K > 0)
				{
					int digit = K % 10;
					if (count[digit] == 0)
					{
						++count[digit];
						++digitCount;
					}
					K = K / 10;
				}
				if (digitCount == 10)
					break;
				i++;
			}
			cout << "Case #" << t << ": " << i*N << endl;
		}
		t++;
	}

	return 0;
}