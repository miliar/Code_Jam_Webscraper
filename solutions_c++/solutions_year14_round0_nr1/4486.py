#include <cstdio>
#include <vector>
#include <utility>
#include <cstring>
#include <cstdlib>
#include <map>
#include <iostream>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>
#include <cmath>
#include <set>
#include <assert.h>
#include <bitset>
#include <climits>
#include <sstream>

using namespace std;
#define pb push_back
#define mp make_pair
#define S second
#define F first
#define INF 0x3f3f3f3f
#define ll long long
#define mod 10
#define B 33
#define MAX 100011
#define eps 1e-7
#define ull unsigned long long

double pi = acos(-1);

typedef vector<int> vi;
typedef pair<int,int>ii;
typedef vector<ii> vii;

int c[4][4];

set<int> s;

int main() {
	int n;

	cin >> n;

	for (int k = 0; k < n; k++)
	{
		s.clear();
		int r;
		cin >> r;

		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				cin >> c[i][j];
			}
		}

		for (int i = 0; i < 4; ++i)
		{
			s.insert(c[r-1][i]);
		}

		int total = 0;
		int solution;

		cin >> r;

		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				cin >> c[i][j];
			}
		}

		for (int i = 0; i < 4; ++i)
		{
			if (s.count(c[r-1][i]))
			{
				total++;
				solution = c[r-1][i];
			}
		}

		if(total == 0)
		{
			printf("Case #%d: Volunteer cheated!\n", k+1);
		}
		else if (total == 1)
		{
			printf("Case #%d: %d\n", k+1 ,solution);
		}
		else
		{
			printf("Case #%d: Bad magician!\n", k+1);
		}
	}
	return 0;
}