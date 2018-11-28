#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <sstream>

using namespace std;


string toString(int n) {
    string result;
    ostringstream convert;
    convert << n;
    result = convert.str();
    return result;
}


bool palindrome(int n) {
    string word = toString(n);
    int length = word.length();
    int half = floor(length/2);
    const char* chain= word.c_str();

    bool palin = true;
    for (int i=0; (i!=half) && (palin) ; i++) {
        if (chain[i] != chain[length-i-1]) {
            palin = false;
        }
    }
    return palin;
}

int solveFairSquare(int min, int max) {
    int a = ceil(sqrt(min));  // ceil
    int b = floor(sqrt(max)); // floor

    int count = 0;
    for(int i=a; i<=b;i++) {
        if (palindrome(i)) {
            if (palindrome(i*i)) count++;
        }
    }
    return count;
}



/** ******************
 *  MAIN PROGRAM
 ** ******************/

int main()
{
    string line;
    ifstream myFile;
    myFile.open("test.txt");
    if (myFile.is_open()) {
        // N Test Cases
        int T;
        myFile >> T;
        for (int caseN  = 0; caseN != T; caseN++) {
            int a,b;
            myFile >> a >> b;
            cout << "Case #" << caseN+1 << ": ";
            cout << solveFairSquare(a,b) << endl;
        }
    } else {
        cout << "Unable to read file." << endl;
    }
    myFile.close();
    return 0;
}

