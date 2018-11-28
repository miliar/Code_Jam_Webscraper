//
//  main.cpp
//  Google Code Jam Qualification Round 1
//
//  Created by Chunjing Jia on 4/11/14.
//  Copyright (c) 2013 Chunjing Jia. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <set>
#include <iomanip>

using namespace::std;

int main(int argc, const char * argv[])
{
    int nums;
    ifstream myfile("/Users/cjjia/Documents/Work/Google Code Jam/Qualification Round 4 Ken/CloneGraph/D-large.in");

    //cout.setf(ios::fixed);
    myfile >> nums;
    for(int num=0; num<nums; num++){
        //cout << num+1;
        int blocks;
        myfile >> blocks;
        vector<double> Naomi(blocks,0);
        vector<double> Ken(blocks,0);
        for(int i=0; i<blocks; i++) myfile >> Naomi[i];
        for(int i=0; i<blocks; i++) myfile >> Ken[i];
        sort(Naomi.begin(), Naomi.end());
        sort(Ken.begin(), Ken.end());
        //cout << num+1;
        
        int Res1 = 0, Res2 = 0;
        int Ks = 0, Ke = blocks-1;
        for(int Ni=0; Ni<blocks; Ni++){
            if(Naomi[Ni] > Ken[Ks]){
                Res2++;
                Ks++;
            } else {
                Ke--;
            }
        }
        
        int Ki = 0;
        for(int Ni=0; Ni<blocks; Ni++){
            while(Ki < Ken.size() && Naomi[Ni] > Ken[Ki]) Ki++;
            if(Ki < Ken.size()) {
                Ken.erase(Ken.begin()+Ki);
            } else {
                Ken.erase(Ken.begin());
                Res1++;
            }
        }
        

        
        cout << "Case #" << num+1 << ": " << Res2 << " " << Res1 << endl;
    }
    return 0;
}


