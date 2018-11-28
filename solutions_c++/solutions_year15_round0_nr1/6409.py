#include <vector>
#include <algorithm>
#include <set>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>

#include <cstdlib>

using namespace std;

class StandingOvation {
public:


	int getExtras(string counts) {
		int ret = 0;
		int tot = 0;
		for (int n = 0; n < counts.size(); n++){
			if (n <= tot){
				tot += (counts[n] - '0');
			}
			else
			{
				ret += n-tot;
				tot += n - tot + (counts[n] - '0');

			}
		}
		return ret;
	}
};

int main(int argc, char *argv[]) {
	ifstream inFile("C:\\Users\\Mike\\Downloads\\A-large.in");
	ofstream outFile("C:\\Users\\Mike\\Downloads\\A-large.out");
	string line;
	getline(inFile, line);
	int cases;
	istringstream(line) >> cases;
	StandingOvation proc;
	for (int n = 0; n < cases; n++){
		string c;
		getline(inFile, c);
		int level;
		string counts;
		istringstream iss(c);
		iss >> level >> counts;

		
		int ret = proc.getExtras(counts);
		outFile << "Case #" << (n + 1) << ": " << ret << "\n";
	}
	return 0;
}

