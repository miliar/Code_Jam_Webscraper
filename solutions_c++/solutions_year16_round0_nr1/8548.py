//
//  main.cpp
//  sheeps
//
//  Created by Dziugas Simaitis on 09/04/16.
//  Copyright © 2016 Dziugas Simaitis. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, const char * argv[]) {
    ifstream in("A-large.in");
    ofstream out("sheeps.out");
    
    int n;
    in>>n;
    for(int u=0; u<n; u++){
        bool win=false;
        int o=1;
        vector<int> reikia;
        for(int i=0; i<10; i++){
            reikia.push_back(i);
        }
        int skaicius1;
        in>>skaicius1;
        if(skaicius1==0){
            out<<"Case #"<<u+1<<": "<<"INSOMNIA"<<endl;
            win=true;
        }
        while(!win){
            int skaicius=skaicius1*o;
            string skaiciai = to_string(skaicius);
            for(int i=0; i<skaiciai.length(); i++){
                for(int y=0; y<reikia.size(); y++){
                    if(reikia[y]+'0'==skaiciai[i]){
                        reikia.erase(reikia.begin() + y);
                        y--;
                    }
                }
            }
            if(reikia.size()==0){
                out<<"Case #"<<u+1<<": "<<skaicius<<endl;
                win=true;
            }
            o++;
        }
    }
    return 0;
}
