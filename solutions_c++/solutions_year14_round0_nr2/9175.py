#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	double F, C, X,  time,rate,cookies;
	int cases, icase;
	cin >> cases;
	for (icase = 1; icase <= cases; icase++)
	{
		cin >> C >> F >> X;
		rate = 2; time = 0; cookies = 0;
		while (cookies<X)
		{
			if ((X / rate )> (X / (rate + F) + C / rate))
			{
				time += C / rate;
				rate += F;
			}
			else
			{
				time += X / rate;
				cookies = X;
			}


		}
		cout << "Case #" << setprecision(0) << icase << ": " << fixed << setprecision(7) << time << '\n';

	}

}
