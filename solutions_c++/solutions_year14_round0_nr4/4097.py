//
//  main.cpp
//  CodeJam - Deceitful War
//
//  Created by Administrator on 4/12/14.
//  Copyright (c) 2014 Ryan. All rights reserved.
//

#include <iostream>
#include <functional>
#include <set>

using namespace std;

int main(int argc, const char * argv[])
{
    set<double> massesKen;
    set<double> massesKenWar;
    set<double> massesNaomi;
    set<double> massesNaomiWar;
    
    int numCases;
    cin >> numCases;
    
    int numBlocks;
    double mass;
    int caseCounter = 1;
    int winsDeceitfulWar = 0;
    int winsWar = 0;
    
    while (cin >> numBlocks) {
        for (int i = 0; i < numBlocks; i++) {
            cin >> mass;
            massesNaomi.insert(mass);
            massesNaomiWar.insert(mass);
        }
        for (int i2 = 0; i2 < numBlocks; i2++) {
            cin >> mass;
            massesKen.insert(mass);
            massesKenWar.insert(mass);
        }
        
        //Optimal Deceitful War--------------------------------------------------
        for (int b = 0; b < numBlocks; b++) {
            if (*massesNaomi.begin() > *massesKen.begin()) {
                massesNaomi.erase(*massesNaomi.begin());
                massesKen.erase(*massesKen.begin());
                winsDeceitfulWar++;
                continue;
            }
            massesNaomi.erase(*massesNaomi.begin());
            massesKen.erase(*massesKen.rbegin());
        }
        //End Optimal Deceitful War----------------------------------------------
        
        
        //Optimal War------------------------------------------------------------
        for (int a = 0; a < numBlocks; a++) {
            if (*massesNaomiWar.rbegin() > *massesKenWar.rbegin()) {
                winsWar++;
                massesNaomiWar.erase(*massesNaomiWar.rbegin());
                massesKenWar.erase(*massesKenWar.begin());
            }
            else {
                massesNaomiWar.erase(*massesNaomiWar.rbegin());
                massesKenWar.erase(*massesKenWar.rbegin());
            }
        }
        //End Optimal War--------------------------------------------------------
        
        cout << "Case #" << caseCounter << ": " << winsDeceitfulWar << " " << winsWar << "\n";
        caseCounter++;
        winsDeceitfulWar = 0;
        winsWar = 0;
        massesKen.clear();
        massesKenWar.clear();
        massesNaomi.clear();
        massesNaomiWar.clear();
    }
    
    
    return 0;
}
