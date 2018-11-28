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
    
    //inputfile.open("./A-small-practice.in");
    if(ifile.is_open()) {
        ifile>>cases;
        for(int k = 0; k < cases; ++k){
            //cout << "\n Case: " << k << "\n";
            ifile>>row;
            vector<int> x(size);
            
            getline(ifile,line);
            getline(ifile,line);
            for(int i = 1; i < row; ++i){
                getline(ifile,line);
            }
            
            stringstream tok(line);
            for(int i = 0; i < size; ++i){
                tok>>x[i];
            }
            
            for(int i = row; i < size; ++i){
                getline(ifile,line);
            }
            ifile>>row;
            vector<int> y(size);
            
            getline(ifile,line);
            getline(ifile,line);
            
            for(int i = 1; i < row; ++i){
                getline(ifile,line);
            }

            
            stringstream tok2(line);
            for(int i = 0; i < size; ++i){
                tok2>>y[i];
            }
            
            for(int i = row; i < size; ++i){
                getline(ifile,line);
            }

            sort(x.begin(),x.begin()+size);
            sort(y.begin(),y.begin()+size);
            
 
            cout << std::endl;
            

            
            cout << endl;
            
            vector<int> result(size);
            auto it=std::set_intersection (x.begin(), x.begin()+size, y.begin(), y.begin()+size, result.begin());
            result.resize(it-result.begin());
            
            
            
            string output;
            
            switch(result.size()) {
                case 0: output = "Volunteer cheated!";
                    break;
                case 1: output = std::to_string(result[0]);
                    break;
                default: output = "Bad magician!";
            }
            
            
     
            ofile << "Case #" << k+1 << ": " << output   << "\n";
            if(k < 3){
                cout << "Case #" << k+1 << ": " << output  << "\n";
            }
        }
        
        
    }else{
        cout << "fail";
    }
    
    ifile.close();
    ofile.close();
    return 0;
}




