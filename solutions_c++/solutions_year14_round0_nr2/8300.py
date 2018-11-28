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
#include <string>
#include <cstring>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int ti = 1;ti <= t;ti++)
	{
		double C,F,X;
		double spd = 2;
		cin >> C >> F >> X;
		double res = 0;
		while((X/spd) > (C/spd) + (X / (spd+F)))
		{
			res += (C/spd);
			spd+=F;
		}
		res += (X/spd);
		printf("Case #%d: %.7llf\n",ti,res);
	}
	return 0;
}