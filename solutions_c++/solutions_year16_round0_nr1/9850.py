//
//  main.cpp
//  Problem A. Counting Sheep
//
//  Created by KoRNz on 4/9/2559 BE.
//  Copyright © 2559 KoRNz. All rights reserved.
//

#include <iostream>
#include <vector>
#include <sstream>
#include <string>

using namespace std;

string digits;

long long Solve() {
    
    digits = "0123456789";
    
    //To choose first number of row
    long long M, N;
    cin >> N;
    
    if(N == 0) return -1;
    
//    for(int k = 1; k < 10000000; k++) {
    int k = 1;
    while(true) {
    
        M = N * k;
        k++;
        
        // Convert to string
        ostringstream convert;
        convert << M;
        string sNum = convert.str();
//        cout << "Number: " << sNum << endl;
    
        // Check
        for(int i = 0; i < sNum.length(); i++) {
            for(int j = 0; j < digits.length(); j++) {
                if(sNum[i] == digits[j]) digits.erase(digits.begin() + j);
                if(digits.length() == 0) return M;
            }
        }
    }
    
    
    //return answer
    return -1;
};

int main()
{
    //To insert number of testcases
    int n = 0;
    cin >> n;
    
    //To call Solve method
    long long answer;
    for (int i=0; i<n; i++) {
        answer = Solve();
        
        int num = i+1;
        ostringstream convert;
        convert << num;
        string sNum = convert.str();
        
        //store answer
        if (answer == -1) {
            cout << "Case #" + sNum + ": " + "INSOMNIA" << endl;
        }
        else {
            string sAnswer = std::to_string(answer);
            
            cout << "Case #" + sNum + ": " + sAnswer << endl;
        }
    }
    
    return 0;
}