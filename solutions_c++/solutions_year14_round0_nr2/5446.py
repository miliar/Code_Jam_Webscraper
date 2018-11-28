#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
long double K[1000010];
int main()
{
	long double X, C, F;
	int t;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	
	for (int j = 1; j <= t; j++)
	{
		    cin >> C >> F >> X;
		    int pp = (int)(X + 1);
			long double ans = X / (long double)2;
			for (int i = 1; i <= pp; i++)
			{
				K[i] = K[i - 1] + C / (2 + (long double)(i - 1) * F);
				if (ans > (K[i] + X / (2 + (long double)(i)* F)))
				{
					ans = (K[i] + X / (2 + (long double)(i)* F));
				}
			}
			cout << "Case #" << j << ": ";
		    printf("%.9llf", ans);
			cout << endl;
	}
	return 0;
}