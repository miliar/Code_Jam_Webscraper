#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <limits>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <string>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
const int INF = numeric_limits<int>::max();

const int kmax = 100000000;

int main(int argc,char* argv[])
{
	int num_test_cases;
	scanf("%d",&num_test_cases);
	for(int test_case=1; test_case<=num_test_cases; test_case++)
	{
		double C, F, X;
		cin >> C >> F >> X;
		double farmCost = 0, best = numeric_limits<double>::infinity();
		for(int k=0;;k++)
		{
			double cost = farmCost + X / (2 + k * F);
			//best = min(best, cost);
			if(cost > best)
				break;
			best = cost;
			farmCost += C / (2 + k * F);
		}
		printf("Case #%d: %.7f\n", test_case, best);
	}
	return 0;
}
