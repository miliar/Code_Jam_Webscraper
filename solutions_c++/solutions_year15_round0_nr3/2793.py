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
typedef pair<char, char> par;
typedef pair<char, bool> value;
#define mp make_pair

#define MAXN 100005
#define MOD 1000000007

// Define Variables/
map<par, par> M;
int c, i, j, n, x, k, sign, isI, isJ, isK;
string cad;
char v, temp;
bool firstTime;
// Define Variables

int main()
{
	ios::sync_with_stdio(false);

	//Load table
	M[mp('1', '1')] = mp('1', 1);
	M[mp('1', 'i')] = mp('i', 1);
	M[mp('1', 'j')] = mp('j', 1);
	M[mp('1', 'k')] = mp('k', 1);
	M[mp('i', '1')] = mp('i', 1);
	M[mp('i', 'i')] = mp('1', 0);
	M[mp('i', 'j')] = mp('k', 1);
	M[mp('i', 'k')] = mp('j', 0);
	M[mp('j', '1')] = mp('j', 1);
	M[mp('j', 'i')] = mp('k', 0);
	M[mp('j', 'j')] = mp('1', 0);
	M[mp('j', 'k')] = mp('i', 1);
	M[mp('k', '1')] = mp('k', 1);
	M[mp('k', 'i')] = mp('j', 1);
	M[mp('k', 'j')] = mp('i', 0);
	M[mp('k', 'k')] = mp('1', 0);

	ifstream input("C-small.in");
	ofstream output("C-small.out");

	input >> c;

	for (j = 1; j <= c; j++)
	{
		input >> n >> x;

		input >> cad;

		firstTime = false;

		isI = isJ = isK = 0;		

		for (k = 0; k < x; k++)
		{
			for (i = 0; i < n; i++)
			{
				if (firstTime)
				{
					sign = M[mp(v, cad[i])].second == sign;

					v = M[mp(v, cad[i])].first;
				}
				else
				{
					v = cad[i];

					sign = 1;

					firstTime = true;
				}

				if (v == 'i' && sign == 1)
				{
					isI = 1;
				}

				if (v == 'k' && sign == 1 && isI)
				{
					isK = 1;
				}
			}
		}

		if (v == '1' && sign == 0 && isI + isK == 2)
		{
			output << "Case #" << j << ": YES" << endl;
		}
		else
		{
			output << "Case #" << j << ": NO" << endl;
		}
	}	

	input.close();
	output.close();

	return 0;
}