//Problem A

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int trialResult(int smax, const string& trial){
    if (smax == 0) {
        return 0;
    }
    int numNeeded = 0;
    int currStanding = 0;
    int numPeeps = 0;
    for (int i = 0; i < trial.size(); ++i) {
        numPeeps = stoi(trial.substr(i, 1));
        //cout << "numPeeps when i=" << i << ": " << trial.substr(i, 1) << endl;
        if (numPeeps != 0 && currStanding < i) {
            numNeeded += i-currStanding;
            currStanding += numNeeded;
            //cout << "numNeeded updated when i=" << i << ": " << numNeeded << endl;
        }
        currStanding += numPeeps;
    }
    return numNeeded;
}

void small(ifstream& input){
    int numTrials;
    input >> numTrials;
    int smax;
    string trial;
    for (int i = 1; i <= numTrials; ++i) {
        input >> smax >> trial;
        cout << "Case #" << i << ": " << trialResult(smax, trial) << endl;
    }
}

int main() {
    
    /*ofstream outputFile("program3data.txt");
    outputFile << "writing to file";
    outputFile.close();*/
    
    //ifstream test("Atest.txt");
    ifstream test("A-small-attempt1.in");
    if (!test) {
        cerr << "Could not open the file.\n";
        exit(1);
    }
    small(test);
    
}
