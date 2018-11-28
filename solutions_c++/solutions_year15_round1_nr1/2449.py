// DONE
// clang++ -o A template.cpp -I./

#include <stdio.h> 
#include <algorithm> 
#include <cstdlib> 
#include <iostream> 
#include <vector> 
#include <set> 
#include <string> 
#include <map> 

using namespace std;

typedef long long				ll;
typedef std::pair<int, int>		ii;
typedef std::vector<ii>			vii;
typedef std::vector<int>		vi;
typedef std::set<int>			si;
typedef std::map<string,int>	msi;

#define INF				1000000000

int main()
{
	// Number of entries in data file
	// Max is 100
	int numEntries = 0;

	// Potential inputs
	vi mushTimes;

	// Outputs go here
	int sol1, sol2;


	int numMoments;
	// Potential program skeleton
	scanf("%d\n", &numEntries);
	// Max entries is 100
	for(int i = 0; i < numEntries; i++) {
		// INIT
		mushTimes.clear();
		// INPUT
		scanf("%d\n", &numMoments);	
		for (int j = 0; j < numMoments; j++) {
			int curr;
			scanf("%d ", &curr);	
			mushTimes.push_back(curr);	
		}


		// SOLUTION 1
		// if the next is smaller assume she ate them 
		// if it's the same nothing happens
		// if it's larger, bart added more and she ate nothing 
		int prevMush = mushTimes[0];
		sol1 = 0;
		for (int j = 1; j < numMoments; j++) {
			if (prevMush > mushTimes[j]){
				sol1 += prevMush - mushTimes[j];
			}

			prevMush = mushTimes[j];
		}


		// SOLUTION 2
		sol2 = 0;
		// Get rate
		int minRate = 0;
		// If this never gets set, then she never eats anything
		for (int j = 1; j < numMoments; j++) {
			if (mushTimes[j] < mushTimes[j-1] &&
					minRate < mushTimes[j-1] - mushTimes[j]){
				minRate =  - mushTimes[j] + mushTimes[j-1];
			}
		}

		if (minRate == 0) { 
			sol2 = 0;
		}
		else {
			for (int j = 1; j < numMoments; j++) {
				if (mushTimes[j-1] == 0) {
					// NOP
				}
				else
				if (mushTimes[j-1] < minRate) {
					sol2 += mushTimes[j-1];
					// NOP
				}
				else {
					sol2 += minRate;
				}
			}
		}

			//cout << minRate << endl;


		// Output
		printf("Case #%d:", i+1);	// Important! Verify

		//First output the input
		//printf(" %d ", maxShyness);	
		//printf("%s ", sI);	
		//cout << audience << " " ;
		printf(" %d", sol1);	
		printf(" %d", sol2);	
		printf("\n");
	}

	return 0;
}

