// B.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <iomanip>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream cin("B-large.in");
	ofstream cout("outB.txt");
	int T;
	int t = 0;
	cin >> T;
	cout << fixed;
	while (t != T){
		++t;
		cout << "Case #" << t << ": ";
		double C,F,X;
		cin >> C >> F >> X;
		double c = 2, time = 0;
		time = X / c;
		double farm = 0.0;
		while ((X / (c + F) + C / c + farm) < time){
			time = X / (c + F) + C / c + farm;
			farm += C / c;
			c += F;
		}
		cout << setprecision(7) << time << endl;
	}
	return 0;
}


