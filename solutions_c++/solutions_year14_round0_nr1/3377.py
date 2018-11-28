//
//  main.cpp
//  Qualification Round
//
//  Created by Ha Young Park on 4/12/14.
//  Copyright (c) 2014 Ha Young Park. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <set>
#include <iterator>
#include <algorithm>
#include <string>

using namespace std;

int main(int argc, const char * argv[])
{
    ifstream fin;
    ofstream fout;
    fin.open("A-small-attempt0.in");
    fout.open("A-small.out");
    int T;
    fin >> T;
    for(int i = 1; i <= T; i++){
        int nRow, nElem;
        int dummy;
        set<int> sCards;
        multiset<int> mCards;
        
        for(int l = 0; l < 2; l++){
            fin >> nRow;

            for(int j = 0; j < 4; j++){
                if(j == nRow - 1){
                    for(int k = 0; k < 4; k++){
                        fin >> nElem;
                        sCards.insert(nElem);
                        mCards.insert(nElem);
                    }

                }
                else{
                    fin >> dummy >> dummy >> dummy >> dummy;
                }
            }
        }
        
/*        fout << "Set: ";
        for(multiset<int>::iterator vIt = sCards.begin(); vIt != sCards.end(); vIt++){
            fout << *vIt << " ";
        }
        fout << endl;
        
        fout << "Multiset: ";
        for(multiset<int>::iterator vIt = mCards.begin(); vIt != mCards.end(); vIt++){
            fout << *vIt << " ";
        }
        fout << endl;
*/
        

        fout << "Case #" << i << ": ";
        if(sCards.size() == mCards.size())
            fout << "Volunteer cheated!";
        else if(sCards.size() == mCards.size() - 1){
            set<int>::iterator vIt;
            for(vIt = sCards.begin(); vIt != sCards.end(); vIt++){
                if(mCards.count(*vIt) == 2){
                    fout << *vIt;
                    break;
                }
            }
        }
        else
            fout << "Bad magician!";
        
        fout << endl;
    }
    
    fout.close();
    fin.close();
    return 0;
}

