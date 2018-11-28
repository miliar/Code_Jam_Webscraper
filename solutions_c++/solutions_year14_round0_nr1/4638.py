#include<iostream>
using namespace std;
#define SIZE 4
int main() 
{
	int N;
	cin >> N;
	for (int i = 0; i < N; ++i)
	{
		int ans1, ans2;
		int invalid;
		int input1[SIZE], input2[SIZE];

		cin >> ans1;
		for (int j = 0; j < SIZE; ++j)
		{
			for (int k = 0; k < SIZE; ++k)
			{
				if ((j+1) == ans1)
					cin >> input1[k];
				else
					cin >> invalid;
			}
		}

		cin >> ans2;
		for (int j = 0; j < SIZE; ++j)
		{
			for (int k = 0; k < SIZE; ++k)
			{
				if ((j+1) == ans2)
					cin >> input2[k];
				else 
					cin >> invalid;
			}
		}
	
		int cnt = 0;
		int chosen;
		for (int i = 0; i < SIZE; ++i)
		{
			for (int k = 0; k < SIZE; ++k)
			{
				if (input1[i] == input2[k])
				{
					chosen = input1[i];
					++cnt;
				}
			}
		}
		cout << "Case #" << i+1 << ": ";
		if (cnt == 1)
			cout << chosen;
		else if (cnt > 1)
			cout << "Bad magician!";
		else 
			cout << "Volunteer cheated!";
		cout << endl;
	}
	return 0;
}


