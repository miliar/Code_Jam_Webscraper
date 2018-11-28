#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <deque>
using namespace std;

#define FOR(i, a, b) for(i = (a) ; i<(b) ; i++)
#define RFOR(i, a, b) for(i = (a)-1 ; i>=(b); i--)
#define MEM(a,b) memset(a,b,sizeof(a))

//#define SMALL 1
#define SMALL 0

char change(char side)
{
	if (side == '+')
		return '-';
	else if (side == '-')
		return '+';
}

void Solve()
{
	string S;
	cin >> S;

	int i,j;
	deque<char> origin;
	deque<char> flip;
	FOR(i, 0, S.length())
	{
		origin.push_back(S[i]);
	}

	int result = 0;
	bool IsFlip = false;
	flip = origin;
	RFOR(j, origin.size(), 0){
		//from bottom find '-'
		if (origin[j] == '-')
		{
			FOR(i, 0, origin.size())
			{
				if (origin[i] == '+')
				{
					origin[i] = '-';
					IsFlip = true;
				}
				else if (origin[i] == '-')
					break;
			}
			if (IsFlip)
			{
				result += 1;
				IsFlip = false;
			}
			//flip over
			FOR(i, 0, j + 1)
				flip[i] = change(origin[j - i]);

			result += 1;
			origin = flip;
		}
	}

	cout << result << endl;
}

int main()
{
	if (SMALL)
	{
		freopen("B-small-attempt0.in", "r", stdin);
		freopen("B-small-attempt0.out", "w", stdout);
	}
	else
	{
		freopen("B-large.in", "r", stdin);
		freopen("B-large.out", "w", stdout);
	}

	int t, T;
	cin >> T;
	FOR(t, 0, T)
	{
		cout << "Case #" << t + 1 << ": ";
		Solve();
	}

	return 0;
}