#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <sstream>
#include <typeinfo>
#include <fstream>

using namespace std;
// #define INPUT_FILE

double total_time(int no, double C, double F, double farms)
{
	double r = 2.0 + (no-1)*F;
	farms += C/r;
	return farms;
}

int main(int argc, char const *argv[])
{
	#ifdef INPUT_FILE
	    freopen("B-small-attempt0.in", "r", stdin);
	#endif
	int t;
	scanf("%d", &t);
	int n = t;
	while(t--)
	{
		double C, F, X;
		scanf("%lf%lf%lf", &C, &F, &X);
		std::vector<double> farms;
		std::vector<double> time_taken;
		farms.push_back(0.0);
		time_taken.push_back(X/2.0);
		int no = 1;
		while(1)
		{
			// printf("time_taken: %lf\n", time_taken.back());
			farms.push_back(total_time(no, C, F, farms.back()));
			time_taken.push_back(farms.back() + X/(2.0 + no*F));
			if(time_taken.back() > time_taken[time_taken.size() - 2])
			{
				printf("Case #%d: %.7lf\n", n-t, time_taken[time_taken.size() - 2]);
				break;
			}
			no++;
		}
	}
	return 0;
}
