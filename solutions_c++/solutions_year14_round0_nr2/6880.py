#include <functional>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <bitset>
#include <queue>
#include <deque>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <map>
#include <set>

using namespace std;


int main()
{
#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	int T;
	cin >> T;

	for(int t=0; t < T; ++t)
	{
		double C, F, X;
		cin >> C >> F >> X;

		double speed = 2;
		double time = 0;
		double amount = 0;

		while(amount + 1e-8 < X)
		{
			double t1 = (X-amount) / speed;
			double t2 = C / speed + (X-amount) / (speed+F);

			if (t1 < t2)
			{
				time += t1;
				break;
			}
			else
			{
				time += C / speed;
				speed += F;
			}
		}

		printf("Case #%d: %.8f\n", t+1, time);





	}


}