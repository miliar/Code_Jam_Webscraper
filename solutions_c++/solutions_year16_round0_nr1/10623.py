#include <iostream>

using namespace std;

bool canSleep(int arr[], int size)
{
	for (int i = 0; i < size; i++)
	{
		if (arr[i] != 1)
		  return false;
	}
	return true;
}

int getNumberToSleep(unsigned long N)
{
	int numbersFound[10] = {0};
	for(int i = 1; i <= 100;i++)
	{
		unsigned long num = N * i;
		while(num != 0) 
		{
			unsigned long remainder = num % 10;
			numbersFound[remainder] = 1;
			num = num / 10;
		}
		if (canSleep(numbersFound, 10))
			return N * i;
	}
	return -1;
}

int main()
{
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++)
	{
		unsigned long N, ret;
		cin >> N;
		if ((ret = getNumberToSleep(N)) != -1)
		{
			cout << "Case #" << i << ": " << ret << endl;
		}
		else
		{
			cout << "Case #" << i << ": " << "INSOMNIA" << endl;
		}
	}
}