/*************************************************************************
    > File Name: Bsmall.cpp
    > Author: Hu Pengxiang
    > Mail: hpxiangsky@gmail.com 
    > Created Time: Sat 12 Apr 2014 09:00:34 PM CST
 *************************************************************************
 Function:
		1. 
 History:
		1. Created by Hu Pengxiang on Sat 12 Apr 2014 09:00:34 PM CST
 ************************************************************************/

#include<iostream>
using namespace std;

int main()
{
	double C, F, X;
	double G, G2;
	int T;
	cin >> T;
	cout.setf(ios::showpoint);
	cout.precision(7);
	cout.setf(ios::fixed);
	for(int i = 0;i < T;++i)
	{
		cin >> C >> F >> X;
		double time = 0;
		bool buy;
		G = 2.0;
		do
		{
			G2 = G + F;
			if(X/G > X/G2 + C/G)
			{
				buy = true;
				time += C / G;
				G += F;
			}
			else
			{
				buy = false;
				time += X/G;
			}
		}
		while(buy);
		cout << "Case #" << i+1 << ": " << time << endl;
	}
}
