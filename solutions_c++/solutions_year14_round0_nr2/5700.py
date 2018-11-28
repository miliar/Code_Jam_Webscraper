#include<cstdlib>
#include<cctype>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<iostream>
#include<sstream>
#include<fstream>
#include<bitset>
#include<list>
using namespace std;

const double EPS = 0.00000001;

int main()
{

	freopen("E:\\B.in", "r", stdin);
	freopen("E:\\B.out", "w", stdout);

	int T;

	scanf("%d", &T);
	for (int cas = 0; cas < T; cas++)
	{
		double C = 0.0;
		double F = 0.0;
		double X = 0.0;
		double SUM_TIME = 0.0;
		double T1 = 0.0;
		double T2 = 0.0;
		double speed = 2.0;
		cin >> C >> F >> X;

		while (true)
		{
			T1 = X / speed;
			T2 = X / (speed + F) + (C / speed);
			if (T2 - T1 > EPS)
			{
				break;
			}
			else
			{
				SUM_TIME += C / speed;
				speed += F;
			}

		}
		SUM_TIME += X / speed;
		printf("Case #%d: %.7lf\n", cas + 1, SUM_TIME);
	}

	return 0;
}
