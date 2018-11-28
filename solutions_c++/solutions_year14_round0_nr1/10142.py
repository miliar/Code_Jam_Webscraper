#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int answer, answer2;
int rows[5][5], rows2[5][5];
bool used[20];

void read()
{
	scanf("%d", &answer);
	for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
			scanf("%d", &rows[i][j]);
	scanf("%d", &answer2);
	for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
			scanf("%d", &rows2[i][j]);
	
}

void clean()
{
	for(int i=0; i<20; i++)
		used[i] = false;
}

void solveTask(int number)
{
	clean();
	for(int i=0; i<4; i++)
		used[rows[answer-1][i]] = true;
	bool badMagician = false;
	int card = 0;
	for(int i=0; i<4; i++)
	{
		if(used[rows2[answer2-1][i]])
		{
			if(!card)
				card = rows2[answer2-1][i];
			else
				badMagician = true;
		}
	}
	printf("Case #%d: ", number); 
	if(!card)
		printf("Volunteer cheated!");
	else if(badMagician)
		printf("Bad magician!");
	else
		printf("%d", card);
	printf("\n");
}

int main()
{

	int t;
	scanf("%d", &t);
	for(int q=1; q<=t; q++)
	{
		read();
		solveTask(q);	
	}
	return 0;
}
