#include <iostream>

using namespace std;

int main(void)
{
	int count = 0;
	double C = 0;
	double F = 0;
	double X = 0;
	double speed = 2.0;
	double res = 0.0;
	int num = 0;
/*	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
*/	cin >> count;
	for (int i = 0; i < count; i++)
	{
		speed = 2.0;
		res = 0;
		cin >> C >> F >> X;
		while ((X / speed) >((C / speed + X / (speed + F))))
		{
			res += C / speed;
			speed += F;
		}
		res += X / speed;
		cout << "Case #" << i + 1 << ": ";
		printf("%.7f\n", res);
	}
	return 0;
}