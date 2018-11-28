#include<iostream>
#include<math.h>
using namespace std;

long long int getVal(int x, int y)
{
	long long int result = 1;
	while (y > 0)
	{
		y--;
		result = result * x;
	}
	return result;
}

long long int isPrime(long long int y)
{
	long long int x = sqrt(y), i = 2;
	while(i <= x)
	{
		if (y%i == 0)
			return i;
		i++;
	}
	return -1;
}

int main()
{
	int n = 16, j = 50;
	long long int c = 32769, k = 0;
	int count = 0, i=1, temp;
	cout << "Case #1: "<<endl;
	while (count < j)
	{
		temp = 0;
		k = c + (i << 1);
		i++;
		long long int arr[9] = {0};
		int pos = 0;
		int arr2[16] = {0};
		while (k > 0)
		{
			int d = k%2;
			if (d == 1)
			{
				for (int y = 0;y < 9; y++)
				{
					arr[y] += getVal(y+2, pos);
				}
				arr2[pos] = 1;
			}
			
			pos++;
			k = k/2;
		}
				
		for (int it = 0; it < 9; it++)
		{
			long long int result = isPrime(arr[it]); 
			if (result == -1)
			{
				temp = 1;
				break;
			}
			arr[it] = result;
		}
					
		if (temp == 1)
			continue;
		count++;
		for (int it = 15;it>=0; it--)
		{
			cout << arr2[it];
			
		}	
		cout << " ";
		for (int it = 0; it < 9; it++)
		{
			cout << arr[it] << " ";
		}
		cout << endl;
	}
}
