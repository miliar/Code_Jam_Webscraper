#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <climits>
using namespace std;

int main ()
{
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int TC; scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++)
	{
		set<int> a1, a2;
		int n; 
		scanf("%d", &n); n--;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				int t; scanf("%d", &t);
				if (i == n)	a1.insert(t);
			}
		scanf("%d", &n); n--;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				int t; scanf("%d", &t);
				if (i == n)	a2.insert(t);
			}
		vector<int> rs(8);
		vector<int>::iterator p = set_intersection(a1.begin(), a1.end(), a2.begin(), a2.end(), rs.begin());
		rs.resize(p - rs.begin());
		printf("Case #%d: ", tc);
		if (rs.size() == 0) printf("Volunteer cheated!\n");
		else if(rs.size() > 1)	printf("Bad magician!\n");
		else printf("%d\n", rs[0]);

	}

}