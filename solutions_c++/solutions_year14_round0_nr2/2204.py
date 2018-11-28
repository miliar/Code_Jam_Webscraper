#pragma warning (disable : 4996)

#include <stdlib.h>
#include <iostream>
#include <vector>
#include <string>
#include <assert.h>
#include <stack>
#include <algorithm>
#include <ios>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <queue>
#include <set>
#include <functional>
#include <cmath>
#include <sstream>
#include <map>
#include <memory.h>
#include <stdio.h>
#include <cassert>
#include <string.h>

#define forn(i , n) for (int i = 0; i < n; ++i)
#define down(i, n) for (int i = n - 1; i >= 0; --i)


using namespace std;

typedef unsigned long long int u64;
typedef long long int i64;
typedef vector<int> vint;
typedef pair<int, int> pint;
typedef pair<i64, i64> pi64;


#define FILE_NAME "file"

#define CONTEST "bees"

const int inf = 2000000000;


struct Node
{
	int p;
	int h;
	Node()
	{
		p = -1;
		h = 1;
	}
};



int find(vector<Node> & arr, int v)
{
	if (arr[v].p == -1)
		return v;
	return arr[v].p = find(arr, arr[v].p);

}

void uni(vector<Node> & arr, int a, int b)
{
	a = find(arr, a);
	b = find(arr, b);
	if (arr[a].h < arr[b].h)
	{
		arr[a].p = b;
		arr[b].h += arr[a].h;
	}
	else
	{
		arr[b].p = a;
		arr[a].h += arr[b].h;
	}
}

struct Rebro
{
	int a, b, v;

	bool operator< (const Rebro & b) const
	{
		return v < b.v;
	}

};

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout << fixed << setprecision(9);
#ifdef FILE_INPUT
	freopen(FILE_NAME ".in", "r", stdin);
	freopen(FILE_NAME ".out", "w", stdout);
#else
	freopen(CONTEST ".in", "r", stdin);
	freopen(CONTEST ".out", "w", stdout);
#endif
	int T;
	cin >> T;
	forn(t, T)
	{
		double c, f, x;
		cin >> f >> c >> x;
		double speed = 2;
		double ans = 0;
		double curr = 0;


		while (1)
		{
			double timeToEnd;
			double timeToNextF;
			double timeToEndWithNext;

			timeToEnd = (x - curr) / speed;

			timeToNextF = (f - curr) / speed;

			timeToNextF = max(timeToNextF, (double)0);

			timeToEndWithNext = timeToNextF + (x) / (speed + c);
			if (timeToEndWithNext < timeToEnd)
			{
				ans += timeToNextF;
				speed += c;
				curr = 0;
			}
			else
			{
				ans += timeToEnd;
				break;
			}

		}



		cout << "Case #" << t + 1 << ": " << ans << "\n";
	}

	return 0;

}