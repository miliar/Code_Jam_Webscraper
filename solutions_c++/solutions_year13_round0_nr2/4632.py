#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>

using namespace std;

int main(int argc, char ** argv){

    int ** lawnMap;

    int numberOfTest;
    int rowSize;
    int columeSize;

    int count, count2, count3, count4;
    int temp;

    bool rowStatus;
    bool columeStatus;
    bool wholeStatus;

    ifstream inFile;
    ofstream outFile;

    inFile.open(argv[1]);
    outFile.open(argv[2]);

    inFile >> numberOfTest;

    for(count = 0 ; numberOfTest > count ; count++){
	inFile >> rowSize;
	inFile >> columeSize;

	lawnMap	= new int*[rowSize];
	
	for(count2 = 0 ; rowSize > count2 ; count2++){
	    lawnMap[count2] = new int[columeSize];
	    for(count3 = 0 ; columeSize > count3 ; count3++){
		inFile >> lawnMap[count2][count3];
	    }
	}

	wholeStatus = true;
	for(count2 = 0 ; (rowSize > count2) && wholeStatus; count2++){
	    for(count3 = 0 ; columeSize > count3 ; count3++){
		rowStatus   = false;
		columeStatus	= false;
		temp	= lawnMap[count2][count3];
		for(count4 = 0 ; columeSize > count4 ; count4++){
		    if(temp < lawnMap[count2][count4]){
			rowStatus   = true;
			break;
		    }
		}
		for(count4 = 0 ; rowSize > count4 ; count4++){
		    if(temp < lawnMap[count4][count3]){
			columeStatus = true;
			break;
		    }
		}

		if(rowStatus && columeStatus){
		    wholeStatus = false;
		    break;
		}
	    }
	}
	outFile << "Case #" << count + 1 << ": ";

	if(wholeStatus)
	    outFile << "YES" << endl;
	else
	    outFile << "NO" << endl;
    }
    return EXIT_SUCCESS;
}
