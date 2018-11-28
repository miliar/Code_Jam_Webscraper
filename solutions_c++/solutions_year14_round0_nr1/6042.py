#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

void findCard(vector<vector<int> > &cardArrangementA, vector<vector<int> > &cardArrangementB, int& questionA, int& questionB) {
    int i;
    int results = 0, foundCards = 0, card = 0;

    for(i = 0; i < 4; i++) {
        results = count(cardArrangementB[(questionB - 1)].begin(), cardArrangementB[(questionB - 1)].end(), cardArrangementA[(questionA - 1)][i]);
        if(results == 1) {
            foundCards++;
            card = cardArrangementB[(questionB - 1)][(find(cardArrangementB[(questionB - 1)].begin(), cardArrangementB[(questionB - 1)].end(), 
                    cardArrangementA[(questionA - 1)][i]) - cardArrangementB[(questionB - 1)].begin())];
        }
    }
    
    if(foundCards == 1) {
        cout << card << endl;
    } else if(foundCards == 0) {
        cout << "Volunteer cheated!" << endl;
    } else {
        cout << "Bad magician!" << endl;
    }
}

int main() {
    int T;
    int i, j, k;
    int questionA, questionB;
    vector<vector<int> > cardArrangementA(4, vector<int>(4, 0));
    vector<vector<int> > cardArrangementB(4, vector<int>(4, 0));

    ifstream testFile("a.in");
    freopen("a.out", "w", stdout);
    
    testFile >> T;
    
    for(i = 0; i < T; i++) {
        testFile >> questionA;
        for(j = 0; j < 4; j++) {
            for(k = 0; k < 4; k++) {
                testFile >> cardArrangementA[j][k];
            }
        }

        testFile >> questionB;
        for(j = 0; j < 4; j++) {
            for(k = 0; k < 4; k++) {
                testFile >> cardArrangementB[j][k];
            }
        }
        
        cout << "Case #" << (i+1) << ": ";
        findCard(cardArrangementA, cardArrangementB, questionA, questionB);
    }
    
    return 0;
}
