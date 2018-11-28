#include<iostream>

using namespace std;

typedef unsigned long long ull;

FILE* pF; 
FILE* pAnsF;

ull K, C, S;

int main()
{
	freopen_s(&pF, "Text.txt", "r", stdin);
	
	freopen_s(&pAnsF, "OutputFractalSmall.txt", "w", stdout);

	int nCases;

	cin >> nCases;

	for (int c = 1; c <= nCases; c++)
	{
		cin >> K >> C >> S;
		cout << "Case #" << c << ": ";
		if (S < K)
		{
			cout<<"IMPOSSIBLE"<< endl;
		}
		else
		{
#if 0
			ull interval = pow(K, C - 1);
			for (ull a = 1; a <= pow(K, C); a = a + interval)
			{
				cout << a << " ";
			}
#else
			for (ull a = 1; a <= S; a++)
			{
				cout << a << " ";
			}
#endif
			cout << endl;
		}
	}

	return 0;
}
