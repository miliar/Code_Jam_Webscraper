#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main(int argc, char ** argv) {
    int testCases;
    cin >> testCases;
    int countCases = 0;
    for (countCases; countCases < testCases; countCases ++) {
        string wordString;
        cin >> wordString;

        string outputString = "";
        outputString.append(wordString.substr(0,1));
        int wordIndex = 1;

        for (wordIndex; wordIndex < wordString.length(); wordIndex ++){
            if (wordString[wordIndex] >= outputString[0]){
                outputString = wordString.substr(wordIndex,1) + outputString;
            } else {
                outputString.append(wordString.substr(wordIndex,1));
            }
        }


        cout << "Case #" << countCases + 1 << ": " << outputString << endl;
    }
    return 0;
}

string charToString (){

}