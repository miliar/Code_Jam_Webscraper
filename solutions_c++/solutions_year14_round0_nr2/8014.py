#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() 
{
	double C,F,X, time;
	int T;
	scanf("%d ", &T);
	for(int i=0;i<T;i++)
	{
		double V=2.0;
		scanf("%lf %lf %lf",&C,&F,&X);
		time = 0.0;
		while(X/V > C/V + X/(V+F))
		{
			time += C/V;
			V += F;
		}
		time += X/V;
		printf("Case #%d: %lf\n",i+1,time);
	}
	return 0;
}