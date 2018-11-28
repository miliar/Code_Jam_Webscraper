//
//  2008prob2.cpp
//  
//
//  Created by srikar on 01/04/17.
//
//

#include <stdio.h>
//
//  main.cpp
//  dfd
//
//  Created by srikar on 28/03/17.
//  Copyright © 2017 srikar. All rights reserved.
//

#include <iostream>
#include <string>
#include <queue>
#include <unordered_set>
#include<limits.h>
#include <fstream>
#include <math.h>
#include <iomanip>
using namespace std;

int main() {
    int t;
    cin >> t;
    int l=1;
    ofstream myfile;
    myfile.open ("1stlarge.txt");
    while(t--){
        int k;
        string s;
        cin >> s >> k;
        int flips[s.length()];
        for(int i=0;i<s.length();i++){
            flips[i]=0;
        }
        int cou=0;
        for(int i=0;i<s.length();i++){
            if((s[i]=='+' && flips[i]%2==0) || (flips[i]%2==1 && s[i]=='-'))
                continue;
            if(i>s.length()-k){
                cou=-1;
                break;
            }
            cou++;
            for(int j=i;j<i+k;j++){
                flips[j]++;
            }
        }
        myfile << "Case #";
        myfile << l;
        myfile << ": ";
        if(cou!=-1)
            myfile << cou;
        else
            myfile << "IMPOSSIBLE";
        myfile << endl;
        l++;
        
    }
    return 0;
}
