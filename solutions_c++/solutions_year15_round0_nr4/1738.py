//
//  main.cpp
//  CodeJamProbD
//
//  Created by Mihai Visuian on 11/04/2015.
//  Copyright (c) 2015 Mihai Visuian. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("f.in");
ofstream fout("f.out");

int t,x,r,c;

int main(int argc, const char * argv[]) {

    fin>>t;
    
    for(int i = 1; i<=t; i++ ) {
        fin>>x>>r>>c;
        int xmin=(x+1)/2;
        if( r*c%x != 0 ) {
            fout << "Case #" << i << ": RICHARD\n";
            continue;
        }
        
        if( r<xmin || c<xmin ) {
            fout << "Case #" << i << ": RICHARD\n";
            continue;
        }
        
        if(x>r && x>c) {
            fout << "Case #" << i << ": RICHARD\n";
            continue;
        }
        
        if(x==4) {
            if(r==2 || c==2) {
                fout << "Case #" << i << ": RICHARD\n";
                continue;
            }
        }
        
        fout << "Case #" << i << ": GABRIEL\n";
    }
    
    fin.close();
    fout.close();
    return 0;
}
