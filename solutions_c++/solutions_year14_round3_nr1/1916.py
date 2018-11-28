#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<iomanip>
#include<cmath>

using namespace std;



int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long p, q, t, c; char y;
	double n,g;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		
		cin >> p >>y>> q; n = (double) p / q;
		c = (double) log2(q) * 1000000000;
		if(c % 1000000000 != 0)  cout << "Case #" << i << ": impossible" << endl;


		else
		{
			g = log2(1 / n);
			g = ceil(g);












			cout << "Case #" << i << ": " << g << endl;
		}









	}
	
	return 0;



}