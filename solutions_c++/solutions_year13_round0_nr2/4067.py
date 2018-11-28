//
//  main.cpp
//  LM
//
//  Created by jiusi on 4/13/13.
//  Copyright (c) 2013 jiusi. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;


int main(int argc, const char * argv[])
{
    ifstream cin("/Users/jiusi/Downloads/B-large.in");
    ofstream cout("/Users/jiusi/workspace-cv/LM/LM/re.out");
    int n;
    cin >> n;
    int count = 0;
    for(int c = 0; c < n ; c++) {
        int rl;
        int cl;
        cin >> rl >> cl;
        int ma[100][100];
        
        for(int i = 0; i < rl; i++) {
            for(int j= 0; j < cl; j++) {
                cin >> ma[i][j];
            }
        }
        
        int mc[100][100];
        for(int i = 0; i< 100; i++) {
            fill_n(mc[i], 100, 100);
        }
        
        for(int i = 0; i < max(rl, cl); i++) {
            int max_h = 0;
            for(int j = 0; j < rl; j++) if(i < cl){
                if(ma[j][i] > max_h) {
                    max_h = ma[j][i];
                }
            }
            for(int j = 0; j < rl; j++) if(i < cl){
                if(mc[j][i] > max_h) {
                    mc[j][i] = max_h;
                }
            }
            
            max_h = 0;
            for(int j = 0; j < cl; j++) if(i < rl){
                if(ma[i][j] > max_h) {
                    max_h = ma[i][j];
                }
            }
            for(int j=0; j < cl; j++) if(i < rl){
                if(mc[i][j] > max_h){
                    mc[i][j] = max_h;
                }
            }
        }
        
        bool fail = false;
        for(int i = 0; i<rl; i++){
            for(int j=0; j<cl; j++) {
                if(ma[i][j] != mc[i][j]) {
                    fail = true;
                    goto fin;
                }
            }
        }
    
    fin:
        if(fail ) {
            cout << "Case #" << ++count << ": NO" << endl;
        } else {
            cout << "Case #" << ++count << ": YES" << endl;
        }
        

        
    }
    
    return 0;
}

