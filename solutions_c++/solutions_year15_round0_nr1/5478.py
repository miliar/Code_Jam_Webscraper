#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

int main(int argc, char *argv[]) {
    ifstream file;
    ofstream outputFile;

    int intTestCases = 0;
    int maxShyness = 0;
    vector<int> myVector;
    vector<int>::iterator it;
    char currentCharacter;
    int totalPeopleInRoom = 0;
    int currentStandingPeople = 0;
    int currentExtraPeopleNeeded = 0;
    int totalExtraPeopleNeeded = 0;
            
    outputFile.open(argv[2]);
    file.open(argv[1]);

    if (!file.eof()) {
        file >> intTestCases;
    }

    for (int t=0; t<intTestCases; ++t) {
        totalPeopleInRoom = 0;
        currentStandingPeople = 0;
        currentExtraPeopleNeeded = 0;
        totalExtraPeopleNeeded = 0;

        file >> maxShyness;
        
        for (int i=0; i<maxShyness+1; ++i) {
            file >> currentCharacter;
            myVector.push_back(currentCharacter - '0'); 
            totalPeopleInRoom = totalPeopleInRoom + (currentCharacter - '0');
        }

        currentStandingPeople = myVector.at(0);

        for (int i=1; i<myVector.size(); i++) {
            if (currentStandingPeople < i) {
                if (myVector.at(i) > 0) {
                    currentExtraPeopleNeeded = i - currentStandingPeople;
                    totalExtraPeopleNeeded = totalExtraPeopleNeeded + currentExtraPeopleNeeded;
                    currentStandingPeople = currentStandingPeople + currentExtraPeopleNeeded + myVector.at(i);
                }
            } else {
                currentStandingPeople = currentStandingPeople + myVector.at(i);
            }
        }

        if (t==0) {
            outputFile << "Case #" << t+1 << ": " << totalExtraPeopleNeeded;
        } else {
            outputFile << "\nCase #" << t+1 << ": " << totalExtraPeopleNeeded;
        }
        
        myVector.clear();
    }
}
