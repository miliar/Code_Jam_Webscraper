#include <iostream>

using namespace std;

#define REP(v, repeat) for(int v=0; v<(repeat); ++v)
#define FOR(v, start, end) for(int v=(start); v<=(end); ++v)

int main()
{
#ifdef _CONSOLE
	freopen("input.txt", "r", stdin);
	freopen("output.txt","w+", stdout);
#endif

	int table[5][5];
	int suffle[5][5];
	int t;
	scanf("%d", &t);
	FOR(tc, 1, t)
	{
		int n1, n2;
		scanf("%d", &n1);
		FOR(i, 1, 4) FOR(j, 1, 4) scanf("%d", &table[i][j]);
		scanf("%d", &n2);
		FOR(i, 1, 4) FOR(j, 1, 4) scanf("%d", &suffle[i][j]);

		int cnt = 0, num;
		FOR(i, 1, 4) FOR(j, 1, 4)
		if (table[n1][i] == suffle[n2][j])
		{
			num = table[n1][i];
			++cnt;
		}
		printf("Case #%d: ", tc);
		switch (cnt)
		{
		case 0: printf("Volunteer cheated!\n"); break;
		case 1: printf("%d\n", num); break;
		default: printf("Bad magician!\n");
		}
	}
	return 0;
}