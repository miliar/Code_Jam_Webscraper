#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
double calc(double coin, double toWin, double CockPS)
{
	return (((toWin - coin) / CockPS));
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	double C, F, X;
	scanf("%d", &t);
	for (int k = 1; k <= t; ++k){
		printf("Case #%d: ", k);
		cin >> C >> F >> X;
		double AF = 2, AX = X;
		double time = 0.0;
		double coin = 0;
		while (true)
		{
			double newF = F + AF, newCoin, newT = 0;
			if (coin >= C)
				newCoin = coin - C;
			else
			{
				newT = (C - coin) / AF;
				newCoin = 0;
			}
			if (((AX - coin) / AF) > (((AX - newCoin) / newF) + newT))
			{
				coin = newCoin;
				time += newT;
				AF = newF;
			}
			else
			{
				newT = (X - coin) / AF;
				newT = max(newT, 0.0);
				time += newT;
				break;
			}
		//	cout << time << " " << AX << " " << AF << " " << coin << " " << endl;
		}
		printf("%.7lf\n", time);
	}
	return 0;
}