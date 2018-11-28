#include<cstdio>
#include<algorithm>

using namespace std;

int main()
{
	int t, ca;
	double c, f, x, no;
	scanf("%d", &t);
	for (ca = 1; ca <= t; ca++)
	{
		no = 0.0;
		double s = 2.0;
		scanf("%lf %lf %lf", &c, &f, &x);
		while (true)
		{
			if (x / s > (x / (f + s) + c / s))
			{
				no += c / s;
				s += f;
			}
			else
			{
				no += x / s;
				break;
			}
		}
		printf("Case #%d: %.7lf\n", ca, no);
	}
}