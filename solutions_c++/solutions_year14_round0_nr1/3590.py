#include <iostream>
#include <cstdio>

using namespace std;


int main (void)
{
	int T, caso = 1;
	cin >> T;

	while (T--)
	{
		int r1;
		int candidates[17] = { 0 };

		cin >> r1;
		for (int i = 1; i <= 4; ++i)
			for (int j = 1; j <= 4; ++j)
			{
				int x; cin >> x;
				if (i == r1) candidates[x]++;
			}
		cin >> r1;
		for (int i = 1; i <= 4; ++i)
			for (int j = 1; j <= 4; ++j)
			{
				int x; cin >> x;
				if (i == r1) candidates[x]++;
			}
		int ans = -1;
		for (int i = 1; i <= 16; ++i)
			if (candidates[i] == 2)
			{
				if (ans == -1) ans = i;
				else ans = 20;
			}

		printf("Case #%d: ", caso++);
		if (ans == -1) printf("Volunteer cheated!\n");
		else if (ans == 20) printf("Bad magician!\n");
		else printf("%d\n", ans);
	}

	return 0;
}