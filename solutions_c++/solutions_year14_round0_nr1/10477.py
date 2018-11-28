#include <iostream>

using namespace std;

void getMagicianMethod(int testCaseNo, int rowInArragementOne, int arrangementOne[][4], int rowInArrangementTwo, int arrangeMentTwo[][4] ) {
    
    int numberOfMatches = 0, matchedCard;
    for(int i = 0; i<4; i++ ) {
        for(int j = 0; j<4; j++) {
            if(arrangementOne[rowInArragementOne - 1 ][i] == arrangeMentTwo[rowInArrangementTwo - 1 ][j] ) {
                numberOfMatches++;
                if(numberOfMatches == 1) {
                    matchedCard = arrangementOne[rowInArragementOne - 1][i];
                }
                
            }
        }
    }

    if(numberOfMatches == 1) {
        cout<<"Case #"<<testCaseNo<<": "<<matchedCard<<endl;
    }
    else if(numberOfMatches > 1) {
        cout<<"Case #"<<testCaseNo<<": Bad magician!"<<endl;
    }
    else {
        cout<<"Case #"<<testCaseNo<<": Volunteer cheated!"<<endl;
    }
}

void getArrangements(int testCaseNo) {
    int rowInArrangementOne = 0, rowInArrangementTwo = 0, arrangementOne[4][4], arrangementTwo[4][4];
    cin>>rowInArrangementOne;
    
    for(int i=0; i<4; i++) {
        for(int j=0; j<4; j++) {
            cin>>arrangementOne[i][j];
        }
    }
    
    cin>>rowInArrangementTwo;
    for(int i=0; i<4; i++) {
        for(int j=0; j<4; j++) {
            cin>>arrangementTwo[i][j];
        }
    }
    
    getMagicianMethod(testCaseNo, rowInArrangementOne, arrangementOne, rowInArrangementTwo, arrangementTwo );
}

int main(void)
{
    int testCaseNo = 1,testCases; 
    cin>>testCases;
    while( testCaseNo <= testCases ) {
        getArrangements(testCaseNo);
        testCaseNo++;
    }
}
