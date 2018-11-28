#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char*argv[]){

	fstream fcin(argv[1], fstream::in);
	fstream fcout(argv[2], fstream::out);


	int totalCase;
	fcin >> totalCase;
	
	for(int caseIdx=1; caseIdx <= totalCase; caseIdx++){
		int maxShyness;
		fcin >> maxShyness;
		string histogramShyness;
		fcin >> histogramShyness;
		cout << "max shyness: "<< maxShyness << " string histogram: "<< histogramShyness<<endl;
		int accumPerson = 0;
		int neededPerson = 0;

		for(int shy_level = 0; shy_level <= maxShyness; shy_level++){
			if( accumPerson < shy_level ){
				neededPerson += shy_level - accumPerson;
				accumPerson = shy_level;
			}
			accumPerson += (histogramShyness[ shy_level ] - 48);
		}

		fcout << "Case #" << caseIdx << ": "<<neededPerson<<endl;

	}


	return 0;
}
