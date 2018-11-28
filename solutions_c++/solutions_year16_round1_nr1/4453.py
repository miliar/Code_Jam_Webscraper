//
//  main.cpp
//  fr
//
//  Created by Pedro Abraham Moreno Vazquez on 15/04/16.
//  Copyright © 2016 Pedro Abraham Moreno Vazquez. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>

using namespace std;



string game(string ca){
    
    string nCad;
    nCad=nCad+ca[0];
    for (int i=1; i<ca.length(); i++) {
        if ((int)nCad[0]>(int)ca[i]) {
            nCad=nCad+ca[i];
        }
        else{
            nCad=ca[i]+nCad;
        }
    }
    return nCad;
}

int main(int argc, const char * argv[]) {
    
    int cases=0;
    
    cin>>cases;
    if (cases<0 || cases>100 ) {
        return 0;
    }
    vector<string>words;

    
    for (int i=0; i<cases; i++) {
        string aux;
        cin>>aux;
        words.push_back(aux);
        
    }
    
    
    for (int i=0; i<cases; i++) {
        
        if (words[i].length()>1000) {
            continue;
        }
     
         cout<<"Case #"<<i+1<<": "<<game(words[i])<<endl;
    }
   
  
    return 0;
}
