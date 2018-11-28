#include <iostream>
using namespace std;

int main() {
    int caseNum;

    cin >> caseNum;
    for (int caseCount = 1; caseCount <= caseNum; caseCount++) {
        int maxLevel;
        string peopleStr;
        int clapPeopleCount = 0;
        int addPeople = 0;

        cin >> maxLevel >> peopleStr;
        for (int level = 0; level <= maxLevel; level++) {
            int peopleNum = peopleStr[level] - '0';

            if (peopleNum == 0) {
                continue;
            } else if (clapPeopleCount >= level) {
                clapPeopleCount += peopleNum;
            } else {
                addPeople += level - clapPeopleCount;
                clapPeopleCount = level + peopleNum;
            }
        }
        cout << "Case #" << caseCount << ": " << addPeople << endl;
    }

    return 0;
}
