//============================================================================
// Name        :
// Author      : Bryce Sandlund
// Version     :
// Copyright   :
// Description : Google Code Jam Code
//============================================================================

#include <iostream>
#include <iomanip>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <list>
#include <map>
#include <fstream>
#include <string>
#include <time.h>
#include <queue>
#include <tuple>
//#include <unordered_set>
//#include <unordered_map>
//#include <ctgmath>

#define INF 1000000000000000000LL

using namespace std;

typedef pair<int, pair<int, int> > iii;

int main() {
	ofstream out;
	out.open("out.txt");
	ifstream in("in.txt");
	out << std::setprecision(7) << std::fixed;

	int T;
	in >> T;
	for (int caseNum = 1; caseNum <= T; ++caseNum)
	{
		double C, F, X;
		in >> C >> F >> X;

		double prev = X/2;
		double secsElapsed = 0;
		double rate = 2;

		while (true)
		{
			secsElapsed += C/rate;
			rate += F;
			double cost = secsElapsed + X/rate;
			if (cost > prev)
			{
				break;
			}

			prev = cost;
		}

		out << "Case #" << caseNum << ": " << prev << endl;
	}
	out.close();
	return 0;
}
