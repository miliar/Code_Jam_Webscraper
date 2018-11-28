#include <stdio.h>
#include <stdlib.h>

void guess_number(int cards_first[4][4], int cards_second[4][4], int first_ans, int second_ans,int case_num)
{
	int valid_ans;
	int count_valid_ans = 0;
	int i, j;
	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 4; j++)
		{
			if (cards_first[first_ans][i] == cards_second[second_ans][j])
			{
				count_valid_ans++;
				valid_ans = cards_first[first_ans][i];
			}
		}
	}
	if (count_valid_ans == 0)
		printf("Case #%d: Volunteer cheated!\n", case_num);
	else if (count_valid_ans == 1)
		printf("Case #%d: %d\n", case_num, valid_ans);
	else
		printf("Case #%d: Bad magician!\n", case_num);
}

int main(void)
{
	FILE * fd = fopen("D:\\A-small-attempt0.in","r");
	if (fd == NULL)
	{
		perror("fopen");
		return 1;
	}

	int i, row, col;
	int num_tests;
	int first_ans, second_ans, cards_first[4][4], cards_second[4][4];

	fscanf(fd, "%d", &num_tests);
	//printf("num tests : %d \n", num_tests);

	for (i = 0; i < num_tests; i++)
	{
		fscanf(fd, "%d", &first_ans);
		//printf("first ans: %d \n", first_ans);
		first_ans--;
		for (row = 0; row < 4; row++)
		{
			for (col = 0; col < 4; col++)
			{
				fscanf(fd, "%d", &cards_first[row][col]);
				//printf("cards_first[%d][%d] = %d\t", row, col, cards_first[row][col]);
			}
			//printf("\n");
		}

		fscanf(fd, "%d", &second_ans);
		//printf("second ans: %d \n", second_ans);
		second_ans--;

		for (row = 0; row < 4; row++)
		{
			for (col = 0; col < 4; col++)
			{
				fscanf(fd, "%d", &cards_second[row][col]);
				//printf("cards_first[%d][%d] = %d", row, col, cards_second[row][col]);
			}
			//printf("\n");
		}
		guess_number(cards_first, cards_second, first_ans, second_ans,i+1);

	}

	getchar();

	return 0;
}
