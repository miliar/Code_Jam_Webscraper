#include <cstdio>
#include <iostream>
#include <stdlib.h>

using namespace std;

int main(void)
{
	FILE* in = fopen("A-large.in", "r");
	FILE* out;

	if(!in)
	{
		cout << "File A-large.in could not be opened!!\n";
		exit(-1);
	}

	out = fopen("A-large.out", "w");

	if(!out)
	{
		fclose(in);
		cout << "File A-large.out could not be opened!!\n";
		exit(-1);
	}

	int T;
	char strS[3000];
	int Smax;

	fscanf(in, "%d", &T);

	for(int i = 0; fscanf(in, "%d %s", &Smax, strS) != EOF && i < T; i++)
	{
		int answer = 0;
		int alreadyStoodUp = (int) (strS[0] - '0');

		if(Smax != 0)
		{
			/*for(int j = Smax-1; j > -1 && answer > 0; j--)
			{
				if(strS[j] != '0')
				{
					answer -= (int) (strS[j] - '0');
				}

			}*/

			for(int j = 1; j < Smax && alreadyStoodUp < Smax; j++)
			{
				if(strS[j] != '0')
				{
					//int sub = alreadyStoodUp - ((int)strS[j] - '0');
					int sub = alreadyStoodUp - j;

					if(sub < 0)
					{
						answer += -sub;
						alreadyStoodUp += -sub;
					}

					alreadyStoodUp += ((int)strS[j] - '0');
				}
			}

			if(alreadyStoodUp < Smax)
				answer += (Smax-alreadyStoodUp);
		}

		fprintf(out, "Case #%d: %d\n", (i+1), answer);
	}

	fclose(out);
	fclose(in);
	return 0;
}