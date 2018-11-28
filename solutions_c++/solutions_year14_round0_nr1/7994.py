#include <iostream>
#include <cstdio>
#include <set>


using namespace std;

int main()
{
	int T;
	scanf("%d", &T);

	for (int c = 1; c <= T; ++c) {
		set<int> A;
		set<int> B;

		int nL1, nL2;

		scanf("%d", &nL1);

		for (int j = 0; j < 4; ++j) {		
			for (int i = 0; i < 4; ++i) {
				int v;
				scanf("%d", &v);
				if (j + 1 == nL1)
					A.insert(v);
			}
		}

		scanf("%d", &nL2);
		for (int j = 0; j < 4; ++j) {		
			for (int i = 0; i < 4; ++i) {
				int v;
				scanf("%d", &v);
				if (j + 1 == nL2)
					B.insert(v);
			}
		}

		set<int> sol;
		set<int>::iterator it = A.begin(), ed = A.end();

		while (it != ed) {
			if (B.find(*it) != B.end()) sol.insert(*it);
			++it;
		}

		printf("Case #%d:", c);
		if (sol.size() == 1) {
			printf(" %d\n", *sol.begin());
		} else if (sol.size() == 0) {
			printf(" Volunteer cheated!\n");
		} else {
			printf(" Bad magician!\n");
		}
	}

	return 0;
}


