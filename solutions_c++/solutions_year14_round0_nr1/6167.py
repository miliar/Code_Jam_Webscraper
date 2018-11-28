#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>

using namespace std;

typedef long long ll;
typedef long double ld;

#define SMALL
//#define LARGE
int main()
{
	freopen("A-test.in", "rt", stdin);
	freopen("A-test.out", "wt", stdout);
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif

	int T;
	cin >> T;

	for(int ii=0; ii<T; ii++)
	{
		cout << "Case #" << (ii+1) << ": ";

		int row1;
		int board1[4][4];
		cin >> row1;

		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				cin >> board1[i][j];
			}
		}

		int row2;
		int board2[4][4];
		cin >> row2;

		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				cin >> board2[i][j];
			}
		}

		int count = 0;
		int match;
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				if(board1[row1-1][i] == board2[row2-1][j])
				{
					match = board1[row1-1][i];
					count++;
				}
			}
		}

		if(count == 0) cout << "Volunteer cheated!";
		else if (count == 1) cout << match;
		else cout << "Bad magician!";

		cout << endl;

END_CASE:;
	}

	return 0;
}
