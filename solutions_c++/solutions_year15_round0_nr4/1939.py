#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long int ll;
typedef pair<int, int> par;
#define mp make_pair

#define MAXN 100005
#define MOD 1000000007

// Define Variables/
int cc, j, i, x, r, c, temp;
string R = "RICHARD", G = "GABRIEL", sol;
// Define Variables

int main()
{
	ios::sync_with_stdio(false);

	ifstream input("D-small.in");
	ofstream output("D-small.out");

	input >> cc;

	for (j = 1; j <= cc; j++)
	{
		input >> x >> r >> c;

		temp = min(r, c);

		c = max(r, c);

		r = temp;

		if (r * c < x || (r*c) % x > 0)
		{
			sol = R;
		}		
		else if (r * c == x) // 1 1 1 - 2 1 2
		{
			if (x <= 2)
			{
				sol = G;
			}
			else // 3 1 3 - 4 1 4 - 4 2 2
			{
				sol = R;
			}			
		}		 
		else
		{
			if (x == 1) // 1 1 1 - 1 1 2 - 1 1 3 - 1 1 4 - 1 2 2 - 1 2 3 - 1 2 4 - 1 3 3 - 1 3 4 - 1 4 4
			{
				sol = G;
			}
			else if (x == 2 || x == 3) // 2 1 2 - 2 1 4 - 2 2 2 - 2 2 3 - 2 2 4 - 2 3 4 - 2 4 4 // 3 2 3 - 3 3 3 - 3 3 4 
			{
				sol = G;
			}
			else
			{
				if (r >= 3 && c >= 4)
				{
					sol = G;
				}
				else
				{
					sol = R;
				}				
			}
		}

		output << "Case #" << j << ": " << sol << endl;
	}

	input.close();
	output.close();

	return 0;
}