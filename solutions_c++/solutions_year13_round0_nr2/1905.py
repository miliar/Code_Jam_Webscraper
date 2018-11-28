// GoogleCodeJam_B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <cstring>

#define MAX_SIZE 100

using namespace std;

ifstream fin("D:\\Input.in");
ofstream fout("D:\\Output.txt");

int T, N, M, mapgrass[MAX_SIZE][MAX_SIZE], checkgrass[MAX_SIZE][MAX_SIZE];

void cutgrass()
{
	for(int q = 0; q < N; q++)
	{
		int maxheight = 0;
		for(int w = 0; w < M; w++) if(mapgrass[q][w] > maxheight) maxheight = mapgrass[q][w];
		for(int w = 0; w < M; w++) if(mapgrass[q][w] == maxheight) checkgrass[q][w] = 1;
	}
	for(int q = 0; q < M; q++)
	{
		int maxheight = 0;
		for(int w = 0; w < N; w++) if(mapgrass[w][q] > maxheight) maxheight = mapgrass[w][q];
		for(int w = 0; w < N; w++) if(mapgrass[w][q] == maxheight) checkgrass[w][q] = 1;
	}
}

bool finalcheckgrass()
{
	for(int q = 0; q < N; q++) for(int w = 0; w < M; w++) if(checkgrass[q][w] == 0) return false;
	return true;
}

int main()
{
	fin >> T;
	for(int i = 0; i < T; i++)
	{
		fin >> N >> M;
		for(int j = 0; j < N; j++) for(int k = 0; k < M; k++) fin >> mapgrass[j][k];
		memset(checkgrass, 0, sizeof checkgrass);
		cutgrass();
		if(finalcheckgrass()) fout << "Case #" << i + 1 << ": " << "YES" << "\n";
		else fout << "Case #" << i + 1 << ": " << "NO" << "\n";
	}
	return 0;
}