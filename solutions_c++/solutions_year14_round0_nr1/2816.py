#include <iostream>

using namespace std;

int test(int *oLine, int *nLine){
    int nCase = 0;
    int validAns = 0;

    for ( int i = 0; i < 4; ++i ){
        int choice = oLine[i];
        for ( int j = 0; j < 4; ++j ){
            if ( choice == nLine[j] ){
                nCase++;
                validAns = choice;
            }
        }
    }

    if ( nCase == 0 ){
        return -2;
    }
    if ( nCase > 1 ){
        return -1;
    }

    return validAns;
}

int main(int argc, char const *argv[]){
    int nCase;
    int oGrid[4][4];
    int nGrid[4][4];
    cin >> nCase;

    for ( int k = 0; k < nCase; ++k ){
        int firstA, secondA;
        cin >> firstA;
        for ( int i = 0; i < 4; ++i ){
            for ( int j = 0; j < 4; ++j ){
                cin >> oGrid[i][j];
            }
        }

        cin >> secondA;
        for ( int i = 0; i < 4; ++i ){
            for ( int j = 0; j < 4; ++j ){
                cin >> nGrid[i][j];
            }
        }

        int ans = test(oGrid[firstA - 1], nGrid[secondA - 1]);
        switch(ans){
            case -1:
                printf("Case #%d: Bad magician!\n", k+1);
                break;
            case -2:
                printf("Case #%d: Volunteer cheated!\n", k+1);
                break;
            default:
                printf("Case #%d: %d\n", k+1, ans);
        }

    }

    return 0;
}