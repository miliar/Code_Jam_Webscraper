#include <iostream>
#include <cstdio>
#include <string.h>
using namespace std;


int main()
{
	FILE *fp = fopen("A-small-attempt1.in", "r");
	FILE *fout = fopen("A.out", "w");
	int t;
	//cin >> t;
	fscanf(fp, "%d", &t);
	for (int k = 0; k < t; k++)
	{
		int f[17];
		memset(f, 0, sizeof(f));
		int x;
		for (int kk = 0; kk < 2; kk++)
		{
			//cin >> x;
			fscanf(fp, "%d", &x);
			for (int i = 0; i < 4; i++)
			{
				int tt;
				for (int j = 0; j < 4; j++)
				{
					//cin >> tt;
					fscanf(fp, "%d", &tt);
					if (i == x - 1)
						f[tt] ++;
				}
			}
		}
		int ans = 0, count = 0;
		for (int i = 1; i < 17; i++)
		{
			if (f[i] == 2 && count == 0)
				ans = i;
			if (f[i] == 2) count++;
		}
		if (count == 0)
			//cout << "Case #" << t + 1 << ": Volunteer cheated!"<< endl;
			fprintf(fout, "Case #%d: Volunteer cheated!\n", k + 1);
		else if (count == 1)
			//cout << "Case #" << t + 1 << ": " << ans << endl;
			fprintf(fout, "Case #%d: %d\n", k + 1, ans);
		else if (count > 1)
			//cout << "Case #" << t + 1 << ": Bad magician!" << endl;
			fprintf(fout, "Case #%d: Bad magician!\n", k + 1);
	}
	fclose(fp);
    fclose(fout);
	return 0;
}
