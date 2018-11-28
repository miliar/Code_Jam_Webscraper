#include <iostream>
using namespace std;

int main()
{
	FILE *input, *output;
	input = fopen("A-small-attempt0.in", "r");
	output = fopen("output.txt", "w");

	int T;
	fscanf(input, "%d", &T);

	for (int t=1; t<=T; ++t)
	{
		fprintf(output, "Case #%d: ", t);
		int n, m;
		int cards1[4][4];
		int cards2[4][4];
		int check[17] = {0};

		fscanf(input, "%d", &n);
		for (int i=0; i<4; ++i)
		{
			for (int j=0; j<4; ++j)
			{
				fscanf(input, "%d", &cards1[i][j]);		
				if(i == n-1)
					check[cards1[i][j]]++;
			}
		}
		
		fscanf(input, "%d", &m);
		for (int i=0; i<4; ++i)
		{
			for (int j=0; j<4; ++j)
			{
				fscanf(input, "%d", &cards2[i][j]);
				if(i == m-1)
					check[cards2[i][j]]++;
			}
		}

		int cnt = 0;
		int answer = 0;
		for (int i=1; i<=16; ++i)
		{
			if (check[i] == 2)
			{
				++cnt;
				answer = i;
			}
		}

		if (cnt == 1)
			fprintf(output, "%d\n", answer);
		else if (cnt > 1)
			fprintf(output, "Bad magician!\n");
		else if (cnt == 0)
			fprintf(output, "Volunteer cheated!\n");
	}

	fclose(input);
	fclose(output);
	return 0;
}