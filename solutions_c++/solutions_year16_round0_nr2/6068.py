#include <iostream>

using namespace std;

int flip(char* A, int pos)
{
	char B[100] = {0};
	for(int i = pos; i >= 0; i--)
	{
		if(A[i] == '+') B[i] = '-';
		if(A[i] == '-') B[i] = '+';
	}
	for(int i = pos; i >= 0; i--)
	{
		A[i] = B[pos-i];
	}
}

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		char A[100] = {0};
		cin >> A;
		
		int pos = 100;
		int nflips = 0;
		while(pos != 0)
		{
			pos--;
			if (A[pos] == 0 || A[pos] == '+')
			{
				continue;
			}
			
			int flipPos = 0;
			while(A[flipPos] == '+')
			{
				flipPos++;
			}
			if(flipPos != 0)
			{
				flip(A, flipPos - 1);
				nflips++;
			}
			flip(A, pos);
			nflips++;
		}
		cout << "Case #" << i + 1 << ": " << nflips <<  endl;
	}
}
