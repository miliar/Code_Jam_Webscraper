#include<iostream>
#include<vector>
using namespace std;
int calculateChances(int a, int b, int k)
{
	int ways = 0;
	int temp;
	if (a > b)
	{
		temp = b;
		b = a;
		a = temp;
	}
	for (int i = 0; i < a; i++)
	{
		for (int j = i; j < b; j++)
		{
			if ((i & j) < k)
			{
				if (i >= b || j >= a || i == j)
					ways++;
				else
					ways += 2;
			}
		}
	}
	return ways;
}
int main()
{
	int T,A,B,K;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cin >> A >> B >> K;
		cout << "Case #"<<i+1<<": "<<calculateChances(A, B, K)<<endl;
	}
	return 0;
}