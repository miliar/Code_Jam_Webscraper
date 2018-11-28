//
//  main.cpp
//  Lawnmower
//
//  Created by Sava Gerov on 13/04/13.
//  Copyright (c) 2013 Sava Gerov. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, const char * argv[])
{
    ifstream input;
    ofstream output;
    int nCases,N,M;
    input.open(argv[1]);
    output.open(argv[2]);
    input >> nCases;
    bool possible=true;
    
    for(int i=0;i<nCases;i++) {
        output << "Case #" << i+1 << ": ";
        input >> N;
        input >> M;
        int lawn[N][M];
        int maxRows[N];
        int maxCols[M];
        
        //introduce data in matrix
        for (int j=0; j<N; j++) {
            maxRows[j]=0;
            for (int k=0; k<M; k++) {
                maxCols[k]=0;
                input >> lawn[j][k];
            }
        }
        //Set max values
        for (int j=0; j<N; j++) {
            for (int k=0; k<M; k++) {
                if(lawn[j][k]>maxRows[j]) maxRows[j]=lawn[j][k];
            }
        }
        for (int j=0; j<M; j++) {
            for (int k=0; k<N; k++) {
                if(lawn[k][j]>maxCols[j]) maxCols[j]=lawn[k][j];
            }
        }
        
        //Check every value (could be more efficient)
        for (int j=0; j<N; j++) {
            for (int k=0; k<M; k++) {
                if ((lawn[j][k]<maxRows[j]) && (lawn[j][k]<maxCols[k])) {
                    possible=false; break;
                }
            }
            if (!possible) {
                break;
            }
            
        }
        
        if (possible) {
            output << "YES" << endl;
        } else output << "NO" << endl;
        possible=true;

    }
    return 0;
}

