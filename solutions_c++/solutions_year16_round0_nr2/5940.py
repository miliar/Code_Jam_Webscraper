#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
using namespace std;

bool happyStack(const vector<bool>& stack) {
    for (int i = 0; i < stack.size(); ++i)
        if (!stack[i])
            return false;
    return true;
}

void flipStack(vector<bool>& stack, int s, int e) {
    for (int i = s; i <= e; ++i)
        stack[i] = !stack[i];
}

int minFlips(const string& str) {
    vector<bool> stack(str.size());
    for (int i = 0; i < str.size(); ++i)
        stack[i] = (str[i] == '+');
    
    int count = 0;
    for ( ; !happyStack(stack); ++count) {
        int i = 0;
        for (; i < stack.size()-1; ++i)
            if (stack[i] != stack[i+1])
                break;
        
        flipStack(stack, 0, i);
    }
    
    return count;
}

void readInput(const string& inFile, const string& outFile) {
    ifstream in(inFile.c_str());
    if (!in)
        throw exception();
    
    FILE* pFile = fopen(outFile.c_str(), "w");
    if (!pFile)
        throw exception();
    
    int T;
    in >> T;
    for (int i = 0; i < T; ++i) {
        string S;
        in >> S;
        int res = minFlips(S);
        fprintf(pFile, "Case #%d: %s\n", i+1, to_string(res).c_str());
    }
}


int main(int argc, const char * argv[]) {
    readInput("/Users/elvirakalviste/Desktop/CodeJam2016/CodeJam2016/b_small.in",
              "/Users/elvirakalviste/Desktop/CodeJam2016/CodeJam2016/b_small.out");
    
    return 0;
}
