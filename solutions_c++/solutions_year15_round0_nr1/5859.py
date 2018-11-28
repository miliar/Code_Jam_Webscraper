#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char ** argv){
    int nTest;

    int sMax;

    vector <int> s;
    vector <int> c;

    char temp;
    int result;

    ifstream inFile;
    ofstream outFile;

    inFile.open(argv[1]);
    outFile.open(argv[2]);

    inFile >> nTest;

    for(int count = 0 ; nTest > count ; count++){
	result = 0;

	s.clear();
	c.clear();

	inFile >> sMax;

	for(int idx = 0 ; sMax >= idx ; idx++){
	    inFile >> temp;
	    s.push_back(static_cast<int>(temp-48));
	}

	c.push_back(0);

	for(int idx = 0 ; sMax > idx ; idx++){
	    c.push_back(c[idx] + s[idx]);

	}

	for(int idx = sMax ; 0 < idx ; idx--){
	    if(idx > (c[idx]+result)){
		result += (idx - (c[idx] + result));
	    }else if(result > idx){
		break;
	    }

	}

	outFile << "Case #" << count+1 << ": "<< result<< endl;
    }
    inFile.close();
    outFile.close();

    return 0;
}
