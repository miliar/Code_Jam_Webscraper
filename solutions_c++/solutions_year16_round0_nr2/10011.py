//
//  main.cpp
//  Problem B. Revenge of the Pancakes
//
//  Created by KoRNz on 4/9/2559 BE.
//  Copyright © 2559 KoRNz. All rights reserved.
//

#include <iostream>
#include <vector>
#include <sstream>
#include <string>

using namespace std;

string S;

int diff(string *s) {
    int count = 0;
    for(int i = 0; i < (*s).length(); i++) {
        if((*s)[i] == '-') count++;
    }
    return count;
}

string flip(string s, int n) {
//    cout << "String: " + s << endl;
    
    // Flip
    for (int i = 0; i <= n; i++) {
        if(s[i] == '-') s[i] = '+';
        else s[i] = '-';
    }
    
    // Swap
    for (int i = 0; i <= n; i++) {
        swap(s[i], s[n - i]);
    }
    
    return s;
}

//long long compute(string s, long long n) {
//    
//    int dif = diff(&s);
//    if(dif == 0) return n;
//    for(int i = (int)s.length() - 1; i >= 0; i--) {
//        
//        // Try to flip first i-th pancakes
//        string tmpFlip = flip(s, i);
//        int d = diff(&tmpFlip);
//        
//        // Not flip
//        if(d >= dif) continue;
//        
//        // Flip
//        else {
//            n = compute(tmpFlip, ++n);
//        }
//    }
//    
//    return n;
//}

long long computeEz(string s, long long n, int prevFlip) {
    
    int dif = diff(&s);
    if(dif == 0) return n;
    
    int best = INT_MAX;
    for(int i = prevFlip - 1; i >= 0; i--) {
        long long tmp = computeEz(flip(s, i), n+1, i);
        if(tmp < best) best = (int)tmp;
    }
    
    return best;
}

long long Solve() {
    
    // Input
    cin >> S;
    
    long long answer = computeEz(S, 0, (int)S.length());
    
    
    //return answer
    return answer;
};

int main()
{
    //To insert number of testcases
    int n = 0;
    cin >> n;
    
    //To call Solve method
    long long answer;
    for (int i=0; i < n; i++) {
        answer = Solve();
        
        int num = i+1;
        ostringstream convert;
        convert << num;
        string sNum = convert.str();
        
        //store answer
        string sAnswer = std::to_string(answer);
        cout << "Case #" + sNum + ": " + sAnswer << endl;
    }
    
    return 0;
}