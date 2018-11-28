#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
    ifstream inFile("A-large.in");
    if (!inFile.is_open())
        return -1;

    ofstream outFile("A-large-output.txt");
    if (!outFile.is_open())
        return -2;


    int numTestCases;
    inFile >> numTestCases;

    for (int testCase = 0; testCase < numTestCases; ++testCase) {
        int S;
        inFile >> S;

        vector<int> people;
        people.reserve(S);

        char t;
        for (int i = 0; i <= S; ++i) {
            inFile >> t;
            people.push_back(t-48);
        }

        int standingPeople = 0, additionalPeople = 0;
        for (int shyness = 0; shyness < people.size(); shyness++) {
            if (standingPeople < shyness) {
                additionalPeople += shyness-standingPeople;
                standingPeople += shyness-standingPeople;
            }

            standingPeople += people[shyness];
        }


        outFile << "Case #" << testCase+1 << ": " << additionalPeople << endl;
    }

    inFile.close();
    outFile.close();

    return 0;
}
