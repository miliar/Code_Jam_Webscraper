#include "QB.h"

int CQBTaskProcessor::findMinimalTime( int initialNumberOfDiners, const std::vector<int>& pancakesVsDinersUnordered )
{
	assert( pancakesVsDinersUnordered.size() == initialNumberOfDiners );

	//	ascending order
	std::vector<int> pancakesVsDiners;
	pancakesVsDiners.assign( pancakesVsDinersUnordered.begin(), pancakesVsDinersUnordered.end() );
	std::sort( pancakesVsDiners.begin(), pancakesVsDiners.end() );


	std::vector< std::vector<int> > s;	//	min time for i-th diner with k-divisions, divisions not counted
	s.assign( initialNumberOfDiners, std::vector<int>() );
	for( int i = 0; i < initialNumberOfDiners; i++ ) {
		std::vector<int>& times = s[i];
		const int numberOfPancakes = pancakesVsDiners[i];
		for( int numebrOfDivisions = 0; numebrOfDivisions < pancakesVsDiners[i]; numebrOfDivisions++ ) {
			const int numberOfParts = numebrOfDivisions + 1;
			const int largestPart = ( numberOfPancakes + numberOfParts - 1 ) / numberOfParts; //	ceil
			const int time = largestPart;
			times.push_back( time );
		}
	}

	//	dynamic programming
	std::vector<int> tPrev;	//	tPrev, tCrnt - min time with diners [0...i] and k divisions, divisions are counted
	std::vector<int> tCrnt;

	int maxNumberOfDivision = 0;
	for( int i = 0; i < initialNumberOfDiners; i++ ) {
		maxNumberOfDivision += pancakesVsDiners[i] - 1;
	}

	int currentMaxNumberOfDivisions = pancakesVsDiners[0] - 1;
	tPrev.assign( maxNumberOfDivision + 1, INT_MAX );
	for( int k = 0; k <= currentMaxNumberOfDivisions; k++ ) {
		tPrev[k] = k + s[0][k];
	}

	for( int numberOfDiners = 2; numberOfDiners <= initialNumberOfDiners; numberOfDiners++ ) {
		tCrnt.assign( maxNumberOfDivision + 1, INT_MAX );
		currentMaxNumberOfDivisions += pancakesVsDiners[numberOfDiners - 1] - 1;
		for( int k = 0; k <= currentMaxNumberOfDivisions; k++ ) {
			for( int j = 0; j <= min( k, pancakesVsDiners[numberOfDiners - 1] - 1 ); j++ ) {
				tCrnt[k] = min( tCrnt[k], max( j + tPrev[k - j], s[numberOfDiners - 1][j] + k ) );
			}
		}
		tPrev.assign( tCrnt.begin(), tCrnt.end() );
	}
	int smallestTime = INT_MAX;
	for( int k = 0; k < (int)tPrev.size(); k++ ) {
		smallestTime = min( smallestTime, tPrev[k] );
	}
	assert( smallestTime < INT_MAX );
	return smallestTime;
}

///////////////////////////////////
