#include <iostream>
#include <fstream>
#include <stdio.h>

using namespace std;

int main() {
    fstream in("in");
    fstream out("out");
    int tt;
    in >> tt;
    
    for (int i=1; i<=tt; i++) {
        int answer = 0;
        
        //Start Work
        int sMax = 0, stoodUp = 0;
        in >> sMax;
        char firstNum;
        in >> firstNum;
        stoodUp = firstNum - '0';

        for (int j=1; j<=sMax; j++) {
            char num;
            in >> num;
            int numInt = num - '0';
            
            if (stoodUp < j && numInt > 0) {
                answer += j - stoodUp;
                stoodUp += answer + numInt;
            } else if (stoodUp >= j) {
                stoodUp += numInt;
            }
        }
        
//        cout << i << "# Stood Up: " << stoodUp << endl << "Total People: " << totalPeople << endl << "Answer: " << answer << endl << endl;
        
        //Case #1: 0
        cout << "Case #" << i << ": " << answer << endl;
        out << "Case #" << i << ": " << answer << endl;
    }
    
    out.close();
    in.close();
    return 0;
}
