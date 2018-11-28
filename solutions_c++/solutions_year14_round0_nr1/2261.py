#include <cstdio>
#include <cstring>

using namespace std;
int main()
{
	// freopen("in", "r", stdin);
	// freopen("out", "w", stdout);
	int TC, ans1, ans2, deck1[5][5], deck2[5][5], res, check[17], c;
	scanf("%d", &TC);
	c = 1;
	while (TC--){
		res = 0;
		memset(check, 0, sizeof check);
		scanf("%d", &ans1);
		for (int i = 1; i < 5; ++i)
		{
			for (int j = 1; j < 5; ++j)
			{
				scanf("%d", &deck1[i][j]);
				if (i == ans1) check[deck1[i][j]] = 1;
			}
		}
		scanf("%d", &ans2);
		for (int i = 1; i < 5; ++i)
		{
			for (int j = 1; j < 5; ++j)
			{
				scanf("%d", &deck2[i][j]);
				if (i == ans2 && check[deck2[i][j]] == 1){
					if(res == 0) res = deck2[i][j];
					else {
						res = -1;
					}
				}
			}
		}
		printf("Case #%d: ", c++);
		if (res == 0) printf("Volunteer cheated!\n");
		else if (res == -1) printf("Bad magician!\n");
		else printf("%d\n", res);
	}
	return 0;
}