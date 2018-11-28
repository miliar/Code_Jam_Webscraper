#include <iostream>
#include <sstream>

using namespace std;


int main(int argc, char** argv) {
    int numTest = 0;
    cin >> numTest;
    for (int i = 1; i <= numTest; i++){
        int NumFriends = 0;
        int numSoFar = 0;
        int Smax, numMember;
        string members;
        cin >> Smax >> members;
        for (int level = 0; level <= Smax; level++){
            numMember = members[level] - '0';
            if ((level > numSoFar) && (numMember != 0)){
                NumFriends += (level - numSoFar);
                numSoFar += (level - numSoFar);
            }
            numSoFar += numMember;
        }
        cout << "Case #" << i << ": " << NumFriends << endl;
    }
    
    return 0;
}


