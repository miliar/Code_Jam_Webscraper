#include <stdio.h>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int solve(string order)
{
	int n = 0;
	for( uint i = 0; i < order.size() - 1; i++ ) {
		if( order[i] != order[i+1] ) {
			n++;
		}
	}
	if( order[order.size()-1] == '-' ) {
		n++;
	}

	return n;
}

int main(int argc, char *argv[]) {

    int T;

    ifstream ifs(argv[1]);
    ofstream ofs(argv[2]);

    string line;
    std::getline(ifs, line);
    T = stoi(line);

    for( int i = 1; i <= T; i++ ) {
    	std::getline(ifs, line);
    	ofs << "Case #" << i << ": " << solve(line) << endl;
    }

    return 0;
}





