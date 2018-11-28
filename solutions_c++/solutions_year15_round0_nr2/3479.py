#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
    ifstream inputFile("input.txt");
    ofstream outputFile("output.txt");

    int testCasesNum;
    inputFile >> testCasesNum;

    for(int i = 0; i < testCasesNum; i++) {

        vector<int> myVector;

        int dinersNum;
        inputFile >> dinersNum;

        for(int j = 0; j < dinersNum; j++) {
            int tempInput;
            inputFile >> tempInput;

            myVector.push_back(tempInput);
        }

        int leastVal = 20000;

        for(int d = 1; d <= 1000; d++) {
            int specialMinutes = 0;
            int totalMinutes = 0;
            int maxEntry = 0;

            for(int k = 0; k < myVector.size(); k++) {
                specialMinutes += (myVector[k] / d) - 1;
                if(myVector[k] % d > 0) { specialMinutes++; }
                if(myVector[k] / d > maxEntry) { maxEntry = myVector[k] / d; }
            }

            totalMinutes = specialMinutes + max(maxEntry, d);

            if(totalMinutes < leastVal) {
                leastVal = totalMinutes;
            }
        }

        outputFile << "Case #" << i + 1 << ": " << leastVal << "\n";
    }

    return 0;
}
