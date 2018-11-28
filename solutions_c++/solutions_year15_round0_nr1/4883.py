//
//  main.cpp
//  codejam_1
//
//  Created by Hasan Unlu on 11/04/15.
//  Copyright (c) 2015 Hasan Unlu. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

int main(int argc, const char * argv[]) {
    
    string line;
    
    ifstream infile ("/Users/hasanunlu/Desktop/codejam_1/codejam_1/input.txt");
    ofstream outfile ("/Users/hasanunlu/Desktop/codejam_1/codejam_1/output.txt");
    
    if (!infile.is_open())
        cout << "Unable to open file";
    
    int T,Smax;
    getline (infile,line);
    
    T=atoi(line.c_str());
    
    cout << T << endl;
    
    for(int i=0; i<T; i++){
        getline (infile,line);

        char *input = const_cast<char*>(line.c_str());
        
        char *token = strtok(input, " ");
        
        Smax=atoi(token);
        
        cout <<"Smax="<<Smax<< endl;
        token = strtok(NULL, " ");
        
        int sum=0;
        int diff=0;
        
        for(int S=0; S<=Smax; S++){
            
            int value=(*token++)-48;
            
            cout<<value<<endl;
            

            
            if(sum>=S){
            
            } else {
              
                diff=diff+S-sum;
                sum=S;
                
                cout<<"diff="<<diff<<endl;
            }
            
            sum=sum+value;
            
            
        }
        
        cout<<   "Case #"<<i+1<<": "<<diff<<endl;
        outfile<<"Case #"<<i+1<<": "<<diff<<endl;
        
        cout<<"*******"<<endl;
        
        
        
    }
    
    
    infile.close();
    
    outfile.close();
    
    
    
    return 0;
}
