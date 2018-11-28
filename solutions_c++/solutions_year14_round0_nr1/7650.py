#include <fstream>
#include <iostream>
using namespace std;
int main()
{
	ofstream fout("file.out");
	int T, map[4][4], c, r, cur;
	bool vis[17];
	scanf_s("%d", &T);
	for (int t = 0; t < T; ++t)
	{
		for (int i = 0; i <= 16; ++i)
			vis[i] = false;
		scanf_s("%d", &c);
		c--;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				scanf_s("%d", &map[i][j]);
		for (int i = 0; i < 4; ++i)
			vis[map[c][i]] = true;
		r = 0;
		scanf_s("%d", &c);
		c--;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				scanf_s("%d", &map[i][j]);
		for (int i = 0; i < 4; ++i)
			if (vis[map[c][i]])
				++r, cur = map[c][i];
		//printf("Case #%d: ", t + 1);
		fout << "Case #" << t + 1 << ": ";
		if (r == 0)
			//	printf("Volunteer cheated!\n");
			fout << "Volunteer cheated!\n";
		else if (r == 1)
			//	printf("%d\n", cur);
			fout << cur << endl;
		else
			//printf("Bad magician!\n");
			fout << "Bad magician!\n";
	}
	return 0;
}