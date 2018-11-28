#include <iostream>
#include <string>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		int smax;
		cin >> smax;
		string persons;
		cin >> persons;
		long long int sum = 0;
		int count = 0;

		for(int j = 0; j <= smax && sum < smax; j++)
		{
			if (sum < (j + 1) && persons[j] == '0')
			{
				sum++;
				count++;
			}
			else
			{
				sum += (persons[j] - '0');
			}

		}

		cout << "Case #" << (i + 1) << ": " << count << endl;
	}

	return 0;
}
