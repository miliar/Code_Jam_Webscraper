//
//  main.cpp
//  hello
//
//  Created by Marvin Teichmann on 12.04.14.
//  Copyright (c) 2014 mteichmann. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

int main(int argc, const char * argv[])
{
    
    string line;
    int cases;
    int row;
    
    ifstream ifile;
    ofstream ofile;
    
    ifile.open("/Users/marvinteichmann/Dropbox/projekte/input/input");
    ofile.open("/Users/marvinteichmann/Dropbox/projekte/output");
    
    int size = 4;
    
    double C;
    double F;
    double X;
    
    double max_time = numeric_limits<int>::max();
    
    int start_rate = 2;
    
    cout.precision(12);
    ofile.precision(12);
    
    //inputfile.open("./A-small-practice.in");
    if(ifile.is_open()) {
        ifile>>cases;
        getline(ifile,line);
        for(int k = 0; k < cases; ++k){
            cout << "\nCase: " << k+1 << "\n";
            
            getline(ifile,line);
            stringstream tok(line);
            cout << line << endl;
            
            tok >> C;
            tok >> F;
            tok >> X;
            
            double current_rate = start_rate;
            double current_time = 0;
            double best_time = max_time*3;
            double estimated_time = max_time*2;
            while(estimated_time < best_time) {
                best_time = estimated_time;
                estimated_time = current_time + X/current_rate;
                
                current_time = current_time + C/current_rate;
                current_rate = current_rate + F;
            }
            cout << "time: " << best_time << endl;


            stringstream out;
            out.precision(12);
            
            out << best_time;
            string output = out.str();
            
            
            ofile << "Case #" << k+1 << ": " << output   << "\n";
            if(k < 3){
               // cout << "Case #" << k+1 << ": " << output  << "\n";
            }
        }
        
        
    }else{
        cout << "fail";
    }
    
    ifile.close();
    ofile.close();
    return 0;
}




