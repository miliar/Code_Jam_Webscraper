#include <iostream>
#include <string>

/*
 * smax = 0 -> n = 0
 * smax>0 -> n = numzeros - numnonzeros before the zeros are reached, do 
 * 							iteratively till you reach the end and there
 * 							are no more zeros
 * Go to position of each zero. If the number of people before that zero
 * are >= shyness level  * at that zero, go on, else increment number of
 * people to add.
 */

int main(){
	int test, sMax, numFriends, cmpPeople, numAtJ;
	std::string numPeople;
	
	std::cin >> test;
	for(int i=0; i<test; ++i){
		numFriends = 0;
		cmpPeople = 0;
		std::cin >> sMax >> numPeople;
		if(sMax != 0){
			for(int j=0; j<numPeople.size(); ++j){
				numAtJ = (int)(numPeople[j] - '0');
				if(numAtJ == 0 && (j+1) > cmpPeople){
					++numFriends;
					++cmpPeople;
				}
				cmpPeople += numAtJ;
			}
		}
		std::cout << "Case #" << i+1 << ": " << numFriends << "\n";
	}

	return 0;
}
