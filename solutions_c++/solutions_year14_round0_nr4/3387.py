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
    int size;
    
    ifstream ifile;
    ofstream ofile;
    
    
    
    ifile.open("/Users/marvinteichmann/Dropbox/projekte/input/input");
    ofile.open("/Users/marvinteichmann/Dropbox/projekte/output");

    cout.precision(12);
    ofile.precision(12);
    
    //inputfile.open("./A-small-practice.in");
    if(ifile.is_open()) {
        ifile>>cases;
        for(int k = 0; k < cases; ++k){
            cout << "\nCase: " << k+1 << "\n";
            
            ifile >> size;
            getline(ifile,line);
            getline(ifile,line);
            stringstream tok(line);
            
            vector<double> naomi(size);
            vector<double> ken(size);
            for(int i = 0; i < size; ++i) {
                tok >> naomi[i];
            }
            getline(ifile,line);
            stringstream tok2(line);
            for(int i = 0; i < size; ++i) {
                tok2 >> ken[i];
            }
            
            sort(naomi.begin(), naomi.end());
            sort(ken.begin(), ken.end());
            
            stringstream out;
            out.precision(12);
            
            int it = 0;
            bool flag = true;
            while(flag){
                flag = false;
                for(int i = it; i < size; ++i){
                    if(naomi[i] < ken[i-it]) {
                        flag = true;
                        break;
                    }
                }
                it++;
            }
            it--;
            
            out << size - it << " ";
            
            int pointer = 0;
            it = 0;
            while(pointer <= size) {
                while(pointer < size && ken[pointer] < naomi[it]) {
                    pointer++;
                }
                ++it;
                ++pointer;
            }
            --it;

            
            out << size - it << " ";

            string output = out.str();
            
            
            ofile << "Case #" << k+1 << ": " << output   << "\n";
            cout << "Case #" << k+1 << ": " << output  << "\n";
        }
        
        
    }else{
        cout << "fail";
    }
    
    ifile.close();
    ofile.close();
    return 0;
}




