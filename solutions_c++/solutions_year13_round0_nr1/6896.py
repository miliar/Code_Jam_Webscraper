#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){

    int numTests;

    cin >> numTests;

    vector<int> results(numTests);

    for(int i = 0; i < numTests; ++i){
        vector<unsigned char> symbl(16);
        int currentPos = 0;
        for(int j = 0; j < 4; ++j){
            cin >> symbl[currentPos++];
            cin >> symbl[currentPos++];
            cin >> symbl[currentPos++];
            cin >> symbl[currentPos++];
        }

        // X Winner
        if((symbl[0] == 'X' ||  symbl[0] == 'T') && (symbl[4] == 'X' ||  symbl[4] == 'T') && (symbl[8] == 'X' ||  symbl[8] == 'T') && (symbl[12] == 'X' ||  symbl[12] == 'T') ||
           (symbl[1] == 'X' ||  symbl[1] == 'T') && (symbl[5] == 'X' ||  symbl[5] == 'T') && (symbl[9] == 'X' ||  symbl[9] == 'T') && (symbl[13] == 'X' ||  symbl[13] == 'T') ||
           (symbl[2] == 'X' ||  symbl[2] == 'T') && (symbl[6] == 'X' ||  symbl[6] == 'T') && (symbl[10] == 'X' ||  symbl[10] == 'T') && (symbl[14] == 'X' ||  symbl[14] == 'T') ||
           (symbl[3] == 'X' ||  symbl[3] == 'T') && (symbl[7] == 'X' ||  symbl[7] == 'T') && (symbl[11] == 'X' ||  symbl[11] == 'T') && (symbl[15] == 'X' ||  symbl[15] == 'T') ||

           (symbl[0] == 'X' ||  symbl[0] == 'T') && (symbl[1] == 'X' ||  symbl[1] == 'T') && (symbl[2] == 'X' ||  symbl[2] == 'T') && (symbl[3] == 'X' ||  symbl[3] == 'T') ||
           (symbl[4] == 'X' ||  symbl[4] == 'T') && (symbl[5] == 'X' ||  symbl[5] == 'T') && (symbl[6] == 'X' ||  symbl[6] == 'T') && (symbl[7] == 'X' ||  symbl[7] == 'T') ||
           (symbl[8] == 'X' ||  symbl[8] == 'T') && (symbl[9] == 'X' ||  symbl[9] == 'T') && (symbl[10] == 'X' ||  symbl[10] == 'T') && (symbl[11] == 'X' ||  symbl[11] == 'T') ||
           (symbl[12] == 'X' ||  symbl[12] == 'T') && (symbl[13] == 'X' ||  symbl[13] == 'T') && (symbl[14] == 'X' ||  symbl[14] == 'T') && (symbl[15] == 'X' ||  symbl[15] == 'T') ||

           (symbl[0] == 'X' ||  symbl[0] == 'T') && (symbl[5] == 'X' ||  symbl[5] == 'T') && (symbl[10] == 'X' ||  symbl[10] == 'T') && (symbl[15] == 'X' ||  symbl[15] == 'T') ||
           (symbl[3] == 'X' ||  symbl[3] == 'T') && (symbl[6] == 'X' ||  symbl[6] == 'T') && (symbl[9] == 'X' ||  symbl[9] == 'T') && (symbl[12] == 'X' ||  symbl[12] == 'T') 
          ) {
              results[i] = 0;
        } else if((symbl[0] == 'O' ||  symbl[0] == 'T') && (symbl[4] == 'O' ||  symbl[4] == 'T') && (symbl[8] == 'O' ||  symbl[8] == 'T') && (symbl[12] == 'O' ||  symbl[12] == 'T') ||
           (symbl[1] == 'O' ||  symbl[1] == 'T') && (symbl[5] == 'O' ||  symbl[5] == 'T') && (symbl[9] == 'O' ||  symbl[9] == 'T') && (symbl[13] == 'O' ||  symbl[13] == 'T') ||
           (symbl[2] == 'O' ||  symbl[2] == 'T') && (symbl[6] == 'O' ||  symbl[6] == 'T') && (symbl[10] == 'O' ||  symbl[10] == 'T') && (symbl[14] == 'O' ||  symbl[14] == 'T') ||
           (symbl[3] == 'O' ||  symbl[3] == 'T') && (symbl[7] == 'O' ||  symbl[7] == 'T') && (symbl[11] == 'O' ||  symbl[11] == 'T') && (symbl[15] == 'O' ||  symbl[15] == 'T') ||

           (symbl[0] == 'O' ||  symbl[0] == 'T') && (symbl[1] == 'O' ||  symbl[1] == 'T') && (symbl[2] == 'O' ||  symbl[2] == 'T') && (symbl[3] == 'O' ||  symbl[3] == 'T') ||
           (symbl[4] == 'O' ||  symbl[4] == 'T') && (symbl[5] == 'O' ||  symbl[5] == 'T') && (symbl[6] == 'O' ||  symbl[6] == 'T') && (symbl[7] == 'O' ||  symbl[7] == 'T') ||
           (symbl[8] == 'O' ||  symbl[8] == 'T') && (symbl[9] == 'O' ||  symbl[9] == 'T') && (symbl[10] == 'O' ||  symbl[10] == 'T') && (symbl[11] == 'O' ||  symbl[11] == 'T') ||
           (symbl[12] == 'O' ||  symbl[12] == 'T') && (symbl[13] == 'O' ||  symbl[13] == 'T') && (symbl[14] == 'O' ||  symbl[14] == 'T') && (symbl[15] == 'O' ||  symbl[15] == 'T') ||

           (symbl[0] == 'O' ||  symbl[0] == 'T') && (symbl[5] == 'O' ||  symbl[5] == 'T') && (symbl[10] == 'O' ||  symbl[10] == 'T') && (symbl[15] == 'O' ||  symbl[15] == 'T') ||
           (symbl[3] == 'O' ||  symbl[3] == 'T') && (symbl[6] == 'O' ||  symbl[6] == 'T') && (symbl[9] == 'O' ||  symbl[9] == 'T') && (symbl[12] == 'O' ||  symbl[12] == 'T') 
          ) {
              results[i] = 1;
        } else if (find(symbl.begin(), symbl.end(), '.') != symbl.end()){
            results[i] = 2;
        } else
            results[i] = 3;
    }

    for(int i = 0; i < numTests; ++i){
        cout << "Case #" << i+1;
        switch(results[i]){
            case 0: cout << ": X won" << endl;;
                    break;
            case 1: cout << ": O won" << endl;
                    break;
            case 2: cout << ": Game has not completed" << endl;
                    break;
            case 3: cout << ": Draw" << endl;
                    break;
        }
    }
    return 0;
}

