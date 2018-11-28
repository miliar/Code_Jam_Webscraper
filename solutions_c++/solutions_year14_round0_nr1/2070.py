#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include <time.h>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	int caMax;
	int ans1[10][10], ans2[10][10];
	int r1, r2;
	vector<int> ans;

	FILE *fin = fopen("1.in", "r");
	FILE *fout = fopen("out.txt", "w");
	fscanf(fin,"%d", &caMax);
	for (int ca = 1; ca <= caMax; ca++)
	{
		ans.clear();

		fscanf(fin, "%d", &r1);
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				fscanf(fin, "%d", &ans1[i][j]);
		fscanf(fin, "%d", &r2);
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				fscanf(fin, "%d", &ans2[i][j]);

		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (ans1[r1 - 1][i] == ans2[r2 - 1][j])
					ans.push_back(ans1[r1-1][i]);

		if (ans.size() > 1)
			fprintf(fout, "Case #%d: Bad magician!\n", ca);
		else if (ans.empty())
			fprintf(fout, "Case #%d: Volunteer cheated!\n", ca);
		else 
			fprintf(fout, "Case #%d: %d\n", ca, ans[0]);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}