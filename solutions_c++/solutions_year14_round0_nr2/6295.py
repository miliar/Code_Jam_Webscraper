#include <iostream>
#include <cstdio>
#include <algorithm>


using namespace std;

int t, tt;
double speed, cash, timee, x, c, f;

int main()
{

//	freopen("in.in", "r", stdin);
//	freopen("out.out", "w", stdout);

	cin >> t;


	for (tt = 1; tt <= t; tt++)
	{
		printf("Case #%d: ", tt);

		scanf("%lf%lf%lf", &c, &f, &x);

               	speed = 2.0;
               	cash = 0.0;
               	timee = 0.0;
               	while (cash < x)
               	{
               		timee += c / speed;
               		cash = c;
               		if ((x - cash + c) / (speed + f) < (x - cash) / speed)
                        {
                                speed += f;
                                cash -= c;
                        }
                        else
                        {
                                timee += (x - cash) / speed;
                                break;
                        }
               	}
               	printf("%.6lf\n", timee);
	}

	return 0;
}
