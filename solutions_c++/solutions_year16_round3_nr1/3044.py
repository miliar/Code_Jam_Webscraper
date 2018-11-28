//
//  main.cpp
//  CodeJamR1P1
//
//  Created by Yanyan Tran on 2016-05-08.
//  Copyright © 2016 Yanyan Tran. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

int N, P, T, sens[26];

void solution()
{
    bool v, v2 = true;
    for (int a = 0; a < P; a++){
        
        for (int i = 0; i < N; i++){
            //cout <<sens[i];
            
            if (sens[i]-1 >= 0){
                sens[i]--;
                P--;
                
                //cout << "check0: "<< 'A' << sens[0] << " "<< 'B' << sens[1] << " " << 'C' << sens[2] << " "<< P << endl;
                
                v = true;
                
                for (int j = 0; j < N; j++){
                    //cout <<(double)(sens[j])/(P) << endl;
                    if ((double)(sens[j])/(P) > 0.5){
                        v = false;
                    }
                }
                
                for (int j = 0; j < N; j++){
                    
                    v2 = true;
                    if (sens[j] -1 >= 0){
                        
                        sens[j]--;
                        P--;
                        //cout << "check1: " << 'A' << sens[0] << " "<< 'B' << sens[1] << " " << 'C' << sens[2] << " " <<  P << endl;
                        
                        for (int k = 0; k < N; k++){
                            if ((double)(sens[k])/(P) > 0.5){
                                v2 = false;
                            }
                        }
                        //cout << v2 << endl;
                        
                        if (v2){
                            cout << (char)(j+'A');
                            break;
                        }else{
                            sens[j]++;
                            P++;
                        }
                        //cout << "check2: "<< 'A' << sens[0] << " "<< 'B' << sens[1] << " " << 'C' << sens[2] << " " <<  P << endl;
                        
                    }
                }
                
                if (!v && !v2){
                    sens[i]++;
                    P++;
                }
                if (v2){
                    cout << (char)(i+'A') << " ";
                }else if(v){
                    cout << (char)(i+'A') << " ";
                }
            }
            
        }
        
    }
}


int main() {
    //freopen("data.txt", "r", stdin);
    freopen("A-small-attempt2.in.txt", "r", stdin);
    freopen("OUT.txt", "w", stdout);
    
    cin >> T;
    for (int x = 1; x <= T; x++){
        P = 0;
        memset(sens, 0, sizeof sens);
        cin >> N;
        for (int i = 0; i < N; i++){
            cin >> sens[i];
            P += sens[i];
        }
        //cout << P << endl;
        
        cout << "Case #" << x << ": ";
        solution();
        cout << endl;
        
        
    }
    
    return 0;
}
