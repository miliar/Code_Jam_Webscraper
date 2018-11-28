//
//  main.cpp
//  CountingSheep
//
//  Created by TT on 09/04/2016.
//  Copyright © 2016 TT. All rights reserved.
//

#include <iostream>
#include <string>
#include <queue>
#include <unordered_set>

using namespace std;

typedef unsigned long long ull;

bool check(string& S){
    for (int i=0; i < S.length(); ++i){
        if (S[i] == '-'){
            return false;
        }
    }
    return true;
}

char negate_char(char c){
    if (c == '+'){
        return '-';
    } else {
        return '+';
    }
}

string updateOccurence(string S, size_t pos){
    
    string tmp = S.substr(0, pos + 1);
    
    for (int i=0; i<tmp.length(); ++i){
        S[i] = negate_char(tmp[tmp.length() - i - 1]);
    }
    return S;
}

string pre(string S){
    string tmp = "";
    char c = S[0];
    while (true){
        size_t pos = S.find_first_of(negate_char(c));
        if (pos == string::npos){
            tmp += c;
            break;
        }
        S = S.substr(pos);
        tmp += c;
        c = negate_char(c);
    }
    return tmp;
}

void fMain(int t){
    string S;
    cin >> S;
    
    S = pre(S);
    if (check(S)){
        cout << "Case #" << t << ": 0" << endl;
        return;
    }

    queue<string> qs;
    queue<int> qi;
    unordered_set<string> seen;
    
    for (int i=0; i<S.length(); ++i){
        string ss = updateOccurence(S, i);
        if (seen.find(ss) == seen.end()){
            qs.push(ss);
            qi.push(1);
            seen.insert(ss);
        }
        
    }
    
    while (true){
        string ts = qs.front();
        int ti = qi.front();
        qs.pop(); qi.pop();

        if (check(ts)){
            cout << "Case #" << t << ": " << ti << endl;
            break;
        }
        
        for (int i=0; i<ts.length(); ++i){
            string ss = updateOccurence(ts, i);
            if (seen.find(ss) == seen.end()){
                qs.push(ss);
                qi.push(ti + 1);
                seen.insert(ss);
            }
        }
    }
}




int main(int argc, const char * argv[]) {
    int T;
    cin >> T;
    for (int t = 1; t <=T; ++t){
        fMain(t);
    }
    return 0;
}
