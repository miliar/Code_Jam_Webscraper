//
//  main.cpp
//  Pancakes
//
//  Created by 이재현 on 2016. 4. 9..
//  Copyright © 2016년 haru. All rights reserved.
//

#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int N;
    cin >> N;
    for(int n=1;n<=N;n++) {
        char S[200];
        cin >> S;
        int count = 0;
        char prevS = '+';
        char currentS = '+';
        for(int i=0;;i++) {
            prevS = currentS;
            currentS = S[i];
            if(i==0) {
                if(currentS=='-') {
                    count--;
                }
            }
            else if(prevS=='-' && (currentS=='+' || currentS=='\0')) {
                count+=2;
            }
            if(currentS=='\0') break;
        }
        cout << "Case #" << n << ": " << count << endl;
    }
}
