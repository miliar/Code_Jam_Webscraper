#include<bits/stdc++.h>

using namespace std;

int main() {
	/* Variables used in the program */
	int numberOfPeopleToAdd, numberOfPeopleSoFar, 
	    s, sMax, t, tempNumberOfPeopleToAdd, testCases, 
	    totalNumberOfPeople, u;
	
	char numberOfPeople;
	
	vector<int> shynessVector;
	
	/* Read in the test cases */
	scanf("%d\n", &testCases);
	
	/* Process the test cases */
	for(t = 0; t < testCases; t++) {
		
		/* Reset the variables */
		shynessVector.clear(); totalNumberOfPeople = 0; 
		numberOfPeopleToAdd = 0; numberOfPeopleSoFar = 0;
		tempNumberOfPeopleToAdd = 0;	
		
		/* Read in SMax */
		scanf("%d\n", &sMax);	
		
		/* Increase it by 1 */
		sMax++;
		
		/* 
		   Store the shyness indices of the audience and calculate 
		   the total 
		*/
		for(s = 0; s < sMax; s++) {
			/* Read in as a character and convert to integer */
			scanf("%c\n", &numberOfPeople);
			shynessVector.push_back(numberOfPeople - '0');
			totalNumberOfPeople += (numberOfPeople - '0');	
		}
		
		/* Process the number of people */
		for(s = 0; s < sMax; s++) {
			/* Check if the number of people so far is equal to the (changing) total number of people */
			numberOfPeopleSoFar = numberOfPeopleSoFar + tempNumberOfPeopleToAdd + shynessVector[s];
			
			/* If the number of people so far equals the total number of people, exit */
			if(numberOfPeopleSoFar >= totalNumberOfPeople) {
				break;
			}
			
			tempNumberOfPeopleToAdd = 0;
			
			/* If this is a zero */
			if(shynessVector[s] == 0) {
				/* Skip to the first non-zero number */
				u = s + 1;
				
				while(shynessVector[u] == 0) {
					u++;
				}
				/* If the number of people so far is less, add the necessary people */	
				if(numberOfPeopleSoFar < u) {
					tempNumberOfPeopleToAdd = u - numberOfPeopleSoFar;
				}
			} 
			/* Keep track of the total number of people to add */
			numberOfPeopleToAdd += tempNumberOfPeopleToAdd;
			
			/* Keep track of the changing total */
			totalNumberOfPeople += tempNumberOfPeopleToAdd;
		}
		printf("Case #%d: %d\n", (t + 1), numberOfPeopleToAdd);
	}



	return 0;
}
