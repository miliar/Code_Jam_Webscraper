//
//  main.cpp
//  Lawnmower
//
//  Created by dmp on 4/13/13.
//  Copyright (c) 2013 dmp. All rights reserved.
//

#include <iostream>
#include <vector>
#include <map>
#include <list>

#define MaxN 100
#define MaxM 100

using namespace std;

void processCase()
{
	int N, M;
	int field[MaxN][MaxM];

	int maxColumn[MaxN];
	int maxRow[MaxM];
	
	bzero(maxColumn, sizeof(maxColumn));
	bzero(maxRow, sizeof(maxRow));
	
	cin >> N;
	cin >> M;
	
	for(int i = 0; i < N; i++)
	{
		for(int j = 0; j < M; j++)
		{
			int value;
			cin >> value;

			if( value > maxColumn[i]) maxColumn[i] = value;
			if( value > maxRow[j]) maxRow[j] = value;
			field[i][j] = value;
		}
	}

	for(int i = 0; i < N; i++)
	{
		for(int j = 0; j < M; j++)
		{
			if( min(maxColumn[i], maxRow[j]) != field[i][j])
			{
				printf("NO");
				return;
			}
		}
	}
	
	printf("YES");
}

int main(int argc, const char * argv[])
{
	int T;
	cin >> T;
	
	for (int i = 0; i < T; i++) {
		printf("Case #%d: ", i + 1);
		processCase();
		printf("\n");
	}
	
    return 0;
}
