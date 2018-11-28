// ConsoleApplication1.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//


#include <stdio.h>

int main()
{
	int T = 0;
	
	FILE *f;
	FILE *fout;
	f = fopen("A-small-attempt0.in", "r");
	fout = fopen("output.txt", "w");
	fscanf(f, "%d", &T);
	//fscanf(f, "%d", &T);
	
	//printf("%d", T);

	
	for (int i = 0; i < T ; i++) {
		int row1 = 0;
		int row2 = 0;
		int card1[4][4];
		int card2[4][4];

		//first deck
		fscanf(f, "%d", &row1);		
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				fscanf(f, "%d", &card1[i][j]);
			}
		}
		/*
		for (int j = 0; j < 4; j++) {
			printf("%d ", card1[row1-1][j]);
		}*/


		//second deck		
		fscanf(f, "%d", &row2);
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				fscanf(f, "%d", &card2[i][j]);
			}
		}
	
		/*
		for (int j = 0; j < 4; j++) {
			printf("%d ", card2[row2-1][j]);
		}*/


		int count = 0;
		int answer = 0;

		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (card1[row1 - 1][i] == card2[row2 - 1][j])
				{
					count++;
					answer = card1[row1 - 1][i];
				}
			}
		}

		//printf("%d\n", row1);
		//printf("%d\n", row2);

		fprintf(fout, "Case #%d: ", i+1);
		if (count == 0)
			fprintf(fout,"Volunteer cheated!\n");
		else if (count == 1)
			fprintf(fout, "%d\n", answer);
		else if (count >= 2)
			fprintf(fout, "Bad magician!\n");
	}
	
	
	fclose(f);
	fclose(fout);


	return 0;
}


