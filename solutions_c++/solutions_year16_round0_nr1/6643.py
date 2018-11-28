#include <bits/stdc++.h>
using namespace std;

int a[10];

void count(long long int n)
{
	int rem;

	while(n > 0)
	{
		rem = n%10;
		a[rem] = 1;
		n /= 10;
	}
}

int main()
{
	freopen("Input.in", "r", stdin);
	freopen("Output.out", "w", stdout);

	int t, j;
	cin >> t;

	for(j=1; j<=t; j++)
	{
		long long int i, n, mu, temp;
		cin >> n;

		if(n == 0)
			cout << "Case #" << j << ": " << "INSOMNIA" << endl;
		else
		{
			for(i=0; i<10; i++)
				a[i] = 0;
			
			mu = 2;
			temp = n;

			while(true)
			{
				count(temp);

				for(i=0; i<10; i++)
				{
					if(a[i] == 0)
						break;
				}

				if(i >= 10)
					break;

				temp = mu*n;
				mu++;
			}

			cout << "Case #" << j << ": " << temp << endl;
		}
	}

	return 0;
}