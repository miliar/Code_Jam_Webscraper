#include <iostream>
#include <cstdio>
#include <fstream>

using namespace std;

int main()
{
    ofstream resultFile;
    resultFile.open("result.txt");
    int T;
    cin >> T;
    for(int i = 0; i < T; ++i){
        int Smax;
        cin >> Smax;
        getchar(); // whitespace
        int needToInvite = 0, standing = 0;
        for(int s = 0; s <= Smax; ++s){
            int numOfCurrS = getchar() - '0';
            int currInv = s - standing;
            if(currInv < 0) currInv = 0;
            needToInvite += currInv;
            standing += currInv + numOfCurrS;
        }
        cout << "Case #" << i + 1 << ": " << needToInvite << endl;
        resultFile << "Case #" << i + 1 << ": " << needToInvite << endl;
    }
    resultFile.close();
    return 0;
}
