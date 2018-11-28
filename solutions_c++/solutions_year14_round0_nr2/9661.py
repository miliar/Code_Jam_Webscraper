#include "stdafx.h"
#include <iomanip>
#include <iostream>
#include <float.h>
using namespace std;
#pragma warning(disable:4996)

double speedn(double c, double f, double x, double &lasttime, double rspeed = 2.0,double q1 = 0)
{
	q1 += c / rspeed;
	if (lasttime > (q1 + x / (rspeed + f))) { lasttime = q1 + x / (rspeed + f); speedn(c, f, x, lasttime, rspeed + f,q1); }
	else return 1;
}


int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int p=1;
	int exp;
	cin >> exp;
	double farmcost, farmspeed, x, speed = 2.0, lasttime;
	

	while (exp > 0)
	{
		cin >> farmcost;
		cin >> farmspeed;
		cin >> x;
		lasttime = x / 2.0;
		speedn(farmcost, farmspeed, x, lasttime, 2.0);
		cout << "Case #"<< p<<": ";
		
		cout << setprecision(15) << lasttime << endl;
		p++;
		exp--;
	}

	return 0;
}