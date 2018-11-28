/*
 *  DeceitfulWar.cpp
 *  
 *
 *  Created by sean brown on 14-04-12.
 *  Copyright 2014 __MyCompanyName__. All rights reserved.
 *
 */

#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int tests, numOfBlocks;
int naomiWarScore, naomiDeceitfulWarScore;
int naomiBlockPlace, kenBlockPlace;
vector<float> naomiBlocks, kenBlocks, tempNaomiBlocks, tempKenBlocks;

void printVector(vector<float> array) {
	printf("<");
	for (int i = 0; i < array.size(); i++) {
		printf("%.3f ", array[i]);
	}
	printf(">\n");
}

// assumes a is less than b
float getValueBetween(float a, float b) {
	return a + ((b - a)/2);
}

int pickBestBlock() {
	if (tempNaomiBlocks[tempNaomiBlocks.size() - 1] > tempKenBlocks[tempKenBlocks.size() - 1]) {
		return tempNaomiBlocks.size() - 1;
	}
	else {
		return 0;
	}

}

// gets value between ken's two biggest blocks
float getBestFakeBlock() {
	return getValueBetween(tempKenBlocks[tempKenBlocks.size() - 2], tempKenBlocks[tempKenBlocks.size() - 1]);
}

// returns place of best block
int kenReact(float weight) {
	float bestBlock = 0.0f;
	int i = tempKenBlocks.size() - 1;
	while(tempKenBlocks[i] > weight) {
		printf("Best choice so far is %.2f.\n", tempKenBlocks[i]);
		bestBlock = i;
		if (i == 0) {
			break;
		}
		i -= 1;
	}
	
	if (bestBlock == 0.0f) {
		return 0;
	}
	else {
		return bestBlock;
	}

}

int main() {
	
	float blockInput;
	float naomiChosenBlock, kenChosenBlock;
	FILE* input;
	FILE* output;
	const char* inFile = "D-large.in";
	const char* outFile = "D-large.out";
	
	input = fopen(inFile, "r");
	output = fopen(outFile, "w");
	
	fscanf(input, "%d", &tests);
	for (int test = 0; test < tests; test++) {
		naomiWarScore = 0.0;
		naomiDeceitfulWarScore = 0.0;
		fscanf(input, "%d", &numOfBlocks);
		printf("This game features %d blocks each!\n", numOfBlocks);
		naomiBlocks = vector<float>();
		kenBlocks = vector<float>();
		
		for (int i = 0; i < numOfBlocks; i++) {
			fscanf(input, "%f", &blockInput);
			printf("Added %.2f to Naomi!\n", blockInput);
			naomiBlocks.push_back(blockInput);
		}
		sort(naomiBlocks.begin(), naomiBlocks.end());

		for (int i = 0; i < numOfBlocks; i++) {
			fscanf(input, "%f", &blockInput);
			printf("Added %.2f to Ken!\n", blockInput);
			kenBlocks.push_back(blockInput);
		}
		sort(kenBlocks.begin(), kenBlocks.end());

		
		// Play war
		tempNaomiBlocks = vector<float>(naomiBlocks);
		tempKenBlocks = vector<float>(kenBlocks);
		printVector(tempNaomiBlocks);
		printVector(tempKenBlocks);
		printf("Starting war!\nNaomi has %d blocks!\nKen has %d blocks!\n", (int)tempNaomiBlocks.size(), (int)tempKenBlocks.size());
		while (tempNaomiBlocks.size() > 0 && tempKenBlocks.size() > 0) {
			naomiChosenBlock = tempNaomiBlocks[tempNaomiBlocks.size()-1];
			naomiBlockPlace = tempNaomiBlocks.size() - 1;
			printf("Naomi chose her %dth block.\n", naomiBlockPlace+1);
			
			kenBlockPlace = kenReact(naomiChosenBlock);
			printf("Ken chose his %dth block.\n", kenBlockPlace+1);
			kenChosenBlock = tempKenBlocks[kenBlockPlace];
			
			if (kenChosenBlock < naomiChosenBlock) {
				printf("War:\n%.5f < %.5f\n", kenChosenBlock, naomiChosenBlock);
				naomiWarScore += 1;
			}

			tempNaomiBlocks.erase(tempNaomiBlocks.begin() + naomiBlockPlace);
			tempKenBlocks.erase(tempKenBlocks.begin() + kenBlockPlace);

		}
		
		// Play deceitful war
		float naomiFalseBlock = 0.0f;
		tempNaomiBlocks = vector<float>(naomiBlocks);
		tempKenBlocks = vector<float>(kenBlocks);
		printVector(tempNaomiBlocks);
		printVector(tempKenBlocks);
		printf("Starting deceitful war!\nNaomi has %d blocks!\nKen has %d blocks!\n", (int)tempNaomiBlocks.size(), (int)tempKenBlocks.size());
		while (tempNaomiBlocks.size() > 0 && tempKenBlocks.size() > 0) {
			naomiBlockPlace = pickBestBlock() ;
			naomiFalseBlock = getBestFakeBlock();
			naomiChosenBlock = tempNaomiBlocks[naomiBlockPlace];
			printf("Naomi chose her %dth block.\n", naomiBlockPlace+1);
			
			kenBlockPlace = kenReact(naomiFalseBlock);
			printf("Ken chose his %dth block.\n", kenBlockPlace+1);
			kenChosenBlock = tempKenBlocks[kenBlockPlace];
			
			if (kenChosenBlock < naomiChosenBlock) {
				printf("Deceitful War:\n%.5f < %.5f\n", kenChosenBlock, naomiChosenBlock);
				naomiDeceitfulWarScore += 1;
			}
			
			tempNaomiBlocks.erase(tempNaomiBlocks.begin() + naomiBlockPlace);
			tempKenBlocks.erase(tempKenBlocks.begin() + kenBlockPlace);
			
		}
		
		fprintf(output, "Case #%d: %d %d\n", test + 1, naomiDeceitfulWarScore, naomiWarScore);
		
	}
	
	fclose(input);
	fclose(output);
	
}