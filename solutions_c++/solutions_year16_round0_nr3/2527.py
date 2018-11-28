#include <iostream>
#include <fstream>
#include <cstdlib>
#include<string>
#include<vector>
#include<cmath>
#include <sstream>

using namespace std;


int cases = 0;

string face;


long long temp;

unsigned long long int num[9];

int N, J;

int track, level, kth = 0;

char jam[5000];

char old_jam[1000][5000];

int check();

int prime(int a);

int main()
{

	int deg = 0;
	freopen("a.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> cases;


	

	cout << "Case #" << 1 << ":" << endl;

		cin >> N;
		cin >> J;
		jam[0] = '1';
		
		for (int a = 1; a < N - 1; a++)
		{
			jam[a] = '0';
		}
		jam[N-1] = '1';
		


		track = N - 2;
		deg = track;
		//jam[N - 2] = '1';
		//cout << jam[N-2];
		for (int qq = 0; qq < J; qq++) {


			for (int a = 0; a < 9; a++)
			{
				num[a] = 0;
			}


			while (check() == 0)
			{

				for (int q = track; q > 0; q--)
				{

					if (jam[q] == '0')
					{
						jam[q] = '1';
						break;
					}
					else
					{
						jam[q] = '0';
					}
				}

			}

			for (int a = 0; a < N; a++)
			{
				cout << jam[a];
				old_jam[kth][a] = jam[a];
			}

			kth++;

			for (int k = 0; k < 9; k++)
			{
				cout << " " << num[k];
			}

			cout << endl;


			for (int q = track; q > 0; q--)
			{

				if (jam[q] == '0')
				{
					jam[q] = '1';
					break;
				}
				else
				{
					jam[q] = '0';
				}
			}
		}

	return 0;
}

int check()
{
	int counter = 1;
	for (int k = 0; k < kth; k++)
	{

	
		for (int r = 0; r < N; r++)
		{
			if (jam[r] == old_jam[k][r])
			{
				counter++;
			//	cout << counter << endl;
			}
		}
		if (counter >= N)
		{
			return 0;
		}
		counter = 0;
	}
	

	for (int z = 2; z < 11; z++)
	{
		num[z - 2] = 0;
		for (int a = 0; a < N ; a++)
		{

			if (jam[a] == '1')
			{
				num[z-2] = num[z-2] + pow(z, N - a - 1);
				
			}

		}


		if (prime(z) <= 0)
		{
			//cout << "asdsad";
			return 0;
		}
	}
	return 1;

}


int prime(int z)
{
	for (int i = 2; i < num[z - 2]; i++)
	{
		if (num[z - 2] % i == 0)
		{
			//cout << num[z - 2] << endl;
			num[z - 2] = i;
			//cout << num[z - 2] << endl;
			return 1;
		}
	}

	return 0;

}