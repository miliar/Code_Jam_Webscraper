//
//  main.cpp
//  Revenge of the Pancakes
//
//  Created by TsengKai Han on 4/8/16.
//  Copyright © 2016 TsengKai Han. All rights reserved.
//

#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;


int pancake(string s){
    while (s.back() == '+') {//erase '+' from back
        s.pop_back();
    }
    if (s.empty()) {
        return 0;
    }

    if (s[0] == '+') {//'+'
        s[0] = '-';
        for(int i = 1; i < s.size(); i++){
            if (s[i] == '+') {
                s[i] = '-';
            }
            else{
                break;
            }
        }
        return 1 + pancake(s);
    }
    else{//'-'
        string new_s;
        while (!s.empty()) {
            if (s.back() == '+') {
                new_s = new_s + '-';
                s.pop_back();
            }
            else{
                new_s = new_s + '+';
                s.pop_back();
            }
        }
        return 1 + pancake(new_s);
    }
}


int main (int argc, const char * argv[]) {
    fstream fout;
    fout.open("sol_l.txt", ios::out);
    ifstream fin;
    fin.open(argv[1],ios::in|ios::binary);
    string s;
    //input by file
    if (fin.is_open()){//file opened
        fin>>s;
        int case_num = stoi(s);//how many cases
        for (int i = 0; i < case_num; i++) {
            fin>>s;
            fout<<"Case #"<<i + 1<<": ";
            fout<<pancake(s)<<endl;
        }
    }
    else{
        cout<<"opend fail"<<endl;
    }
    
    
    return 0;
}