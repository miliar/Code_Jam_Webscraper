#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;

int T, A[8];

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int t = 0; t < T; ++t)
	{
		int a, b; scanf("%d", &a); --a;
		int s = 0;
		for (int i = 0; i < 4; ++i) for (int j = 0; j < 4; ++j)
		{
			int x; scanf("%d", &x);
			if (i == a) A[s++] = x;
		}
		scanf("%d", &b); --b;
		for (int i = 0; i < 4; ++i) for (int j = 0; j < 4; ++j)
		{
			int x; scanf("%d", &x);
			if (i == b) A[s++] = x;
		}
		sort(A, A + 8);
		vector<int> ans;
		int prev = -1;
		for (int i = 0; i < 8; ++i)
		{
			if (A[i] == prev) ans.push_back(prev);
			else prev = A[i];
		}
		printf("Case #%d: ", t + 1);
		if (ans.size() == 1) printf("%d\n", ans[0]);
		else if (ans.empty()) printf("Volunteer cheated!\n");
		else printf("Bad magician!\n");
	}
	return 0;
}
