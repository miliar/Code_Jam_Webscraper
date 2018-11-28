#include <iostream>
#include <fstream>
using namespace std;

int friendsNeeded(string audience, int maxShyness) {
    int numStanding = 0;
    int numNeeded = 0;
    for (int i = 0; i <= maxShyness; ++i) {
        int numShy = audience[i] - '0';
        if (numStanding + numNeeded < i && numShy > 0) {
            numNeeded += (i - (numStanding + numNeeded));
        }
        numStanding += numShy;
    }
    return numNeeded;
}

int main() {
    int numTests = 0;
    ifstream smallFile("A-large.in");
    ofstream outputFile("output.out");
    if (smallFile.is_open()) {
        smallFile>>numTests;
    }
    for (int test = 1; test <= numTests; test++) {
        int maxShyness;
        smallFile>>maxShyness;
        string audience;
        smallFile>>audience;
        outputFile<<"Case #"<<test<<": "<<friendsNeeded(audience, maxShyness)<<endl;
    }
    outputFile.close();
    return 0;
}