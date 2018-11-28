//
//  main.cpp
//  projB
//
//  Created by Stephen Zhu on 4/13/13.
//  Copyright 2013 University of Michigan. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

int board[100][100];

int N, M;

bool isGood(int x, int y){
    bool g = true;
    
    for ( int i = 0; i < M; i++){
        if (board[x][i] > board[x][y]){
            g = false;
            break;
        }
    }
    if (g){
        return true;
    }
    
    for (int i = 0; i < N; i++){
        if( board[i][y] > board[x][y]){
            return false;
        }
    }
    
    return true;
    
}



int main ()
{

    int T;
    
    int round = 1;
    
    ifstream in("test.txt");
    ofstream out("projB.out");
    
    in >> T;
    
    
    while ( round <= T ){
        in >> N >> M;
        bool good = true;
        for (int i = 0; i < N; i++){
            for ( int j = 0; j < M; j++){
                in >> board[i][j];
            }
        }
        for (int i = 0; i < N; i++){
            for ( int j = 0; j < M; j++){
                if (!isGood(i, j)){
                    good = false;
                    break;
                }
            }
        }
        
        if (good){
            out << "Case #" << round << ": YES\n";
        }
        else 
            out << "Case #" << round << ": NO\n";
        round++;
    }
    
    return 0;
}

