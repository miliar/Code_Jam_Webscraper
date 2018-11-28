#include <iostream>
#include <stdio.h>
#include <string>
#include <limits>
#include <algorithm>

using namespace std;

float list1[1002];
float list2[1002];
int N;


int getNormalScore()
{
	int i = N-1;
	int j = N-1;
	int score = 0;
	while(true)
	{
		while(i >= 0 && list1[i] > list2[j])
			i--;
		if(i < 0)
			return N-score;
		if(list1[i] <= list2[j]) 
		{
			score++;
			i--;
			j--;
		}
	}
}

int getCheatScore()
{
	int i = 0;
	int j = 0;
	int k = N-1;
	int score = 0;
	while(i<N)
	{
		while(i < N && list1[i] < list2[j])
		{
			i++;
			k--;
			
		}
		while(i < N && list1[i] > list2[j])
		{
			i++;
			j++;
			score++;
		}
	}
	return score;
	
}


int main()
{
	int T;
	scanf("%d", &T);
	for(int index = 1; index <= T; index++)
	{
		scanf("%d", &N);
		for(int i = 0; i < N; i++)
			scanf("%f", &list1[i]);
		for(int i = 0; i < N; i++)
			scanf("%f", &list2[i]);

		sort(list1, list1+N);
		sort(list2, list2+N);

		printf("Case #%d: %d %d\n", index, getCheatScore(), getNormalScore());



	}


	//system("pause");
	return 0;
}
