#include <assert.h>
#include <cstring>
#include <iostream>
#include <fstream>
#include <climits>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <list>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
using namespace std;


int f[4][4];

int main() {
	int cases;
	double C, F, X;
	cin >> cases;
	for (int t = 1; t <= cases; t++)
	{
		cin >> C >> F >> X;
		double v = 2.0;
		double y = 0;
		double time = 0;
		double minT = 100000 / v;
		while (time <= 100000 / v) 
		{
			if (time + (X - y) / v < minT)
			{
				minT = time + (X - y) / v;
			}
			time += C / v;
			v += F;
		}
		printf("Case #%d: %.7lf\n", t, minT);
	}
	return 0;
}