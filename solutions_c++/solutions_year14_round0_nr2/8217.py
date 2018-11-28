#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
	int n;
	double C, F, X;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> C >> F >> X;
		double cur = 2;
		double time, time2,ctime;
		ctime = 0;
		do
		{
			time = X / cur;
			time2 = C / cur + X / (cur + F);
			if (time2<time)
			{
				ctime += C / cur;
				cur += F;
			}
		} while (time > time2);
		printf("Case #%d: %.7f\n", i + 1, ctime+time);
		//cout << "Case #"<<i+1<<": "<<ctime + time<<"\n";
	}
	return 0;
}