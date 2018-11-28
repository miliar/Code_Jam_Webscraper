#include<iostream>
#include<cmath>
#include<conio.h>
using namespace std;



long long int convert(int arr[], int base, int N)
{

	long long int num = 0;

	for (int k = 0; k < N; k++)
		num += arr[N-1-k] * pow(base, k);

	return num;

}

long int divisor(int arr[], long long int num)
{

	long int fac = sqrt(num);
	long int divs = 1;
	for (int k = 2; k < fac; k++)
	{
		if (num % k == 0) {

			divs = k;
			break;
		}

	}


	return divs;
}

bool check(int arr[], long int div[], int N)
{

	bool found = true;

	for (int k = 2; k <= 10; k++)
	{
		long long int num = convert(arr, k, N);

		div[k - 2] = divisor(arr, num);
		
		if (div[k - 2] == 1) {
			found = false;
			break;
		}

	}


	return found;


}

int permute(int a, int arr[], long int div[], int &count, int N, int J)
{
		
		int temp;
		for (int i = N-2; i >= a; i--)
		{

			if (check(arr, div, N))
			{
				count++;
				if (count > J)
					return 0;
				for (int w = 0; w < N; w++)
				{
					cout << arr[w];
				}
				for (int w = 0; w < 9; w++)
				{
					cout << " " << div[w];
				}
				cout << endl;
				

			}

			arr[i] = 1;
			temp = i + 1;
			while (temp < N-1)
			{
				arr[temp] = 0;
				temp++;
			}

			if (i + 1 < N-1)
				permute(i + 1, arr, div, count, N, J);
		}
	
}


int main()
{
	int T, N, J;
	int count = 0;

	int arr[100];
	cin >> T;
	cin >> N >> J;
	for (int c = 0; c < N; c++)
	{
		if ((c == 0) || (c == N - 1))
			arr[c] = 1;
		else
			arr[c] = 0;
	}
	long int div[9];
	for (int c = 0; c < T; c++)
	{
		cout << "Case #" << c + 1 << ":\n";
		permute(1, arr, div, count, N, J);
	}
		

	return 0;
}
