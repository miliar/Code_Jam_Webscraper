//
//  main.cpp
//  02
//
//  Created by 呂弈臻 on 2016/4/9.
//  Copyright (c) 2016年 henry. All rights reserved.
//

#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <set>
using namespace std;

int main(int argc, const char * argv[]) {
    vector<string> sig;
    ifstream input;
    input.open("02.txt");
    int number;
    string hold;
    getline(input,hold);
    number = stoi(hold);
    int counter = 0;
    ofstream output;
    output.open("result2.txt");
    while(getline(input,hold)){
        sig.push_back(hold);
    }
    for(int i=0;i<number;i++){
        output << "Case #" << i+1 << ": ";
        if(sig[i][sig[i].length()-1]=='-'){
            sig[i] += '+';
        }
        for (int k=0; k<sig[i].length(); k++) {
            if((sig[i][k]!=sig[i][k+1]) && (k!=sig[i].length()-1))
                counter++;
        }
        output << counter << endl;
        counter = 0;
    }
    return 0;
}
