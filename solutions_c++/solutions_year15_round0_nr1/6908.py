//
//  main.cpp
//  GoogleCodeJam_Q2015_StandingOvation
//
//  Created by Youngduke Koh on 4/11/15.
//  Copyright (c) 2015 Youngduke Koh. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, const char * argv[]) {
    int T, S, temp, i, j, answer, sum;
    char buffer[1003];
    
    ifstream in("in.txt");
    cin.rdbuf(in.rdbuf());
    
    cin >> T;
    i = 0;
    while (i < T) {
        i++;
        cin >> S;
        cin.getline(buffer, 1003);
        j = 2;
        answer = 0;
        sum = buffer[1] - '0';
        while (buffer[j]) {
            temp = buffer[j] - '0';
            
            if (temp >= 0 && temp <= 9) {
                if (sum < (j - 1)) {
                    answer++;
                    sum++;
                }
                sum += temp;
            }
            j++;
        }
        cout << "Case #" << i << ": " << answer << "\n";
    }
    
    return 0;
}
