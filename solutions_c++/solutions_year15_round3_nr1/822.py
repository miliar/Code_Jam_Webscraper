#include<iostream>
#include<stdio.h>
#include<queue>
#include<vector>
#pragma warning(disable:4996)

using namespace std;	


int main()
{
	FILE *in = fopen("input.txt", "r");
	FILE *out = fopen("output.txt", "w");
	int TT;
	int R, C, W;
	fscanf(in, "%d", &TT);
	for (int t = 1; t <= TT;t++)
	{
		fscanf(in, "%d %d %d", &R, &C, &W);
		int B = R*(C/W) + W - 1;
		if (C%W != 0)B++;
		fprintf(out, "Case #%d: %d\n", t, B);
	}
} 