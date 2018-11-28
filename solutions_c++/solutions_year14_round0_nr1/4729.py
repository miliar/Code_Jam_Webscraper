#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int n_case, ans1, ans2, cnt_ans, ans;
int first[5][5], second[5][5];
vector<int> temp;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	while(scanf("%d", &n_case) != EOF)
	{
		for (int c = 0; c < n_case; c++)
		{
			/// init
			temp.clear();
			cnt_ans = 0;
			/// read first data
			scanf("%d", &ans1);
			for (int i = 1; i <= 4; i++)
			{
				for (int k = 0; k < 4; k++)
					scanf("%d", &first[i][k]);
			}
			/// read second data
			scanf("%d", &ans2);
			for (int i = 1; i <= 4; i++)
			{
				for (int k = 0; k < 4; k++)
					scanf("%d", &second[i][k]);
			}
			/// calc
			for (int i = 0; i < 4; i++)
				temp.push_back(first[ans1][i]);
			for (int i = 0; i < 4; i++)
			{
				vector<int>::iterator ret = find(temp.begin(), temp.end(), second[ans2][i]);

				if (ret != temp.end())
					cnt_ans++, ans = *ret;
			}
			/// output
			if (cnt_ans == 1)
				printf("Case #%d: %d\n", c+1, ans);
			else if (cnt_ans == 0)
				printf("Case #%d: Volunteer cheated!\n", c+1);
			else
				printf("Case #%d: Bad magician!\n", c+1);
		}
	}

	return 0;
}
