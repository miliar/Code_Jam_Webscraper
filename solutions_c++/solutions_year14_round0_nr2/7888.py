#include <iostream>
#include <cstdio>
#include <iomanip>
#include <cmath>
#include <vector>
#include <algorithm>
#include <functional>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>
#include <cstdlib>
#include <stack>
#include <queue>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

#define REP(v, hi) for (int v=0;v<(hi);v++)
#define REPD(v, hi) for (int v=((hi)-1);v>=0;v--)
#define FOR(v, lo, hi) for (int v=(lo);v<(hi);v++)
#define FORD(v, lo, hi) for (int v=((hi)-1);v>=(lo);v--)
#define REP1(v, hi) for (int v=1;v<=(hi);v++)
#define REPD1(v, hi) for (int v=(hi);v>=1;v--)
#define FOR1(v, lo, hi) for (int v=(lo);v<=(hi);v++)
#define FORD1(v, lo, hi) for (int v=(hi);v>=(lo);v--)
const double eps = 1 / (double)1000000000;

istream &in = ifstream("input.txt");
//ostream &out = ofstream("output.txt");
FILE *fout = fopen("output.txt", "w");
//ostream &out = cout;

int main()
{
	int T;
	in >> T;
	REP1(t, T)
	{
		double C, F, X, ans = 0.0;
		in >> C >> F >> X;

		double factoryGen = C;
		double cookieGen = 2.0;
		REP(i, 1000000)
		{
			double factoryTime = factoryGen / cookieGen;
			double genTimeWithFactory = X / (cookieGen + F) + factoryTime;
			double genTimeWithoutFactory = X / cookieGen;
			if (genTimeWithFactory >= genTimeWithoutFactory)
			{
				ans += genTimeWithoutFactory;
				break;
			}
			else
			{
				ans += factoryTime;
				cookieGen += F;
			}
		}


		fprintf(fout, "Case #%d: %.07lf\n", t, ans);
		printf("Case #%d: %.07lf\n", t, ans);
	}

	return 0;
}