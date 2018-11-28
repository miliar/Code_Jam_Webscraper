#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <stdio.h>

using namespace std;

const double step = 2;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt", "w", stdout);

	char* format = "Case #%d: %.7f\n";

	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		double c, f, x;
		cin >> c >> f >> x;

		double curSpeed = step;
		double curTime = 0;
		while (true)
		{
			double t1 = x / curSpeed;
			double t2 = (c / curSpeed) + (x / (curSpeed + f));

			if (t1 < t2)
			{
				curTime += t1;
				break;
			}
			else
			{
				curTime += c / curSpeed;
				curSpeed += f;
			}
		}

		printf(format, i + 1, curTime);
	}
	return 0;
}