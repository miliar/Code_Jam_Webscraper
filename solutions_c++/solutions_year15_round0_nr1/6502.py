#include <fstream>
#include <iostream>
using namespace std;

int main(int argc, char* argv[]){

	string filename = argv[1];
	ifstream istr(filename.c_str());

	ofstream ostr(argv[2]);

	int test_cases,smax;
	string audience;

	istr >> test_cases;

	for (int i=0;i<test_cases;i++){

		istr >> smax >> audience;

		int friends = 0;
		unsigned int members = 0;
		unsigned int section = 0;

		for (unsigned int j=0;j<audience.size();j++){

			section = audience[j] - 48;

			if (section != 0){
				members += section;
			}
			else{
				if (members < j+1){
					friends += 1;
					members += 1;
				}
			}

		}

		ostr << "Case #" << i+1 << ": " << friends << endl;

	}

}