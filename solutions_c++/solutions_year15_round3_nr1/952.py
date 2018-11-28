#include <vector>
#include <algorithm>
#include <set>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>

#include <cstdlib>

using namespace std;

class Battleship {
public:

	int Compute(int r, int c, int w) {


		
		/*int ch = max(c-(w-1)*3, 1);
		if (c == w) return r + w - 1;
		if (w == 1) return r*c;
		
		if(r == 1) return ch*r + w;
		return ch*r + w + 1;*/
		int firstHit = floor(1.0*c / w)*r;
		//if (c - w <= 1 || w==1) return firstHit + w - 1;
		if (c%w!=0) firstHit++;
		return firstHit + w - 1;
	}
};

int main(int argc, char *argv[]) {

ifstream inFile("C:\\Users\\Mike\\Downloads\\A-large.in");
ofstream outFile("C:\\Users\\Mike\\Downloads\\A-large.out");
string line;
getline(inFile, line);
int cases;
istringstream(line) >> cases;
Battleship proc;
for (int n = 0; n < cases; n++){
string nums;
int R, C, W;
getline(inFile, nums);
istringstream iss(nums);
iss >> R >> C >> W;

int ret = proc.Compute(R, C, W);
outFile << "Case #" << (n + 1) << ": " << ret << "\n";
}
return 0;
}

