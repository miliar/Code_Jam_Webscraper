#include <string>
#include <cstdio>
#include <set>
#include <algorithm>

using namespace std;

set<int> readPossible()
{
	int row;
	scanf("%d", &row);
	
	set<int> ans;
	for (int theRow = 1; theRow <= 4; theRow++)
		for (int i = 0; i < 4; i++)
		{
			int x;
			scanf("%d", &x);
			if (row == theRow)
				ans.insert(x);
		}
	
	return ans;
}

void solve()
{
	set<int> a = readPossible(), b = readPossible();
	set<int> x;
	set_intersection(a.begin(), a.end(), b.begin(), b.end(), inserter(x, x.begin()));
	
	if (x.empty())
		printf("Volunteer cheated!");
	else if (x.size() > 1)
		printf("Bad magician!");
	else
		printf("%d", *x.begin());
}

int main()
{	
	freopen("asmall.in", "r", stdin);
	freopen("asmall.out", "w", stdout);
	int nTests;
	scanf("%d", &nTests);
	for (int i = 0; i < nTests; i++)
	{
		printf("Case #%d: ", i + 1);
		solve();
		printf("\n");
	}
	
	return 0;
}
