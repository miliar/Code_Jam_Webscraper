#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <fstream>
#include <stdio.h>
using namespace std;

int main()
{
	int testcases;
	FILE *pFile = fopen("A-large.in", "r");
	FILE *outFile = fopen("a-large.out", "w");
	fscanf(pFile, "%d", &testcases);
	printf("%d\n", testcases);
	for (int tc=1; tc<=testcases; tc++) {
		char str[1010];
		int maxScore;
		fscanf(pFile, "%d%s", &maxScore, str);
		fprintf(outFile, "Case #%d: ", tc);
		int alreadyStood = 0;
		int peopleNeeded = 0;
		//cout << "_____________" << endl;
		for (int i=0; i<=maxScore; i++) {
			int people = str[i] - '0';
			//cout<< "i: " << i << endl;
			if (people == 0) continue;
			if (alreadyStood >= i) {
				alreadyStood += people;
				//cout << "alreadyStood: " << alreadyStood << " i: " << i << endl; 
			} else {
				int missedPeople = i - alreadyStood;
				peopleNeeded += missedPeople;
				alreadyStood += missedPeople + people;
				//cout << "alreadyStood: " << alreadyStood << " peopleNeeded: " << peopleNeeded << endl;
			}
		}
		printf("%d\n", peopleNeeded);
		fprintf(outFile, "%d\n", peopleNeeded);
	}

	return 0;
}