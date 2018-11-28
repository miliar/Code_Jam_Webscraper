//
//  main.cpp
//  Coin Jam
//
//  Created by TsengKai Han on 4/8/16.
//  Copyright © 2016 TsengKai Han. All rights reserved.
//

#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
#include <math.h>
using namespace std;

string isJam(unsigned long long t){
    //init
    string s;
    while (t != 0) {
        s.insert(s.begin(), t%2 + '0');
        t = t/2;
    }
    
    //
    string r = s;
    for (int i = 2; i < 11; i++) {
        unsigned long long temp = 0;//base 10 number
        bool Prime = true;
        for (int k = 0; k < s.size(); k++) {
            temp = temp + pow(i, s.size() - k - 1) * (s[k] - '0');
        }
        //test prime
        for (int k = 2; k <= sqrt(temp); k++) {
            if (temp % k == 0) {//divisor
                r = r + " " + to_string(k);
                Prime = false;
                break;
            }
        }
        if (Prime) {
            return "";
        }
    }
    r = r + "\n";
    return r;
}

string jamcoins(int n, int j){
    string r;
    //loop all possible
    for (int i = 0; i < pow(2, n-2); i++) {
        unsigned long long temp = i^(i>>1);
        temp = temp<<1;
        temp++;
        temp = temp + pow(2, n-1);
        if (isJam(temp) != "") {//jamcoin
            r = r + isJam(temp);
            j--;
            if (j == 0) {
                return r;
            }
        }
    }
    return r;
}

int main (int argc, const char * argv[]) {
    fstream fout;
    fout.open("sol.txt", ios::out);
    ifstream fin;
    fin.open(argv[1],ios::in|ios::binary);
    string word;
    //input by file
    if (fin.is_open()){//file opened
        fin>>word;
        int case_num = stoi(word);//how many cases
        for (int i = 0; i < case_num; i++) {
            fin>>word;
            int N = stoi(word);
            fin>>word;
            int J = stoi(word);
            fout<<"Case #"<<i + 1<<": "<<endl;
            fout<<jamcoins(N, J);
        }
    }
    else{
        cout<<"opend fail"<<endl;
    }
    
    
    return 0;
}
