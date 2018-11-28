#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>
#include <queue>
#include <math.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define For(i, n) for(int i = 0; i < (n); i++)
#define ForD(i, n) for(int i = (n) - 1; i >= 0; i--)
#define in cin >>
#define out cout <<
#define ft first
#define sd second
typedef long long LL;

int A[4][4], B[4][4];

int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	in t;
	For (k, t)
	{
		memset(A, 0, sizeof(A));
		memset(B, 0, sizeof(B));
		int x1, x2;

		in x1;
		For (i, 4)
			For (j, 4)
			in A[i][j];
		in x2;
		For (i, 4)
			For (j, 4)
			in B[i][j];
		int which = -1, cnt = 0;
		x1--, x2--;
		For (j, 4)
			For (i, 4)
			if (A[x1][i] == B[x2][j])
				which = A[x1][i],
				      cnt++;
		out "Case #" << k + 1 << ": ";
		if (cnt > 1)
			out "Bad magician!\n";
		else if (which == -1)
			out "Volunteer cheated!\n";
		else
			out which << "\n";
	}
}
