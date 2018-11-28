#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

int main()
{
	int T,t;
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t<=T; ++t)
	{
		set<int> S1;
		set<int> S2;
		int r;
		scanf("%d",&r);
		for (int i = 1; i <= 4; ++i) 
		{
			for (int j = 1; j<=4; ++j)
			{
				int x;
				scanf("%d",&x);
				if (r == i)
					S1.insert(x);
			}
		}
		scanf("%d",&r);
		for (int i = 1; i <= 4; ++i) {
			for (int j = 1; j<=4; ++j) {
				int x;
				scanf("%d",&x);
				if (r == i)
					S2.insert(x);
			}
		}
		
		set<int> S_int;
		set_intersection (S1.begin(),S1.end(),S2.begin(),S2.end(), inserter(S_int, S_int.begin()));
		if (S_int.size() == 1)
			printf("Case #%d: %d\n", t, *S_int.begin());
		else if (S_int.size() == 0)
			printf("Case #%d: Volunteer cheated!\n", t);
		else
			printf("Case #%d: Bad magician!\n", t);
	}
	return 0;
}
