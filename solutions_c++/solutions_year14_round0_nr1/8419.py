
#include <stdio.h>
#include <vector>
using namespace std;

void matchTable(int matches[4], int row) {
	int a;;
	for(int i=0; i<4; i++) {
		for(int j=0; j<4; j++) {
			if(i+1 == row) {
				scanf("%d", &matches[j]);
			}
			else scanf("%d", &a);
		}
	}
}

void testCase() {
	int firstRow;
	int secondRow;

	int firstMatch[4];
	int secondMatch[4];

	scanf("%d", &firstRow);
	matchTable(firstMatch, firstRow);
	scanf("%d", &secondRow);
	matchTable(secondMatch, secondRow);
	
	vector<int> matches;
	for(int i=0; i<4; i++) {
		for(int j=0; j<4; j++) {
			if(firstMatch[i] == secondMatch[j]) {
				matches.push_back(firstMatch[i]);
			}
		}
	}
	if(matches.size() == 1) {
		printf("%d\n", matches[0]);
	}
	else if(matches.size() == 0) {
		printf("Volunteer cheated!\n");
	}
	else {
		printf("Bad magician!\n");
	}
}

int main()
{
	int testCases;
	scanf("%d", &testCases);

	for(int i=0; i<testCases; i++) {
		printf("Case #%d: ", i+1);
		testCase();
	}
	return 0;
}

