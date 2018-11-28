#include <stdio.h>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

string solve(int N)
{
	if ( N == 0 ) {
		return "INSOMNIA";
	}

	int flag = 0x3FF;
	unsigned long long currentN = N;
	unsigned long long nextN = 0;
	while( flag ) {
		nextN = currentN + N;
		while( currentN ) {
			flag &= ~(1 << (currentN % 10));
			currentN /= 10;
		}
		currentN = nextN;
	}

	stringstream ss;
	ss << currentN - N;
	return ss.str();
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
    	int N = stoi(line);
    	ofs << "Case #" << i << ": " << solve(N) << endl;
    }

    return 0;
}





