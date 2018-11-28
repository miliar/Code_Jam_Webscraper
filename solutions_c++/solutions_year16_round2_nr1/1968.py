#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
 	freopen("out.txt", "w", stdout);

	int tests;
	int alpha[26];
	vector <int> ans;
	char str[2001];

	scanf("%d", &tests);

	for (int t = 1; t <= tests; t++)
	{
		scanf("%s", str);
		memset(alpha, 0, sizeof(alpha));
		ans.clear();
		
		int len = strlen(str);

		for (int i = 0; i < len; i++)
			alpha[str[i] - 65]++;
		
		// for (int i = 0; i < 26; i++)
		// 	printf("%c %d\n", i+65, alpha[i]);

		// 0
		int Z = alpha[25];
		alpha[4] -= Z;
		alpha[14] -= Z;
		alpha[17] -= Z;

		for (int i = 0; i < Z; i++)
			ans.push_back(0);
		
		// 6
		int X = alpha[23];
		alpha[18] -= X;
		alpha[8] -= X;

		for (int i = 0; i < X; i++)
			ans.push_back(6);

		// 8
		int G = alpha[6];
		alpha[4] -= G;
		alpha[8] -= G;
		alpha[7] -= G;
		alpha[19] -= G;

		for (int i = 0; i < G; i++)
			ans.push_back(8);

		// 3
		int H = alpha[7];
		alpha[19] -= H;
		alpha[17] -= H;
		alpha[4] -= H;
		alpha[4] -= H;

		for (int i = 0; i < H; i++)
			ans.push_back(3);

		// 2
		int W = alpha[22];
		alpha[19] -= W;
		alpha[14] -= W;

		for (int i = 0; i < W; i++)
			ans.push_back(2);

		// 7
		int S = alpha[18];
		alpha[4] -= S;
		alpha[21] -= S;
		alpha[4] -= S;
		alpha[13] -= S;

		for (int i = 0; i < S; i++)
			ans.push_back(7);

		// 5
		int V = alpha[21];
		alpha[8] -= V;
		alpha[5] -= V;
		alpha[4] -= V;

		for (int i = 0; i < V; i++)
			ans.push_back(5);

		// 4
		int F = alpha[5];
		alpha[14] -= F;
		alpha[20] -= F;
		alpha[18] -= F;

		for (int i = 0; i < F; i++)
			ans.push_back(4);

		// 1
		int O = alpha[14];
		alpha[13] -= O;
		alpha[4] -= O;

		for (int i = 0; i < O; i++)
			ans.push_back(1);

		// 9
		int I = alpha[8];
		for (int i = 0; i < I; i++)
			ans.push_back(9);

		sort(ans.begin(), ans.end());

		printf("Case #%d: ", t);
		for (int i = 0; i < ans.size(); i++)
			printf("%d", ans[i]);
		printf("\n");
	}


	return 0;
}