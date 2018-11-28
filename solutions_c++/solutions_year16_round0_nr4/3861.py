#include <iostream>

using namespace std;

long long lpow(long long base, long long exp)
{
	long long result = 1;
	while(exp > 0)
	{
		exp--;
		result = result * base;
	}
	return result;
}

int main()
{
    int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int K;
		int C;
		int S;
		
		cin >> K >> C >> S;
		
		cout << "Case #" << i + 1 << ": ";
		
		if(K != S)
			cout << "error";
		for(int j = 1; j < K; j++)
		{
			cout << j << " ";
		}
		cout << K;
		cout << endl;		
	}
}

int dummy()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int K;
		int C;
		int S;
		
		cin >> K >> C >> S;
		
		cout << "Case #" << i + 1 << ": ";
		
		if(K != S)
			cout << "error";
		for(int j = 1; j < K; j++)
		{
			cout << j << " ";
		}
		cout << K;
		cout << endl;		
	}
}
