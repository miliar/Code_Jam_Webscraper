//
//  main.cpp
//  codejam
//
//  Created by Stephen Zhu on 4/11/14.
//  Copyright (c) 2014 Stephen Zhu. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

#define tr(i, end) \
for (int i = 0; i < end; ++i)

int gameboard[4][4];

int main()
{
    
    ifstream ins("A-small-attempt0.in");
    FILE * out;
    out = fopen("A-small-attempt0.out", "w");
    int T;
    
    ins >> T;    
    tr(numcase, T){
        
        fprintf(out, "Case #%i: ", numcase+1);
        int potentials[4];
        int row1, row2;
        bool cheated = false;
        ins >> row1;
        --row1;
        tr(i, 4){
            tr(j, 4){
                ins >> gameboard[i][j];
            }
        }
        
        
        tr(i, 4){
            potentials[i] = gameboard[row1][i];
        }
        
        ins >> row2;
        --row2;
        tr(i, 4){
            tr(j, 4){
                ins >> gameboard[i][j];
            }
        }
        
        int card = -1;
        tr(i, 4){
            tr (j, 4){
                if (gameboard[row2][i] == potentials[j]){
                    if (card == -1) card = potentials[j];
                    else {
                        fprintf(out,"Bad magician!\n");
                        cheated = true;
                        break;
                    }
                }
                if (cheated) break;
            }
            if (cheated) break;
        }
        
        if (card == -1) fprintf(out, "Volunteer cheated!\n");
        else if (!cheated) fprintf(out, "%i\n", card);
        
    }
    
    
    return 0;
}



