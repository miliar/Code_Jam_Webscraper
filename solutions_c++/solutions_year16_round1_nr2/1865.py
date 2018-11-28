//
//  main.cpp
//  codejamr1
//
//  Created by Christiana on 16/4/15.
//  Copyright © 2016年 Christiana. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <map>
#include <unordered_map>

using namespace std;

string lastwordcalc(string str){
    string result;
    result = str[0];
    
    for(int i = 1; i < str.size(); ++i){
        if(str[i] >= result[0]){
            result = str[i] + result;
        }
        else{
            result = result + str[i];
        }
    }
    
    return result;
    
}

void lastword(){
    ifstream fin;
    ofstream fout;
    fin.open("/Users/christiana/Documents/workspace/leetcode/codejamr1/codejamr1/A-large.in");
    fout.open("/Users/christiana/Documents/workspace/leetcode/codejamr1/codejamr1/output-A-large.txt");
    int n;
    //cin>>n;
    fin>>n;
    string todo;
    for(int i = 0; i < n; ++i){
        //cin>> todo;
        fin>> todo;
        //cout <<"Case #" << i+1 << ": " <<lastwordcalc(todo) << endl;
        fout <<"Case #" << i+1 << ": " <<lastwordcalc(todo) << endl;

    }
}



void rankFile(){
    ifstream fin;
    ofstream fout;
    fin.open("/Users/christiana/Documents/workspace/leetcode/codejamr1/codejamr1/B-large.in");
    fout.open("/Users/christiana/Documents/workspace/leetcode/codejamr1/codejamr1/output-B-large.txt");
    int n;
    //cin>>n;
    fin>>n;
    //string todo;
    
    for(int i = 0; i < n; ++i){
        map<int, bool> peoplemap;
        //bool peoplemap[2600] = {false};
        int num;
        //cin>> num;
        fin>>num;
        int todo;
        for(int j = 0; j < num * num * 2 - num; ++j){
            //cin >> todo;
            fin>>todo;
            if(peoplemap[todo] == false){
                peoplemap[todo] = true;
            }
            else{
                peoplemap[todo] = false;
            }
        }
        
        //cout <<"Case #" << i+1 << ":";
        fout <<"Case #" << i+1 << ":";
        map<int, bool>::iterator iter;
        for(iter = peoplemap.begin(); iter != peoplemap.end();++iter){
        //for(int j = 0; j < 2500; ++j){
            if(iter->second){
            //if(peoplemap[j]){
                //cout << " " << iter->first;
                fout << " " << iter->first;
                //cout << j << endl;
            }
        }
        //cout << endl;
        fout << endl;
    }
    
    
}

int main(int argc, const char * argv[]) {
    // insert code here...
    //std::cout << "Hello, World!\n";
    
    //lastword();
    
    rankFile();
    
    return 0;
}
