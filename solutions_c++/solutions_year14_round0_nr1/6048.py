#include<iostream>
#include<iomanip>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<functional>
#include<string>
#include<cstdlib>
#include<cmath>
#include<map>
#include<set>
#include<list>
#include<utility>
#include<cstring>
#include<queue>
#include<stack>
#include<climits>
using namespace std;

#define rrepp(i, from, to) for (int i = (from); i <= (to); ++i)
#define rrep(i, from, to) for (int i = (from); i < (to); ++i)
#define repp(i, from, to) for (i = (from); i <= (to); ++i)
#define rep(i, from, to) for (i = (from); i < (to); ++i)


int main()
{
	int t;
	scanf("%d", &t);
	rrepp (i, 1, t) {
		int r1, r2;
		int p1[4][4], p2[4][4];
		scanf("%d", &r1);
		rrep(j, 0, 4)
		{
			scanf("%d%d%d%d", &p1[j][0], &p1[j][1], &p1[j][2], &p1[j][3]);
		}
		scanf("%d", &r2);
		rrep(j, 0, 4)
		{
			scanf("%d%d%d%d", &p2[j][0], &p2[j][1], &p2[j][2], &p2[j][3]);
		}
		set<int> s1(&p1[r1 - 1][0], &p1[r1 - 1][0] + 4);
		set<int> s2(&p2[r2 - 1][0], &p2[r2 - 1][0] + 4);
		set<int> s;
		for each (auto c in s1) {
			if (s2.find(c) != s2.end()) {
				s.insert(c);
			}
		}
		if (s.size() == 1) {
			printf("Case #%d: %d\n", i, *s.begin());
		} else if (s.size() > 1) {
			printf("Case #%d: Bad magician!\n", i);
		} else {
			printf("Case #%d: Volunteer cheated!\n", i);
		}
	}
	return 0;
}