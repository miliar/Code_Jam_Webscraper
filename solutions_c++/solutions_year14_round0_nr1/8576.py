#include <cstdio>

int nbTests;
int answers[2];
int arrange[2][4][4];

void inputTestCase()
{
	for(int id=0; id < 2; id++)
	{
		scanf("%d", &answers[id]);
		for(int row=0; row < 4; row++)
		{
			for(int col=0; col < 4; col++)
			{
				scanf("%d", &arrange[id][row][col]);
			}
		}
	}
}

int solve()
{
	bool valid[16];
	for(int pos=0; pos < 16; pos++)
		valid[pos]= false;
	for(int col=0; col < 4; col++)
		valid[arrange[0][answers[0]-1][col]-1]=true;
	for(int row=0; row < 4; row++)
		for(int col=0; col < 4; col++)
			valid[arrange[1][row][col]-1] &= (answers[1]-1 == row);
	
	int answer = -2;
	for(int id=0; id < 16; id++)
	{
		if(valid[id])
		{
			if(answer > 0)
				return -1;
			answer = id+1;
		}
	}
	return answer;
}

int main(void)
{
	scanf("%d", &nbTests);

	for(int test=0; test < nbTests; test++)
	{
		inputTestCase();
		int answer = solve();
		if(answer < 0)
		{
			if(answer == -1)
				printf("Case #%d: Bad magician!\n", test+1);
			else if(answer == -2)
				printf("Case #%d: Volunteer cheated!\n", test+1);
			else
				fprintf(stderr, "WTF, bad result: %d\n", answer);

		}
		else
			printf("Case #%d: %d\n", test+1, answer);
	}
	return 0;
}

