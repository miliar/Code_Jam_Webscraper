#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int T;
	cin >> T;
	for (int i= 1; i<=T;i++)
	{
		int n;
		cin >> n;
		long double N[1001];
		long double K[1001];
		for (int j= 0; j < n; j++)
			cin >> N[j];
		for (int j= 0; j < n; j++)
			cin >> K[j];
		int Kbegin= n-1, Nbegin = n-1;
		bool over = false;
		std ::sort(N,N+n);
		std :: sort(K,K+n);
		int optimum = 0;
		while (over != true)
		{
			if (N[Nbegin] > K[Kbegin])
			{
				Nbegin--;
				optimum++;
			}
			else 
			{
				Kbegin--;
				Nbegin--;
			}
			if (Nbegin == -1)
				over = true;
		}
		//cout << optimum<<endl;
		int decoptimum = 0;	
		Nbegin = 0, Kbegin = 0;
		over = false;
		while (over != true)
		{
			if (N[Nbegin] < K[Kbegin])
			{
				Nbegin++;
			}
			else
			{
				Nbegin++;
				Kbegin++;
				decoptimum++;
			}
			if (Nbegin == n)
				over = true;
		}
		cout << "Case #"<<i <<": "<<decoptimum << " "<<optimum<<endl;
	}
	
	return 0;
}
