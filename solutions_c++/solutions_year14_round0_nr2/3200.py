#include<iostream>
using namespace std;
int main()
{
	int T;

	errno_t err1;
	FILE *f;
	err1 = freopen_s(&f, "B-large.in", "r", stdin);
	errno_t err2;
	FILE *f2;
	err2 = freopen_s(&f2, "3.txt", "w", stdout);
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		double C, F, X;
		cin >> C >> F >> X;
		double gain = 2;
		double sumtime = 0;
		if (X < C)
		{
			printf("Case #%d: %.7f\n",i+1, X / gain);
			continue;
		}
		while (1)
		{
			double tmp = C / gain;
			if (X / (gain + F)>(X - C) / gain)
			{
				sumtime += X / gain;
				break;
			}
			else
			{
				gain += F;
				sumtime += tmp;
			}
		}
		printf("Case #%d: %.7f\n",i+1, sumtime);
	}
	return 0;
}