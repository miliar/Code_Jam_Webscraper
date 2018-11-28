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
ostream &out = ofstream("output.txt");
//ostream &out = cout;

int main()
{
	int T;
	in >> T;
	REP1(t, T)
	{
		int ans = 0;
		vector<int> candidate(4);
		{
			int lineNum;
			in >> lineNum;

			vector<vector<int>> matrix(4, vector<int>(4));
			REP(i, 4) REP(j, 4) in >> matrix[i][j];

			candidate = matrix[lineNum - 1];
		}
		{
			int lineNum;
			in >> lineNum;

			vector<vector<int>> matrix(4, vector<int>(4));
			REP(i, 4) REP(j, 4) in >> matrix[i][j];
			REP(i, 4) REP(j, 4)
			{
				if(candidate[i] == matrix[lineNum - 1][j])
				{
					if(ans == 0) ans = candidate[i];
					else ans = -1;
				}
			}
		}

		if(ans == -1)
			out << "Case #" << t << ": " << "Bad magician!" << endl;
		else if(ans == 0)
			out << "Case #" << t << ": " << "Volunteer cheated!" << endl;
		else
			out << "Case #" << t << ": " << ans << endl;
	}

	return 0;
}