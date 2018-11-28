#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char ** argv){
    ifstream inFile;
    ofstream outFile;

    inFile.open(argv[1]);
    outFile.open(argv[2]);

    int numberOfTest;

    int count;

    int count2;

    int temp;
    int limitTemp;

    long A;

    int numberOfMotes;

    int result;
    int limit;

    vector <int> N;
    vector <int> sortedN;

    inFile >> numberOfTest;

    for(count = 0 ; numberOfTest > count ; count++){
	N.clear();
	sortedN.clear();
	result = 0;

	inFile >> A;

	inFile >> numberOfMotes;

	for(count2 = 0 ; numberOfMotes > count2 ; count2++){
	    inFile >> temp;
	    N.push_back(temp);
	}

	if( 1 == A ){
	    outFile << "Case #" << count + 1 << ": " << numberOfMotes << endl;
	    continue;
	}


	sortedN	= N;
	sort(sortedN.begin(), sortedN.end());

	limit	= numberOfMotes -1;

	for(count2 = 0 ; numberOfMotes > count2 ; count2++){
	    if( sortedN[limit] < A)
		break;
	    if( sortedN[count2] >= A){
		limitTemp   = numberOfMotes - count2;
		temp = 0;
		while((sortedN[count2] >= A) && (limitTemp > temp)){
		    A	+= (A-1);
		    temp++;
		}

		result += temp;
		if(limitTemp == temp)
		    break;
	    }
	    A   += static_cast<long long>(sortedN[count2]);
	}

	outFile << "Case #" << count + 1 << ": " << result << endl;
    }

    inFile.close();
    outFile.close();

    return EXIT_SUCCESS;
}
