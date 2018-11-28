#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif
#include<iostream>
#include<vector>
#include<fstream>
#include<algorithm>
#include<string>
using namespace std;
double T, C, F, X;


double dabr(double k)
{
	double sum = X / (2 + k*F);
	for (int i = k - 1; i >= 0; i--)
	{
		sum += C / (2 + i*F);
	}
	return sum;
}

int main() {
	cout.precision(10);
	cout.setf(ios::fixed, ios::floatfield);
	freopen("Text.txt", "r", stdin);
	freopen("MyOutput3", "w", stdout);
	cin >> T;
	int cases = 1;
	while (T--)
	{
		cin >> C >> F >> X;

		double min = dabr(0);
		for (int i = 1; i < 10000; i++)
		{
			if (dabr(i) < min)
				min = dabr(i);
		}
		cout<<"Case #"<<cases<<": "<< min << endl;
		cases++;
	}

	return 0;
}