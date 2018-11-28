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

#define MAXN 1005
#define MOD 1000000007

// Define Variables/
ll c, n, i, j, le, co, sol, sum, temp;
string cad;
// Define Variables

int main()
{
	ios::sync_with_stdio(false);

	ifstream input("A-large.in");
	ofstream output("A-large.out");

	input >> c;

	for (j = 1; j <= c; j++)
	{
		input >> n >> cad;

		le = cad.length();

		sum = cad[0] - '0';

		sol = 0;

		for (i = 1; i < le; i++)
		{
			if (cad[i] - '0' == 0)
				continue;
			
			if (i > sum)
			{
				temp = i - sum;
				
				sol += temp;

				sum += temp;
			}

			sum += cad[i] - '0';
		}

		output << "Case #" << j << ": " << sol << endl;
	}

	input.close();
	output.close();

	return 0;
}