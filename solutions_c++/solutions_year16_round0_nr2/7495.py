//
//  QB-large.cpp
//  CodeJam2016
//
//  Created by Ha Young Park on 4/9/16.
//  Copyright © 2016 UCLA. All rights reserved.
//

#include <fstream>
#include <vector>
#include <string>

using namespace std;

string reduce(string* str){
    string::size_type found = str->find_last_of('-');
    return str->substr(0, found + 1);
}

string flip(string* str){
    string ret_str;
    for(string::reverse_iterator rit = str->rbegin(); rit != str->rend(); rit++){
        ret_str += *rit=='-'?'+':'-';
    }
    return ret_str;
}

int main(int argc, const char * argv[]) {
    ifstream fin; fin.open("B-large.in");
    ofstream fout; fout.open("B-large.out");
    
    int T;
    fin >> T;
    
    for(int i = 1; i <= T; i++){
        string S;
        fin >> S;
        
        int y = 0;
        
        while(S.find('-') != string::npos){
            S = reduce(&S);
            
            if(S.find('+') == string::npos ||
               S.size() - 1 - S.find_last_of('+') < S.find_first_of('+')){
                S = flip(&S);
                y++;
            }
            else if(S.find_first_of('+') < S.find_first_of('-')){
                string temp = S.substr(0, S.find_first_of('-'));
                S.replace(0, temp.length(), flip(&temp));
                y++;
            }
            else if(S.find_first_of('+') > 0){
                string temp = S.substr(0, S.find_first_of('+'));
                S.replace(0, temp.length(), flip(&temp));
                y++;
            }
        }
        
        
        fout << "Case #" << i << ": " << y << endl;
        
    }
    fout.close();
    fin.close();
    return 0;
}