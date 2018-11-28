//clang++ -o D template.cpp -I./

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

// This might be DP problem

// We can use brute force for the small dataset

//Limits
//1 ≤ T ≤ 100.
//Small dataset
//1 ≤ D ≤ 6.
//1 ≤ Pi ≤ 9.

// At most 6*9 = 54 pancakes
// Worst case, 53 minutes to place in plates, 1 to eat them all

// Naively I think halving the pancakes of the largest would be best
// but there's a limit at which there's diminishing returns

// Externally generated for speed
int lut[4][4][4] ={{{1,1,1,1},
					{1,1,1,1},
					{1,1,1,1},
					{1,1,1,1}},{
					{0,1,0,1},
					{1,1,1,1},
					{0,1,0,1},
					{1,1,1,1}},{
					{0,0,0,0},
					{0,0,1,0},
					{0,1,1,1},
					{0,0,1,0}},{
					{0,0,0,0},
					{0,0,0,0},
					{0,0,0,1},
					{0,0,1,1}}};

int main()
{
	int numEntries = 0;

	// Potential inputs
	int N;
	int row;
	int col;

	// Potential program skeleton
	scanf("%d\n", &numEntries);
	for(int i = 0; i < numEntries; i++) {
		scanf("%d ", &N);
		scanf("%d ", &row);
		scanf("%d\n", &col);
		N--;
		row--;
		col--;

		if (lut[N][row][col] == 1) {
			printf("Case #%d:", i+1);	// Important! Verify
			cout << " GABRIEL" <<endl;
		}
		else {
			printf("Case #%d:", i+1);	// Important! Verify
			cout << " RICHARD" <<endl;
		}
	}

	return 0;
}

