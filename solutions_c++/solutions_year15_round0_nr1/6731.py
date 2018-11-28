#include <iostream>

using namespace std;

int main(void)
{
	int t, smax;

	int arr[1001];

	char temp;

	cin >> t;

	for(int i = 1; i <= t; i++)
	{
		int out = 0;
		int sum = 0;

		cin >> smax;

		for(int j = 0; j <= smax; j++)
		{
			cin >> temp;
			arr[j] = temp - '0';
		}

		for(int j = 0; j <= smax; j++)
		{
			sum += arr[j];

			if(sum > j)
				continue;
			out++;
			sum++;
		}
		
		cout << "Case #" << i << ": " << out << endl;
	}
	
	return 0;
}
