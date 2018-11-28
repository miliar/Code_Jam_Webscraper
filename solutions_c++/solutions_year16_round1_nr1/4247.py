//
//  main.cpp
//  R1-1
//
//  Created by 呂弈臻 on 2016/4/16.
//  Copyright (c) 2016年 henry. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;
#include <vector>

int main(int argc, const char * argv[]) {
    // insert code here...
    fstream input;
    input.open("011.txt");
    int number;
    string hold;
    getline(input,hold);
    number = stoi(hold);
    vector<string> all_string;
    while (getline(input,hold)) {
        all_string.push_back(hold);
    }
    ofstream output;
    output.open("result01.txt");
    for (int i=0; i<number; i++) {
        output << "Case #" << i+1 << ": ";
        vector<int> holder;
        holder.push_back((int)all_string[i][0]);
        int w = (int)all_string[i][0];
        for(int k=1; k<all_string[i].size();k++){
            vector<int>::iterator it;
            if((int)all_string[i][k]>=w){
                it = holder.begin();
                it = holder.insert(it,(int)all_string[i][k]);
                w = (int)all_string[i][k];
            }
            else{
                holder.push_back((int)all_string[i][k]);
            }
            
        }
        string a;
        for(int k=0;k<holder.size();k++)
            a += holder[k];
        output << a << endl;
    }
    
    
    return 0;
}
