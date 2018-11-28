//
//  main.cpp
//  codejamr1
//
//  Created by Christiana on 16/4/15.
//  Copyright © 2016年 Christiana. All rights reserved.
//

#include <iostream>
#include <fstream>

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

int main(int argc, const char * argv[]) {
    // insert code here...
    //std::cout << "Hello, World!\n";
    
    lastword();
    
    
    return 0;
}
