#include <iostream>

using namespace std;

int T;
int N;
int *P;

bool IsValid(int total)
{

	for( int i = 0; i < N; i++ )
	{
		if( P[i] > total/2 )
			return false;
	}
	return true;
}

int GetRes(int n)
{
	int res = 0;
	while(n > 0)
	{
		int max = n/2;

		int m = 0;
		int in = 0;
		for( int i = 0; i < N; i++ )
		{
			if( P[i] > m )
			{
				m = P[i];
				in = i;
			}
		}

		n--;
		P[in]--;
		char c = in + 'A';
		cout << c;

		m = 0; 
		in = 0;
		for( int i = 0; i < N; i++ )
		{
			if( P[i] > m )
			{
				m = P[i];
				in = i;
			}
		}

		P[in]--;
		if( !IsValid( n - 1 ) )
		{
			P[in]++;
		}
		else
		{
			char c = in + 'A';
			cout << c;
			n--;
		}
		cout << " ";
	}

	return res;
}

int main()
{
	cin >> T;

	for( int t = 0 ; t < T; t++ )
	{
		cin >> N;

		P = new int[N];
		int sum = 0;
		for( int n = 0; n < N; n++ )
		{
			int k;
			cin >> k;
			P[n] = k;
			sum += k;
		}

		cout << "Case #" << t + 1 << ": ";

		int res = GetRes(sum);

		cout << endl;
	}

	return 0;
}