//
//  File.cpp
//  Qualification Round
//
//  Created by Ha Young Park on 4/12/14.
//  Copyright (c) 2014 Ha Young Park. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <iterator>
#include <algorithm>
#include <string>

using namespace std;

int main(int argc, const char * argv[])
{
    ifstream fin;
    ofstream fout;
    fin.open("D-large.in");
    fout.open("D-large.out");
    int T;
    fin >> T;
    for(int i = 1; i <= T; i++){
        int nBlocks;
        fin >> nBlocks;
        
        vector<double> vNaomi, vKen, vKenCopy;
        double dWeight;
        
        for(int j = 0; j < nBlocks; j++){
            fin >> dWeight;
            vNaomi.push_back(dWeight);
        }
        sort(vNaomi.begin(), vNaomi.end());
        reverse(vNaomi.begin(), vNaomi.end());
        
        for(int j = 0; j < nBlocks; j++){
            fin >> dWeight;
            vKen.push_back(dWeight);
        }
        sort(vKen.begin(), vKen.end());
        reverse(vKen.begin(), vKen.end());
        vKenCopy = vKen;
        
        for_each(vNaomi.begin(), vNaomi.end(), [](double elem){
            cout << elem << ' ';
        });
        cout << endl;
        for_each(vKen.begin(), vKen.end(), [](double elem){
            cout << elem << ' ';
        });
        cout << endl << endl;
        
        
        //War
        vector<double>::iterator itNaomi = vNaomi.begin();
        vector<double>::iterator itKen   = vKen.begin();
        
        while(itNaomi != vNaomi.end() && itKen != vKen.end()){
            
            if(*itKen < *itNaomi)
                vKen.pop_back();
            else
                itKen++;
            itNaomi++;
        }
        
        //Deceitful War
        itNaomi = vNaomi.begin();
        itKen = vKenCopy.begin();

        while(itNaomi != vNaomi.end() && itKen != vKenCopy.end()){
            
            if(*itNaomi < *itKen)
                vNaomi.pop_back();
            else
                itNaomi++;
            itKen++;
        }
        
        fout << "Case #" << i << ": " << vNaomi.size() << " " << nBlocks - vKen.size() << endl;
        
    }
    return 0;
}
