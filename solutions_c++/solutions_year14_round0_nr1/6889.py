/* Problem A. Magic Trick */

/*
	using Set.
	n = 8
	runtime O(n)
	Mem O(n)
*/

#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>

using namespace std;

int n;
int m[4];

int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.out", "w", stdout);

	scanf("%d", &n);
	int r1, r2;
	std::set<int> myset[3];
	for (int i = 0; i < n; ++i)
	{
		for (int c = 0; c < 2; ++c)
		{
			myset[c].clear();
			scanf("%d", &r1);
			for (int j = 1; j < 5; ++j)
			{
				scanf("%d %d %d %d", &m[0], &m[1], &m[2], &m[3]);
				if (j==r1)
				{
					for (int k=0; k<4; ++k) myset[c].insert(m[k]);
				}
			}
		}
		std::set_intersection(myset[0].begin(), myset[0].end(),myset[1].begin(), myset[1].end(), std::inserter(myset[2],myset[2].begin()));

		printf("Case #%d: %s\n", i+1, (myset[2].size()==0)?"Volunteer cheated!":(myset[2].size()==1)?to_string(*(myset[2].begin())).c_str():"Bad magician!");
		myset[2].clear();
	}

	return 0;
}