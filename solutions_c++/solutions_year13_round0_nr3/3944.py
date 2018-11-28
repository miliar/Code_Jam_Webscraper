#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <math.h>
using namespace std;

string convertToString(double num) {
    stringstream ss;
    ss << num;
    string s(ss.str());
    return s;
}

bool checkIfPalindrome(double num) {
    string str = convertToString(num);
    
    int len = str.length();
    for (int i = 0; i < len/2; i++) {
        if (str[i] != str[len - i - 1])
            return false;
    }
    
    return true;
}

int main(void) {
    ofstream out;
    out.open("c.out");
    
    int T;
    cin >> T;
    
    for(int i = 0; i < T; i++) {
        int start, end, total;
        total = 0;
        
        cin >> start;
        cin >> end;
        
        for(int j = start; j <= end; j++) {
            if(checkIfPalindrome(j) && checkIfPalindrome(sqrt(j)))
                total++;
        }
        
        out << "Case #" << i+1 << ": " << total << endl;
    }
    
    return 0;
}
