#include <iostream>

#define DEBUG_ON

#ifdef DEBUG_ON
#	define DEBUG(x) do { std::cerr << x; } while (0)
#else
#	define DEBUG(x) do {} while (0)
#endif


using namespace std;

// Input variables
unsigned int numTestCases;
unsigned int currTestCase;
unsigned int choice1;
unsigned int choice2;
unsigned int arrange1[4][4]; 
unsigned int arrange2[4][4];
									
// Internal variables
unsigned int candidates[4];
unsigned int countCandidates;
unsigned int candidate;

int main()
{
	DEBUG("Problem A: Magic Trick" << endl);
	currTestCase = 0;

	// Read the file
	// We will use file redirection in the command line
	// Parse the strings into choice# and arrange#
	scanf("%u\n", &numTestCases);
	DEBUG("Number of test cases: " << numTestCases << endl);
	
	// Iterate over all test cases
	for (unsigned int k = 1; k <= numTestCases; k++) {

		currTestCase++;

		// Reset variables
		countCandidates = 0;
		candidate = 0;

		scanf("%u\n", &choice1);
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf("%u ", &arrange1[i][j]);
			}
			scanf("\n");
		}
		scanf("%u\n", &choice2);
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf("%u ", &arrange2[i][j]);
			}
			scanf("\n");
		}

		DEBUG("Arrangement 1 is:" << endl);
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				DEBUG(arrange1[i][j] << "\t");
			}
			DEBUG(endl);
		}
		DEBUG("Choice 1 is: " << choice1 << endl);

		// Put the candidates into the candidates variable
		for (int i = 0; i < 4; i++) {
			candidates[i] = arrange1[choice1 - 1][i];
		}

		DEBUG("Candidates are:" << endl);
		for (int i = 0; i < 4; i++) {
			DEBUG("\t" << candidates[i]);
		}
		DEBUG(endl);

		DEBUG("Arrangement 2 is:" << endl);
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				DEBUG(arrange2[i][j] << "\t");
			}
			DEBUG(endl);
		}
		DEBUG("Choice 2 is: " << choice2 << endl);
		
		// Check if the candidates are in the new line chosen
		// if not replace them with a 0
		bool wasFound;
		for (int i = 0; i < 4; i++) {
			// For each candidate check if they are in the new chosen line
			wasFound = false;
			for (int j = 0; j < 4; j++) {
				if (candidates[i] == arrange2[choice2 - 1][j]) {
					// This one is a new candidate
					wasFound = true;
					break;
				}
			}
			// If it was not in the newly chosen row, mark with 0
			if (!wasFound) {
				candidates[i] = 0;
			}
		}

		DEBUG("Updated Candidates are:" << endl);
		for (int i = 0; i < 4; i++) {
			DEBUG("\t" << candidates[i]);
		}
		DEBUG(endl);
				
		
		// If the candidate array is all 0 return case 3
		// If the cadidate has a single number that is non zero return case 1
		// if the candidates have more than 1 non-zero number return case 2
		for (int i = 0; i < 4; i++) {
			if (candidates[i] == 0) {
				continue;
			}
			else {
				candidate = candidates[i];
				countCandidates++;
			}
		}

		if (countCandidates == 1) {
			// Case 1, output the candidate
			cout << "Case #" << currTestCase << ": " << candidate << endl;
		}
		else if (countCandidates == 0) {
			// Case 3, 
			cout << "Case #" << currTestCase << ": Volunteer cheated!" << endl;
		}
		else {
			// Case 2, 
			cout << "Case #" << currTestCase << ": Bad magician!" << endl;
		}
	}		

	return 0;
}

