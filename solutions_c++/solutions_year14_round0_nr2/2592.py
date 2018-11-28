#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <stack>
#include <list>
#include <deque>
#include <map>
#include <bitset>
#include <string>
#include <sstream>
#include <algorithm>


using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int cases = 1; cases <= t; cases++)
	{
		double c, f, x;
		cin >> c >> f >> x;
		double best = x/2, ttime = x/2, ctime = 0, speed = 2;
		do 
		{
			if (ttime < best)
				best = ttime;
			ctime += c/speed;
			speed += f;
			ttime = ctime + (x/speed);
		} while (ttime < best);
		printf("Case #%d: %.7lf\n", cases, best);
	}
	return 0;
}