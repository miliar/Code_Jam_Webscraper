#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

//static const string INPUT_FILE = "R1A_A-Small.in";
//static const string OUTPUT_FILE = "R1A_A-Small.out";
static const string INPUT_FILE = "R1A_A-Large.in";
static const string OUTPUT_FILE = "R1A_A-Large.out";

int caseNumber = 1;

// method dclarations
void readFile(int& testCases, vector<string>& cases);
void eval(string word, int index, string& whiteboard);

int main(int argc, char* argv[]) {
    int testCases = 0;
    vector<string> cases;
    
    // reads a file line by line and gets the test cases
    readFile(testCases, cases);
    
    ofstream myfile(OUTPUT_FILE);
    
    vector<string>::iterator it;
    for (it = cases.begin(); it < cases.end(); ++it) {
        string word = *it;
        string whiteboard = "";
        eval(word, 0, whiteboard);
        
        if (myfile.is_open()) {
            myfile << "Case #" << caseNumber << ": " << whiteboard << endl;
        }
        caseNumber++;
    }
    
    myfile.close();
    
    return 0;
}

void readFile(int& testCases, vector<string>& cases) {
    string line;
    ifstream myfile(INPUT_FILE);
    if (myfile.is_open()) {
        getline(myfile, line);  // skip number of cases since using vector
        
        while (getline(myfile, line)) {
            cases.push_back(line);
        }
        
        myfile.close();
    }
}

void eval(string word, int index, string& whiteboard) {
    string before = word[index] + whiteboard;
    string after = whiteboard + word[index];
    
//    The member function returns 0 if all the characters in the compared contents compare equal, a negative value if the first character that does not match compares to less in the object than in the comparing string, and a positive value in the opposite case.
    
    transform(before.begin(), before.end(), before.begin(), ::tolower);
    transform(after.begin(), after.end(), after.begin(), ::tolower);
    
    int result = before.compare(after);
    if (result >= 0) {
        if (++index <= word.length()) {
            whiteboard = before;
            eval(word, index, whiteboard);
        }
    } else if (result < 0) {
        if (++index <= word.length()) {
            whiteboard = after;
            eval(word, index, whiteboard);
        }
    }
}