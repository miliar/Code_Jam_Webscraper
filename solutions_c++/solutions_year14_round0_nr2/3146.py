#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <set>
using namespace std;

double C, F, X;
double nowspeed;

double solve()
{
	double ret = 0.0;
	int buyNFarms = 0;
	buyNFarms = (int)(((X - C) * (2 + F) - 2 * X) / (C * F) + 1.0);
	if(buyNFarms < 1)
	{
		ret = X / 2.0;
	}
	else
	{
		for(int i=0; i<buyNFarms; i++)
		{
			ret += C / (2.0 + i * F);
		}
		ret += X / (2.0 + buyNFarms * F);
	}
	return ret;
}

int initdata()
{
	C = F = X = 0.0;
	return 0;
}

int inputdata()
{
	cin >> C >> F >> X;
	return 0;
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.txt", "w", stdout);
	int T;
	cin>>T;
	for(int t=0; t<T; t++)
	{	
		initdata();
		inputdata();
		double ret = solve();
		// output

		printf("Case #%d: %.7lf\n", t+1, ret);

	}
	return 0;
}

