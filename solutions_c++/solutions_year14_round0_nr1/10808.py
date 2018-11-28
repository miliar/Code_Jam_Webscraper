//
//  magic.cpp
//  
//
//  Created by Alicia Sun on 4/12/14.
//
//

#include "magic.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

int main(int argc,char *argv[]){
    ifstream ifs;
    ifs.open(argv[1]);
    vector<int> square1;
    vector<int> square2;
    string line;
    string case;
    int casenum;
    string word;
    string first;
    string second;
    getline(ifs,line);
    istringstream iss(line);
    iss>>case;
    casenum=stoi(case);
    int count;
    while(int k=1;k<=casenum;k++){
        count=0;
        check(k,ifs);
        
    }
    
}


int check(int case,istringstream ifs){
    getline(ifs,line);
    istringstream iss(line);
    iss>>first;
    for(int i=1;i<first;i++){
        getline(ifs,line);
    }
    getline(ifs,line);
    istringstream iss(line);
    while(iss>>word){
        square1.push_back(stoi(word));
    }
    for(int j=0;j<4-first;j++){
        getline(ifs.line);
    }
    getline(ifs,line);
    istringstream iss(line);
    iss>>second;
    for(int i=1;i<second;i++){
        getline(ifs,line);
    }
    getline(ifs,line);
    istringstream iss(line);
    while(iss>>word){
        square2.push_back(stoi(word));
    }
    for(int j=0;j<4-second;j++){
        getline(ifs.line);
    }
    //compare
    for(int i=(case-1)*4;i<=case*4-1;i++){
        for(int j=(case-1)*4;j<=case*4-1;j++){
            if(square1[i]=square2[j]){
                count++;
            }
        }
    }
    if(count==0){
        cout<<"Case #"<<case<<": "<<"Volunteer cheated!"<<endl;
    }
    else if(count==1){
        for(int i=(case-1)*4;i<=case*4-1;i++){
            for(int j=(case-1)*4;j<=case*4-1;j++){
                if(square1[i]=square2[j]){
                    "Case #"<<case<<": "<<square1[i]<<endl;
                }
            }
        }
    }
    else{
        cout<<"Case #"<<case<<": "<<"Bad magician!"<<endl;
    }
}



    

    

