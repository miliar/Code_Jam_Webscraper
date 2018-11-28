#include <iostream>
#include <ios>
#include <fstream>
#include <string>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <set>

using namespace std;

int warWins(set<double> naomiBlocks, set<double> kenBlocks)
{
    int w = 0;
    bool kw = false;
    auto iter = naomiBlocks.begin();
    while(iter != naomiBlocks.end()) {
        kw = false;
        auto innerIter = kenBlocks.begin();
        for(; innerIter != kenBlocks.end(); ++innerIter) {
            if(*innerIter > *iter) {
                kw = true;
                kenBlocks.erase(innerIter);
                iter = naomiBlocks.erase(iter);
                break;
            }
        }

        if(!kw){
            ++w;
            auto it = kenBlocks.begin();
            kenBlocks.erase(*it);
            iter = naomiBlocks.erase(iter);
        }
    }
    return w;
}

int deceitfulWarWins(set<double> naomiBlocks, set<double> kenBlocks)
{
    int w = 0;
    bool nw = false;
    auto iter = naomiBlocks.begin();
    while(iter != naomiBlocks.end()) {
        nw = false;
        for(auto innerIter = kenBlocks.begin(); innerIter != kenBlocks.end(); ++innerIter) {
            if(*iter > *innerIter) {
                ++w;
                nw = true;
                kenBlocks.erase(*innerIter);
                iter = naomiBlocks.erase(iter);
                break;
            }
        }

        if(!nw) {
            auto it = kenBlocks.rbegin();
            kenBlocks.erase(*it);
            iter = naomiBlocks.erase(iter);
        }

    }
    return w;
}

int main(int argc, char *argv[])
{
	if (argc < 2) {
		cout << "Missing arguments!" << endl;
		return -1;
	}

	ifstream inputFile(argv[1]);
	string outputFileName = string(argv[1]) + ".out";
	ofstream outputFile(outputFileName.c_str(), ios::out | ios::trunc);
	if (!inputFile || !outputFile) {
		cout << "Open file error" << endl;
		return -2;
	}
    outputFile.precision(7);
    string line;
    getline(inputFile, line);
	int caseNum = atoi(line.c_str());
	int i = 0; 
	while (i < caseNum) {
        getline(inputFile, line);
        int n = atoi(line.c_str());
        getline(inputFile, line);
        stringstream ss;
        ss.str(line);
        set<double> naomiBlocks;
        for(int j = 0; j !=n; ++j) {
            double d;
            ss >> d;
            naomiBlocks.insert(d);
        }

        getline(inputFile, line);
        ss.clear();
        ss.str(line);
        set<double> kenBlocks;
        for(int j = 0; j !=n; ++j) {
            double d;
            ss >> d;
            kenBlocks.insert(d);
        }

        int w = warWins(naomiBlocks, kenBlocks);
        int dw = deceitfulWarWins(naomiBlocks, kenBlocks);
        outputFile << "Case #" << ++i << ": " << dw << " " << w << endl;
	}
	outputFile.flush();
	inputFile.close();
	outputFile.close();
	return 0;
}
