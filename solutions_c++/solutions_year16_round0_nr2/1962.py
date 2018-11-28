#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <math.h>
#include <stdlib.h>

using namespace std;

void flip(string &pStack, int position) {
    for (int i=0;i<=position;i++) {
        if (pStack[i] == '-') {
            pStack[i] = '+';
        } else pStack[i] = '-';
    }
}

int calculateNumFlips(string pStack) {
    int result = 0;
    int size = pStack.size();
    
    int position = size-1;
    
    while (position >= 0) {
        if (pStack[position] == '-') {
            flip(pStack, position);
            result++;
        }
        position--;
    }
    
    return result;
}

int main() {
    ifstream fin ("/Users/LeonardNguyen/Documents/projects/ios/usaco/B-large.in");
    
    string strT;
    getline(fin, strT);
    int T = stoi(strT);
    
    for (int i=0;i<T;i++) {
        string pStack;
        getline(fin, pStack);
        cout<<"Case #"<<(i+1)<<": "<<calculateNumFlips(pStack)<<endl;
    }
    
    fin.close();
    
    return 0;
}

