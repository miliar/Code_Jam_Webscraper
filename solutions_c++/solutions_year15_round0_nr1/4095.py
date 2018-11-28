//
//  main.cpp
//  GCJA
//
//  Created by Nathaniel Faulkner on 11/04/15.
//  Copyright (c) 2015 Nathaniel Faulkner. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>

using namespace std;

int N,sMax,tot,extras;
string peopleLevels;

int main(int argc, const char * argv[]) {
    if (argc<2){
        cout<<"Needs input and output flags!";
        exit(EXIT_FAILURE);
    }
    
    string temp;
    
    ifstream fin(argv[1]);
    if(!fin.is_open())
    {
        cout<<"Unable to open input file"<<endl;
        cout<<argv[1];
        exit(EXIT_FAILURE);
    }
    
    ofstream fout(argv[2]);
    
    getline(fin,temp);
    N = atoi(temp.c_str());
    
    cout<<N<<" test cases following"<<endl;
    
    for(int i =0; i<N; i++){
        tot=0;
        extras = 0;
        getline(fin,temp);
        stringstream  tempstream(temp);
        tempstream >> sMax;
        tempstream >> peopleLevels;
        
        for(int jj = 0; jj<sMax+1; jj++){
            if (tot<jj){
                extras+=jj-tot;
                tot = jj;
            }
            
            tot+=peopleLevels[jj]-'0';
        }
        
        fout<<"Case #"<<i+1<<": "<<extras<<endl;
        
        
        
        //c = atoi(temp.c_str());
        
        
        /*
        getline(fin,temp);
        l = atoi(temp.c_str());
        cout<<"Number "<<i<<": credit - "<<c<<", number items - "<<l<<endl;
        getline(fin,temp);
        
        stringstream  tempstream(temp);
        int *tempArray = new int[l];
        for(int j = 0; j<l;j++){
             tempArray[j];
            //cout<<tempArray[j]<<" item number "<<j<<endl;
        }
        //code here
        
        for(int ii = 0;ii<l-1;ii++){
            for(int jj=ii+1;jj<l;jj++){
                if (tempArray[ii]+tempArray[jj] == c){
                    fout<<"Case #"<<i+1<<": "<<ii+1<<" "<<jj+1<<endl;
                    break;
                }
                
            }
        }
        
        delete [] tempArray;
         
         */
     
    }
    
    
    fin.close();
    fout.close();
    
    return 0;
}
