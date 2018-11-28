// Infinite_House_of_Pancakes.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <algorithm>
#include <set>

struct Comparator {
	bool operator()(unsigned int l, unsigned int r) {
		return l > r;
	}
};

typedef std::multiset<unsigned int, Comparator> descMultiSet;


int DivideSet(descMultiSet dms, int x) {
	unsigned int count = 0;
	
	auto first = *dms.begin();

	while (first > x) {
		auto begin = dms.begin();
		unsigned int rest = *begin - x;
		dms.erase(begin);
		dms.insert(x);
		dms.insert(rest);
		first = *dms.begin();
		count++;
	}
	return count;
}



int _tmain(int argc, _TCHAR* argv[])
{
	FILE *pFileRead, *pFileWrite;
	fopen_s(&pFileRead, "B-small-attempt9.in", "r+");
	fopen_s(&pFileWrite, "B-small-attempt9.out", "w+");

	int testCases;
	fscanf_s(pFileRead, "%d", &testCases);
	for (int i = 1; i <= testCases; ++i) 
	{
		descMultiSet dms;

		unsigned int diners;
		fscanf_s(pFileRead, "%d", &diners);

		for (unsigned int j = 0; j < diners; ++j) {
			unsigned int plate;
			fscanf_s(pFileRead, "%d", &plate);
			dms.insert(plate);
		}

		unsigned int max = *dms.begin();
		unsigned int result = *dms.begin();

		for (unsigned int k = 1; k < max - 1; ++k) {
			result = std::min(result, k + DivideSet(dms, k));
		}

		fprintf(pFileWrite, "Case #%d: %d \n", i, result);
	}

	return 0;
}

