#include <cstdio>

using namespace std;

int A1, A2;
int T1[5][5], T2[5][5];

void read()
{
	// read
	scanf("%d", &A1);
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			scanf("%d ", &T1[i][j]);

	scanf("%d", &A2);
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			scanf("%d ", &T2[i][j]);
}

void solve()
{
	A1--;
	A2--;
	// solve
	int no = 0, card = 0;
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			if (T1[A1][i] == T2[A2][j])
			{
				++no;
				card = T1[A1][i];
			}

	if (no == 0)
		printf("Volunteer cheated!\n");
	else if (no == 1)
		printf("%d\n", card);
	else
		printf("Bad magician!\n");
}

int main()
{
	int T;

	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);

	scanf("%d",&T);

	for (int i = 0; i < T; ++i)
	{
		printf("Case #%d: ", i + 1);
		read();
		solve();
	}

	return 0;
}