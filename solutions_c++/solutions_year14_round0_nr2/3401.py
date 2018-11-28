//
//  B-main.cpp
//  Qualification Round
//
//  Created by Ha Young Park on 4/12/14.
//  Copyright (c) 2014 Ha Young Park. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <set>
#include <iterator>
#include <algorithm>
#include <string>

using namespace std;

int main(int argc, const char * argv[])
{
    ifstream fin;
    ofstream fout;
    fin.open("B-large.in");
    fout.open("B-large.out");
    int T;
    fin >> T;
    for(int i = 1; i <= T; i++){
        double C, F, X, dElapsed = 0.0, dProduce = 2.0;
        
        fin >> C >> F >> X;
        fout.precision(7);
        fout.setf(ios::fixed, ios::floatfield);

        if( C < X ){
            //Initial
            dElapsed = C / dProduce;
                
            while((X - C) / dProduce > X/(dProduce + F)){
                dProduce += F;
                dElapsed += C / dProduce;
                
            }
            dElapsed += (X - C) / dProduce;
        }
        else
            dElapsed = X / dProduce;
        
        

        fout << "Case #" << i << ": " << dElapsed << endl;
        
    }
    return 0;
}