#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<set>
#include<map>
#include<fstream>
#define epsilon 0.000000001
#define cosinusa(a, b, c) ((a * a + b * b - c * c) / (2.0 * a * b));
#define infi 1000000000
using namespace std;

int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d: ", testCounter + 1);
		double c, x, l;
		cin >> c >> x >> l;
		double best = l / 2.0;
		double tmp = 0;
		double curV = 2.0;
		double newV;
		while (1)
		{
			tmp += c / curV;
			curV += x;
			newV = tmp + l / curV;
			if (newV < best)
			{
				best = newV;
			}
			else
			{
				break;
			}
		}
		printf("%.7lf\n", best);
	}
	return 0;
}
