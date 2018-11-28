#include <stdio.h>
#include <vector>

#define FILENAME "B-large.in"

void main()
{
	FILE *fIn = fopen(FILENAME, "rb");
	FILE *fOut = fopen("QR_B_out.txt", "wb");

	int T;
	fscanf(fIn, "%d", &T);
	for(int t = 1; t <= T; ++t)
	{
		int row, col;
		fscanf(fIn, "%d %d", &row, &col);
		int *pLawn = new int[row * col];

		std::vector<int> vRow(row);
		std::vector<int> vCol(col);

		bool flag = false;
		for(int r = 0; r < row; ++r)
			for(int c = 0; c < col; ++c)
			{
				fscanf(fIn, "%d", &pLawn[r*col + c]);
				if(pLawn[r*col + c] > 100 || pLawn[r*col + c] < 0)
					goto out;
				if(pLawn[r*col + c] > vRow[r])
					vRow[r] = pLawn[r*col + c];
				if(pLawn[r*col + c] > vCol[c])
					vCol[c] = pLawn[r*col + c];
			}

		for(int r = 0; r < row; ++r)
			for(int c = 0; c < col; ++c)
			{
				if(pLawn[r*col + c] < vRow[r] && pLawn[r*col + c] < vCol[c])
					goto out;
			}
		flag = true;

out:
		if(flag)
			fprintf(fOut, "Case #%d: YES\r\n", t);
		else
			fprintf(fOut, "Case #%d: NO\r\n", t);
		delete[] pLawn;
	}

	fclose(fIn);
	fclose(fOut);
}