#include <iostream>
using namespace std;
int findCharacters(int number)
{
	int LSB;
	int resultMask = 0;
	do
	{
		LSB = number % 10;
		number = number / 10;
		resultMask = resultMask | (1 << LSB);
	} while (number > 0);
	return resultMask;
}

int main(char* argv,int argc)
{
	int cases = 0;
	cin >> cases;
	
	
	

	for (int i = 1; i <= cases; i++)
	{
		int N = 0;
		int Nt = N;
		int result = 0;
		bool solveable = false;
		cin >> N;
		if (N != 0)
		{
			for (int j=1; (result != 0x3FF); j++)
			{
				Nt = N*j;
				result = result | findCharacters(Nt);
			}
			solveable = true;
			
		}
		cout << "Case #" << (i) << ": ";
		if (solveable)
		{
			cout << Nt << endl;
		}
		else
		{
			cout << "INSOMNIA" << endl;
		}
	}
	
}