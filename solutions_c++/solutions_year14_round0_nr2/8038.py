#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
#define db(val) cout << #val << ": " << (val) << endl;
int T;
double c, f, x;

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int t = 0; t < T; ++t)
	{
		scanf("%lf%lf%lf", &c, &f, &x);
		double prevSum = 0.0, prevAns = x / 2.0;
		int i = 0;
		while (true)
		{
			double newSum = prevSum + c / (2.0 + i * f);
			double newAns = newSum + x / (2.0 + (i + 1) * f);
			if (newAns > prevAns) break;
			swap(newAns, prevAns);
			swap(newSum, prevSum);
			++i;
		}
		printf("Case #%d: %.7lf\n", t + 1, prevAns);
	}
	return 0;
}
