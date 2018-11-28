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


int charToInt(char input) 
{
	switch(input) {
	case '0':
		return 0;
	case '1':
		return 1;
	case '2':
		return 2;
	case '3':
		return 3;
	case '4':
		return 4;
	case '5':
		return 5;
	case '6':
		return 6;
	case '7':
		return 7;
	case '8':
		return 8;
	case '9':
		return 9;
	default:
		return -1;
	}
}

int main()
{
	// Number of entries in data file
	// Max is 100
	int numEntries = 0;

	// Potential inputs
	int maxShyness;		// At most 1000
	char sI[1010];		// NEed to assign scanf to char

	// Outputs go here
	long numFriends;


	// Might have to use long
	// Internal vars
	long numAudiencePeople;


	// Potential program skeleton
	scanf("%d\n", &numEntries);
	// Max entries is 100
	for(int i = 0; i < numEntries; i++) {

		// INIT
		numAudiencePeople = 0;
		numFriends = 0;

		//// Potential parsing
		//getline(std::cin, lines[i]);
		scanf("%d ", &maxShyness);	

		// INPUT
		//scanf("%[0-9]\n", &sI); 
		scanf("%[0-9]\n", &sI); 
		string audience = sI;

		// TRIVIAL
		if (audience.size() == 1) {
			// Do nothing
		}
		// NONTRIVIAL
		else {
			//numFriends = 42;
			numAudiencePeople += charToInt(audience[0]);
			for (int i = 1; i < audience.size(); i++) {
				// Check if this is enough for this level:
				//int numRequired = charToInt(audience[i]);
				int numRequired; //= i;

				if (audience[i] == '0') {
					numRequired = 0;
				}
				else {
					numRequired = i;
				}


				if (numRequired > numAudiencePeople) {
					numFriends += numRequired - numAudiencePeople;
					numAudiencePeople += numFriends;
				}
				//cout << "\n numAud: " << numAudiencePeople << "  \n";
				//cout << "\n numReq: " << numRequired << "  \n";
				//cout << "\n numFri: " << numFriends << "  \n";
				numAudiencePeople += charToInt(audience[i]);
			}
		}
		//cout << " numAud: " << numAudiencePeople << "  ";

		// Output
		printf("Case #%d:", i+1);	// Important! Verify

		//First output the input
		//printf(" %d ", maxShyness);	
		//printf("%s ", sI);	
		//cout << audience << " " ;
		printf(" %d", numFriends);	
		printf("\n");
	}

	return 0;
}

