#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <stack>

using namespace std;

int main(int argc, char* args[]) {
        // Open the file
    ifstream ifs("A-small-attempt0.in");
    ofstream ofs("output.txt");

    string line;
    getline(ifs, line);
    stringstream ssNum(line);
    int num;
    ssNum >> num;

    for (int i = 0; i < num; i++) {
        getline(ifs, line);
        stringstream ssFirstChoose(line);
        int firstChoose;
        ssFirstChoose >> firstChoose;

        vector<vector<int> > firstCards;
        for (int row = 0; row < 4; row++) {
            vector<int> temp;
            getline(ifs, line);
            stringstream ssRow(line);
            for (int col = 0; col < 4; col++) {
                int value;
                ssRow >> value;
                temp.push_back(value);
            }
            firstCards.push_back(temp);
        }

        getline(ifs, line);
        stringstream ssSecondChoose(line);
        int secondChoose;
        ssSecondChoose >> secondChoose;

        vector<vector<int> > secondCards;
        for (int row = 0; row < 4; row++) {
            vector<int> temp;
            getline(ifs, line);
            stringstream ssRow(line);
            for (int col = 0; col < 4; col++) {
                int value;
                ssRow >> value;
                temp.push_back(value);
            }
            secondCards.push_back(temp);
        }

        vector<int> rowFirstCards = firstCards[firstChoose - 1];
        vector<int> rowSecondCards = secondCards[secondChoose - 1];

        int answer = 0;
        int isFound = 0; // 0: not found; 1: found; 2: duplicated
        for (int j = 0; j < 4; j++) {
            int value = rowFirstCards[j];
            for (int k = 0; k < 4; k++) {
                if (value == rowSecondCards[k]) {
                    if (isFound == 0) {
                        answer = value;
                        isFound = 1;
                        break;
                    } else if (isFound == 1) {
                        isFound = 2;
                        break;
                    }
                }
            }
            if (isFound == 2) {
                break;
            }
        }


        ofs << "Case #" << (i + 1) << ": ";
        if (isFound == 1) {
            ofs << answer << endl;
        } else if (isFound == 2) {
            ofs << "Bad magician!" << endl;
        } else {
            ofs << "Volunteer cheated!" << endl;
        }
    }

    ifs.close();
    ofs.close();
}
