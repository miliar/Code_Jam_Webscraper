#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <set>
using namespace std;
const int Maxn = 4;
int board[Maxn][Maxn];
int n;
set<int>st;
int main()
{
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas)
	{
		printf("Case #%d: ", cas);
		scanf("%d", &n);
		st.clear();
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
			{
				scanf("%d", &board[i][j]);
				if (i == n - 1) st.insert(board[i][j]);
			}
		scanf("%d", &n);
		int ans, cnt = 0;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
			{
				scanf("%d", &board[i][j]);
				if (i == n - 1)
				{
					if (st.count(board[i][j])) cnt++, ans = board[i][j];
				}
			}
		if (cnt == 1) printf("%d\n", ans);
		else if (cnt == 0) printf("Volunteer cheated!\n");
		else puts("Bad magician!");
	}
	return 0;
}