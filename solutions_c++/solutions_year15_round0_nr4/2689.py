#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char ** argv){
    int nCase;

    ifstream inFile;
    ofstream outFile;

    inFile.open(argv[1]);
    outFile.open(argv[2]);

    inFile >> nCase;

    for(int count = 1 ; nCase >= count ; count++){
	int result; 
	int X, R, C;
	int temp;

	inFile >> X;
	inFile >> R;
	inFile >> C;

	switch(X){
	    case 1 : 
		result = 0;
		break;
	    default :
		if(0 == ((R *C)%X)){
		    result = 0;
		}else{
		    result = 1;
		}
		break;
	}

	if((0 == result) && (2 < X)){
	    if(((R * C) <= X) ){
		result = 1;
	    }else{
		temp = X/2;
		if((temp >= R) || (temp >= C)){
		    result = 1;
		}
	    }
	}

	outFile << "Case #" << count << ": ";

	switch(result){
	    case 0 :
		outFile << "GABRIEL" << endl;
		break;
	    case 1 :
		outFile << "RICHARD" << endl;
	}
    }

    inFile.close();
    outFile.close();

    return 0;
}
