//
//  test.cpp
//  
//
//  Created by DHEERAJ on 3/31/15.
//
//

#include <stdio.h>
#include<iostream>
#include<string>
#include<algorithm>
#include<sstream>
#include<fstream>
using namespace std;

int main(){
    ifstream input("/Users/dheeraj/Downloads/A-large.in");
    ofstream output_file("/Users/dheeraj/Desktop/A-large.out");
    string line;
    getline(input,line);
    int test_cases = stoi(line);
    for(size_t i=0;i<test_cases;++i){
        int output = 0;
        string Smax,shyness;
        getline(input,line);
        stringstream ss(line);
        ss>>Smax>>shyness;
        size_t j = 0;
        int curr_aud_count = stoi(string(1,shyness[j]));
        for(j = 1;j<shyness.size();j++){
            if(curr_aud_count < j){
                output += (j-curr_aud_count);
                curr_aud_count +=(j-curr_aud_count);
            }
            curr_aud_count+=(stoi(string(1,shyness[j])));
        }
        output_file<<"Case #"<<i+1<<": "<<output<<endl;
    }
}