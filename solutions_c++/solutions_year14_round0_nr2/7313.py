#include <iostream>
#include <sstream>
#include <fstream>

using namespace std;

typedef unsigned int uint;

int main(int argc, char * argv[]) {
    if (argc < 2) {
        return 0;
    }

    ifstream fileInput(argv[1]);

    string name = argv[1]; name = name.substr(0, name.length() - 3); name.append(".out");
    ofstream fileOutput(name);

    if (!fileInput.is_open() || !fileOutput.is_open()) { return 2; }

    fileOutput.clear();
    fileOutput.precision(7);
    fileOutput.setf(ios::fixed, ios::floatfield);

    string line;
    uint cases = 0;
    getline(fileInput, line); stringstream(line) >> cases;

    double farmCost = 0;
    double farmRate = 0;
    double cookieTarg = 0;
    double cookieRate = 2;

    double totalTime = 0;
    double waitTime = 0;
    double buyTime = 0;

    for (uint i = 0; i < cases; ++i) {
        fileInput >> farmCost >> farmRate >> cookieTarg;

        cookieRate = 2;
        totalTime = 0;

        while (true) {
            waitTime = (cookieTarg / cookieRate);
            buyTime = (farmCost / cookieRate) + (cookieTarg / (cookieRate + farmRate));

            if (buyTime < waitTime) {
                totalTime += (farmCost / cookieRate);
                cookieRate += farmRate;
            } else {
                totalTime += waitTime;
                break;
            }
        }

        fileOutput << "Case #" << (i + 1) << ": " << totalTime << endl;
    }

    return 1;
}