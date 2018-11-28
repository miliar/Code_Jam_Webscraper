//
//  QualA.cpp
//  CodeJam_Qualification
//
//  Created by Matej Hamas on 11/04/2015.
//  Copyright (c) 2015 Matej Hamas. All rights reserved.
//

#include "QualA.h"

using namespace std;

void solveQualA() {
    
    string name = "A-large";
    stringstream ssIn, ssOut;
    ssIn << "./" << name << ".in";
    ssOut << "./" << name << ".out";
    ifstream input;
    input.open(ssIn.str());
    ofstream output;
    output.open(ssOut.str());
    
    int T;
    
    input >> T;
    
    for (int k = 0; k < T; k++) {
        int S;
        input >> S;
        //cout << S << endl;
        int standing = 0;
        int toAdd = 0;
        
        for (int j = 0; j <= S; j++) {
            char c;
            input >> c;
            
            int x = (int)c - 48;
            
            //cout << x << ";";
            if (standing > j) {
                standing += x;
            } else {
                toAdd += j - standing;
                standing = j + x;
            }
        }
        //cout << endl;
        
        cout << "Case #"<<k+1 << ": " << toAdd << endl;
        output << "Case #"<<k+1 << ": " << toAdd << endl;
    }
    
    input.close();
    output.close();
    
    
}
