#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>
#include <string.h>

using namespace std;

int main(int argc, char* argv[]) {
	ifstream input(argv[1]);
    size_t T, lineNum, cc=0;
	string line;
	
	if(input >> T) {
		while(cc++ < T) {
			size_t exists[17] = {}, hits=0, temp, save=0;
			
			input >> lineNum;
			getline(input, line);
			for(size_t i=1; i<5; i++) {
				getline(input, line);
				if(i == lineNum) {
					istringstream iss(line);
					while(iss >> temp)
						exists[temp] = 1;
				}
			}		

			input >> lineNum;
			getline(input, line);
			for(size_t i=1; i<5; i++) {
				getline(input, line);
				if(i == lineNum) {
					istringstream iss(line);
					while(iss >> temp) {
						if(exists[temp] == 1) {
							hits++;
							save = temp;
						}
					}
				}
			}

			cout << "Case #" << cc << ": ";
			if(hits == 0)
				cout << "Volunteer cheated!" << endl;
			else if(hits == 1)
				cout << save << endl;
			else 
				cout << "Bad magician!" << endl;
		}		
	}

	return 0;
}
