#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	int n, i;

	cin>>n;

	cout << setprecision(7) << fixed;

	for(i = 1; i <= n; i++)
	{
		double C, F, X, T = -1, t;
		int n, j;

		cin>>C>>F>>X;

// X/(2 + nF) + C/(2 + 0F) + C/(2 + F) + C/(2 + 2F) + ... + C/(2 + (n-1)F)

		for(n = 0; true; n++)
		{
			t = 0;
			t += X / (2 + n * F);

			for(j = 1; j <= n; j++)
			{
				t += C / (2 + (j - 1) * F);
			}

			//cout<<t<<endl;

			if(t < T || T < 0)
				T = t;
			else
				break;
		}

		cout<<"Case #"<<i<<": "<<T<<endl;
	}
}
