//
//  main.cpp
//  cj
//
//  Created by TsengKai Han on 4/30/16.
//  Copyright © 2016 TsengKai Han. All rights reserved.
//

#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
#include <math.h>
#include <map>
#include <algorithm>
using namespace std;

string gtd(string s){
    vector<int> ans;
    map<char,int> r;
    string ss;
    //init
    for (int i = 0; i < s.size(); i++) {
        r[s[i]]++;
    }
    
    //check zero
    while (r['Z'] != 0) {
        r['Z']--;
        r['E']--;
        r['R']--;
        r['O']--;
        ans.push_back(0);
    }
    
    //check two
    while (r['W'] != 0) {
        r['T']--;
        r['W']--;
        r['O']--;
        ans.push_back(2);
    }
    
    //check four
    while (r['U'] != 0) {
        r['F']--;
        r['O']--;
        r['U']--;
        r['R']--;
        ans.push_back(4);
    }
    
    //check six
    while (r['X'] != 0) {
        r['S']--;
        r['I']--;
        r['X']--;
        ans.push_back(6);
    }
    
    //check zero
    while (r['G'] != 0) {
        r['E']--;
        r['I']--;
        r['G']--;
        r['H']--;
        r['T']--;
        ans.push_back(8);
    }
    
    //check one
    while (r['O'] != 0) {
        r['O']--;
        r['N']--;
        r['E']--;
        ans.push_back(1);
    }
    
    //check three
    while (r['H'] != 0) {
        r['T']--;
        r['H']--;
        r['R']--;
        r['E']--;
        r['E']--;
        ans.push_back(3);
    }
    
    //check five
    while (r['F'] != 0) {
        r['F']--;
        r['I']--;
        r['V']--;
        r['E']--;
        ans.push_back(5);
    }
    
    //check seven
    while (r['S'] != 0) {
        r['S']--;
        r['E']--;
        r['V']--;
        r['E']--;
        r['N']--;
        ans.push_back(7);
    }
    
    //check nine
    while (r['I'] != 0) {
        r['N']--;
        r['I']--;
        r['N']--;
        r['E']--;
        ans.push_back(9);
    }
    
    //sort
    sort(ans.begin(), ans.end());
    
    //turn to string
    for (int i = 0; i < ans.size(); i++) {
        ss.push_back(ans[i]+'0');
    }
    return ss;
}


int main(int argc, const char * argv[]) {
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
            fout<<"Case #"<<i + 1<<": ";
            fout<<gtd(word)<<endl;
        }
    }
    else{
        cout<<"opend fail"<<endl;
    }
    
    return 0;
}
