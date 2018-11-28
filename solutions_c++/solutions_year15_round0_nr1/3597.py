#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream inputFile("input.txt");
    ofstream outputFile("output.txt");

    int testCasesNum;
    inputFile >> testCasesNum;

    for(int i = 0; i < testCasesNum; i++) {
        int highestShynessLevel; inputFile >> highestShynessLevel;

        char shyPeople[1005]; inputFile >> shyPeople;
        int shyPeopleInt[1005];

        for(int j = 0; j <= highestShynessLevel; j++) {
            shyPeopleInt[j] = shyPeople[j] - '0';
        }

        int availablePeople = shyPeopleInt[0];
        int requestedPeople = 0;

        for(int j = 1; j <= highestShynessLevel; j++) {
            if(availablePeople < j && shyPeopleInt[j] > 0) {
                requestedPeople += j - availablePeople;
                availablePeople += j - availablePeople;
            }

            availablePeople += shyPeopleInt[j];
        }

        outputFile << "Case #" << i + 1 << ": " << requestedPeople << "\n";
    }

    return 0;
}
