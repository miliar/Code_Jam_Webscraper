// Dijkstra.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>

int Multiply(int x, int y) {
	if (x > 0 && y > 0) {
		if (x == 1)
			return y;
		else if (x == 'i') {
			if (y == 'i')
				return -1;
			if (y == 'j')
				return 'k';
			if (y == 'k')
				return -'j';
			if (y == 1)
				return 'i';
		}
		else if (x == 'j') {
			if (y == 'i')
				return -'k';
			if (y == 'j')
				return -1;
			if (y == 'k')
				return 'i';
			if (y == 1)
				return 'j';
		}
		else if (x == 'k') {
			if (y == 'i')
				return 'j';
			if (y == 'j')
				return -'i';
			if (y == 'k')
				return -1;
			if (y == 1)
				return 'k';
		}
		else
			return 0;
	}
	else if (x < 0 && y > 0)
		return -Multiply(-x, y);
	else if (x < 0 && y < 0)
		return Multiply(-x, -y);
	else
		return -Multiply(x, -y);
}


int _tmain(int argc, _TCHAR* argv[])
{
	FILE *pFileRead, *pFileWrite;
	fopen_s(&pFileRead, "C-small-attempt2.in", "r+");
	fopen_s(&pFileWrite, "C-small-attempt2.out", "w+");

	int testCases;
	fscanf_s(pFileRead, "%d", &testCases);
	for (int i = 1; i <= testCases; ++i) 
	{
		int L, X;
		fscanf_s(pFileRead, "%d", &L);
		fscanf_s(pFileRead, "%d", &X);

		char* str = new char[L + 1];
		fscanf_s(pFileRead, "%s", str, L + 1);

		int index_i = 0;
		int max_index_i = L * 4;
		int search_i = 1;
		for (;index_i < L * X && index_i < max_index_i; ++index_i) {
			search_i = Multiply(search_i, str[index_i % L]);
			if (search_i == 'i')
				break;
		}

		int index_j = index_i + 1;
		int max_index_j = index_i + 1 + L * 4;
		int search_j = 1;
		if (search_i == 'i') {
			for (;index_j < L * X && index_j < max_index_j; ++index_j) {
				search_j = Multiply(search_j, str[index_j % L]);
				if (search_j == 'j')
					break;
			}
		}

		int index_k = index_j + 1;
		int max_index_k = index_j + 1 + L * 4;
		int search_k = 1;
		if (search_i == 'i' && search_j == 'j') {
			for (;index_k < L * X; ++index_k) {
				search_k = Multiply(search_k, str[index_k % L]);
			}
		}

		if (search_i == 'i' && search_j == 'j' && search_k == 'k')
			fprintf(pFileWrite, "Case #%d: YES \n", i);
		else
		   fprintf(pFileWrite, "Case #%d: NO \n", i);

		int len = strlen(str);
	}
}

