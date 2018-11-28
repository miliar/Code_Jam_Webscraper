// Mushroom_monster.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>


int _tmain(int argc, _TCHAR* argv[])
{
	FILE *pFileRead, *pFileWrite;
	fopen_s(&pFileRead, "A-large.in", "r+");
	fopen_s(&pFileWrite, "A-large.out", "w+");

	int testCases;
	fscanf_s(pFileRead, "%d", &testCases);
	for (int i = 1; i <= testCases; ++i)
	{
		unsigned int N;
		fscanf_s(pFileRead, "%u", &N);

		std::vector<int> mushrooms_on_plate(N, 0);
		for (int j = 0; j < N; ++j) {
			unsigned int m;
			fscanf_s(pFileRead, "%u", &m);
			mushrooms_on_plate[j] = m;
		}

		//computeA
		unsigned int ComputeA = 0;
		int max_difference_B = 0;
		unsigned int ComputeB = 0;

		//computeA && difference_B
		for (int j = 1; j < N; ++j) {
			
			//computeA
			if (mushrooms_on_plate[j - 1] > mushrooms_on_plate[j])
				ComputeA += (mushrooms_on_plate[j - 1] - mushrooms_on_plate[j]);

			//compute difference_B
			int curr_diff = mushrooms_on_plate[j - 1] - mushrooms_on_plate[j];
			if (curr_diff > max_difference_B)
				max_difference_B = curr_diff;
		}

		//computeB
		for (int j = 0; j < N - 1; ++j) {
			if (mushrooms_on_plate[j] > max_difference_B)
				ComputeB += max_difference_B;
			else
				ComputeB += mushrooms_on_plate[j];

		}

		fprintf_s(pFileWrite, "Case #%d: %u %u\n", i, ComputeA, ComputeB);

	}

	



	return 0;
}

