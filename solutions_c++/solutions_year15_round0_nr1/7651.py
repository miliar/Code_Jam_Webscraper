//
//  Q-A.cpp
//  CodeJam2015
//
//  Created by Ha Young Park on 4/11/15.
//  Copyright (c) 2015 Ha Young Park. All rights reserved.
//

#include <fstream>
#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    ifstream fin;ofstream fout;fin.open("A-large.in");fout.open("A-large.out");

    int T;
    fin >> T;

    for(int i = 0; i < T; i++){
        int Smax;
        fin >> Smax;
        
        char* S = new char[Smax + 2];
        fin >> S;

        int ovation = 0;
        int invitation = 0;

        for(int j = 0; j <= Smax; j++){
            
            if(S[j] > '0'){
                if(j > ovation){
                    invitation += j - ovation;
                    ovation += j - ovation;
                }
            }
            ovation += S[j] - '0';
            
        }
        fout << "Case #" << i + 1 << ": " << invitation << endl;
    }

    fout.close();fin.close();
    
    return 0;
}
