#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <cstdio>

using namespace std;

int main()
{
	int cases;
	double C,F,X, farms;
	cin >> cases;
	double spent, best, newtime;
	
	for (int testcase = 1; testcase <= cases; testcase++)
	{
		cin >> C >> F >> X;
		spent = 0;
		best = X/2;
		newtime = 0;
		farms = 0;
		while (true)
		{
			spent += C/(farms*F+2);
			farms++;
			newtime = spent + X/(farms*F+2);
			//cout << newtime << " " << best << endl;
			if (newtime >= best)
				break;
			best = newtime;
		}
	
		cout << "Case #"<< testcase << ": ";
		printf("%.7lf\n",best);
		
	}
}
