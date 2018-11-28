/*
lan luot tich luy tien de mua farm, do thi thoi gian se co hinh chu V, can xac dinh day cua do thi
*/
#include <iostream>
#include <stdio.h>
using namespace std;

#define FOR(i, a, b) for(int i = a; i <= b; i++)

int sotest;
double c, f, x;

void nhap()
{
	cin >> c >> f >> x;
	//cout << c << ' ' << f << ' ' << x << endl;
}

void lam()
{
	double res;
	double profit = 2, tg1, tg2, tg;
	tg1 = x / profit;
	tg = 0;
	while (true)
		{
			tg2 = tg + c / profit + x / (profit + f);
			//cout << tg2 << endl;
			if (tg2 > tg1) 
				{
					res = tg1;
					break;
				}
			tg1 = tg2;
			tg = tg + c / profit;
			profit += f;
		}
	cout << "Case #" << sotest << ": ";
	printf("%.7lf\n", res);
}

int main()
{
	//freopen("cookie.in", "r", stdin);
	//freopen("cookie.out", "w", stdout);
	//freopen("B-small-attempt0.in", "r", stdin);
	//freopen("B-small-attempt0.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int test;
	cin >> test;
	for (sotest = 1; sotest <= test; sotest++)
		{
			nhap();
			lam();
		}
	return 0;
}
