// clang++ -o C template.cpp 

#include <stdio.h> 
#include <algorithm> 
#include <iostream> 
#include <vector> 
#include <set> 
#include <string> 
#include <map> 
#include <iostream>
#include <math.h>
using namespace std;

int lut[9][9] = { 	{0, 0, 0, 0, 0, 0, 0, 0, 0},
					{0, 1, 2, 3, 4, 5, 6, 7, 8},
					{0, 2, 5, 4, 7, 6, 1, 8, 3},
					{0, 3, 8, 5, 2, 7, 4, 1, 6},
					{0, 4, 3, 6, 5, 8, 7, 2, 1},
					{0, 5, 6, 7, 8, 1, 2, 3, 4},
					{0, 6, 1, 8, 3, 2, 5, 4, 7},
					{0, 7, 4, 1, 6, 3, 8, 5, 2},
					{0, 8, 7, 2, 1, 4, 3, 6, 5}};

// Character to index
// Only for possible inputs
int c2idx(char c) 
{ 
	switch (c) {
	case 'i':
		return 2;
		break;
	case 'j':
		return 3;
		break;
	case 'k':
		return 4;
		break;
	default:
		// Not supposed to happen
		// for this case
		return 0;	
	}
}

// Correct combination lut
int goodThird(int fir, int sec)
{
	if (fir == 2 && sec == 3) {
		return 4;
	}
	else if (fir == 2 && sec == 7) {
		return 8;
	}
	else if (fir == 6 && sec == 3) {
		return 8;
	}
	else if (fir == 6 && sec == 7) {
		return 4;
	}
	else {
		// Error
		return 0;
	}
}


int main()
{
	// Number of entries in data file
	int numEntries = 0;

	// Potential inputs
	int lenSequence;
	int multiplier;

	char quatSeq[100010];


	// Potential program skeleton
	scanf("%d\n", &numEntries);
	for(int i = 0; i < numEntries; i++) {
		bool printYes = false;
		scanf("%d ", &lenSequence);
		scanf("%d\n", &multiplier);
		scanf("%[ijk]\n", &quatSeq);

		string strQuatSeq = quatSeq;
		string strFullQuatSeq;

		for (int j = 0; j < multiplier; j++) {
			strFullQuatSeq.append(strQuatSeq);
		}

		int res;
		int index = 0;
		int found = 0;

		int first = 0;
		int second = 0;

		res = c2idx(strFullQuatSeq[0]);
		for (int j = 1; j < strFullQuatSeq.size(); j++) {
			if (found == 0 && (res == 2 || res == 6)) {
				first = res;	// Now look for j or -j
				found++;
				res = 1;
			}
			else if (found == 1 && (res == 3 || res == 7)) {
				second = res;	
				found++;
				res = 1;	
			}
			res = lut[res][c2idx(strFullQuatSeq[j])];
		}
		if (res == goodThird(first,second)) {
			printYes = true;
		}

		// Output
		printf("Case #%d:", i+1);	// Important! Verify
		if (printYes) {
			cout << " YES" << endl;
		}
		else {
			cout << " NO" << endl;
		}
	}

	return 0;
}
