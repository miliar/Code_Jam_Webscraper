//
//  main.cpp
//  CodejamP1
//
//  Created by swati agrawal on 4/11/15.
//  Copyright (c) 2015 home. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;
#define OUTPUTFILE

ofstream myfile;
void process(int T){
    
    int smax;
    string shyness;
    cin >> smax;
    cin >> shyness;
    
    int standing = 0, friends = 0;
    for(int i = 0; i <= smax; i++){
        char c = shyness[i];
        int n = c - '0';
        if(standing < i){
            int diff = i - standing;
            friends += diff;
            standing += diff;
        }
        standing += n;
    }
    cout << "Case #" << T << ": " << friends << endl;
    
#ifdef OUTPUTFILE
    myfile << "Case #" << T << ": " << friends << endl;
#endif
    
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int T;
#ifdef OUTPUTFILE
    myfile.open("/Users/swatideepakagrawal/work/workspace/Samples/CodejamP1/output.txt");
#endif
    
    cin >> T;
    for(int i = 1; i <= T; i++)
        process(i);
    
#ifdef OUTPUTFILE
    myfile.close();
#endif
    return 0;
}
