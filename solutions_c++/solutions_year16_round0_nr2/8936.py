#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <stack>
using namespace std;

//static const string INPUT_FILE = "B-Small.in";
//static const string OUTPUT_FILE = "B-Small.out";
static const string INPUT_FILE = "B-Large.in";
static const string OUTPUT_FILE = "B-Large.out";

static const char UNHAPPY = '-';
static const char HAPPY  = '+';
int caseNumber = 1;

// method dclarations
void readFile(int& testCases, vector<string>& cases);
void evaluatePancakeStack(string test);

int stringToInt(string str);
int stringToInt(char ch);
string intToString(int num);

int main(int argc, char* argv[]) {
    int testCases = 0;
    vector<string> cases;
    
    readFile(testCases, cases);
    
    vector<string>::iterator it;
    for (it = cases.begin(); it != cases.end(); ++it) {
        evaluatePancakeStack(*it);
    }
    
    return 0;
}

void readFile(int& testCases, vector<string>& cases) {
    string line;
    ifstream myfile(INPUT_FILE);
    if (myfile.is_open()) {
        getline(myfile, line);
        testCases = stringToInt(line);
        
        while (getline(myfile, line)) {
            cases.push_back(line);
        }
        
        myfile.close();
    }
}

void evaluatePancakeStack(string test) {
    stack<char> pancakeStack;
    
    // load stack with test string
    for (int i = test.size() - 1; i >= 0; --i) {
        pancakeStack.push(test.at(i));
    }
    
    int flipsNeeded = 0;
    while (pancakeStack.size() > 0) {
        char ch = pancakeStack.top();
        if (ch == UNHAPPY) {
            flipsNeeded++;
            pancakeStack.pop();
            int unhappyCount = 1;
            while (pancakeStack.size() > 0 && pancakeStack.top() == UNHAPPY) {
                pancakeStack.pop();
                unhappyCount++;
            }
            pancakeStack.push(HAPPY);
        } else {
            while (pancakeStack.size() > 0 && pancakeStack.top() == HAPPY) {
                pancakeStack.pop();
            }
            
            // check next...
            if (pancakeStack.size() > 0 && pancakeStack.top() == UNHAPPY) {
                flipsNeeded++;
                pancakeStack.push(UNHAPPY);
            }
        }
    }
    
    cout << "Case #" << caseNumber << ": " << flipsNeeded << endl;
    caseNumber++;
}


int stringToInt(string str) {
    stringstream ss(str);
    int num;
    ss >> num;
    
    return num;
}

int stringToInt(char ch) {
    stringstream ss;
    string str;
    ss << ch;
    ss >> str;
    
    int num = stringToInt(str);
    
    return num;
}

string intToString(int num) {
    string str = to_string(num);
    
    return str;
}