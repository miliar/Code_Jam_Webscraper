#include <iostream>
//#include <vector>
//#include <unordered_map>
//#include <algorithm>
//#include <functional>

using namespace std;


void execute()
{
	// Input
	int delta;
	cin >> delta;

	// INSOMNIA only happens when the input number is 0
	if (delta == 0)
	{
		cout << "INSOMNIA" << endl;
		return;
	}

	int arr[10] = { 0 }, count = 0;
	int total = delta;

	// Whatever you do, mathematically the routine meets return statement.
	while (1)
	{
		int tmp = total;

		// Check all digit was traversed. I will not use unordered_map, rather use count variable for performance.
		while (tmp)
		{
			if (arr[tmp % 10] == 0)
			{
				count++;
				arr[tmp % 10] = 1;
			}
			tmp /= 10;
		}

		if (count == 10)
		{
			cout << total << endl;
			return;
		}

		// 1*N, 2*N ...
		total += delta;
	}
}




void printHeader(int num)
{
	cout << "Case #" << num << ": ";
}

int main()
{
	int loop;
	cin >> loop;

	for (int i = 1; i <= loop; i++)
	{
		printHeader(i);
		execute();
	}
}