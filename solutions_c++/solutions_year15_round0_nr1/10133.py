#include <fstream>
#include <cstdio>
using namespace std;

int main(int argc, char** argv) {
    if (argc != 3)
        return 1;
    ifstream in(argv[1]);
    ofstream out(argv[2]); 
    int testCases;
    in >> testCases;
    
    for (int i = 0; i < testCases; ++i) {
        int sMax;
        in >> sMax;
        int numNeeded = 0;
        int numStanding = 0;
        for (int j = 0; j <= sMax; ++j) {
            char c;
            in >> c;
            int num;
            sscanf(&c, "%d", &num);
            if (numStanding + numNeeded < j) {
                numNeeded += j - numStanding - numNeeded;       
            }
            numStanding += num;
        }
        out << "Case #" << (i + 1) << ": " << numNeeded << endl;
    }

    return 0;
}
