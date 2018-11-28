//
//  main.cpp
//  rather_preplexing_showdown
//
//  Created by Matjaz Leonardis on 28/05/2016.
//  Copyright © 2016 Matjaz Leonardis. All rights reserved.
//

#include <stdio.h>
#include <string>

using namespace std;

int T;

string codes[3]={"P","R","S"};

string lexBestLineup(int rounds,int winner){
    
    if (rounds == 0) return codes[winner];
    
    string partLineup1 = lexBestLineup(rounds - 1, winner);
    string partLineup2 = lexBestLineup(rounds - 1, (winner + 1) % 3);
    
    if (partLineup1 < partLineup2) return partLineup1 + partLineup2; else return partLineup2 + partLineup1;
}

int main(int argc, const char * argv[]) {
    
    scanf("%d",&T);
    
    for (int caseNumber = 1; caseNumber <= T; caseNumber++){
        int N,P,R,S;
        scanf("%d %d %d %d",&N,&R,&P,&S);
        //Paper 0, Rock 1 , Scissors 2
        
        string answer = "Z";
        
        for (int i=0;i<3;i++){
            string candidate = lexBestLineup(N, i);
            int countP=0;
            int countR=0;
            int countS=0;
            for (int j=0;j<candidate.size();j++){
                if (candidate[j] == 'P') countP++;
                if (candidate[j] == 'R') countR++;
                if (candidate[j] == 'S') countS++;
            }
            if (countP != P) continue;
            if (countR != R) continue;
            if (countS != S) continue;
            
            if (candidate < answer) answer = candidate;
            
        }
        
        if (answer=="Z") answer = "IMPOSSIBLE";
        
        printf("Case #%d: %s\n",caseNumber,answer.c_str());
    
        
    }
    
    

    return 0;
}
