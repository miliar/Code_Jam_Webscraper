#include<iostream>
using namespace std;

double remainTime(double X, double current, double rate)
{
	return (X - current) / rate;
}

int main()
{
	int N;
	cin >> N;
	for (int i = 0; i < N; ++i)
	{
		double C, F, X, ttlTime = 0.0, cur = 0.0, rate = 2.0;
		cin >> C >> F >> X;
		while (1)
		{
			double tmA = (X - 0.0) / rate;		// time needed if wait until it exceeds the amount

			double tmB1 = (C - 0.0) / rate;		// time needed if buy farm
			double tmB2 = (X - 0.0) / (rate+F); 		// after purchase farm, time required if wait until it exceeds the amount
			double tmB = tmB1 + tmB2;

			/*
			double tmC1 = tmB1;
			double tmC2 = (C - 0.0) / (rate + F);
			double tmC3 = (X - 0.0) / (rate + F + F);
			double tmC = tmC1 + tmC2 + tmC3;
			*/

			if (tmA <= tmB)
			{
				ttlTime += tmA;
				break;
			}
			ttlTime += tmB1;

			//cur = 0.0;							// current amount is zero after purchase
			rate += F;							// update the rate after purchase
		}
		cout.precision(7);
		cout << "Case #" << i + 1 << ": " << fixed << ttlTime << endl;
	}
	return 0;
}
