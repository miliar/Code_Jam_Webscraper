//
//  main.cpp
//  Getting the Digits
//
//  Created by Jeremy Wong on 1/5/2016.
//  Copyright © 2016 Jeremy Wong. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <vector>


using namespace std;

int main() {


    int numOfInput;
    cin >> numOfInput;
    
    for (int k=0; k<numOfInput; k++){
        
        
        vector<int> vec;
        
        int E = 0;
        int F = 0;
        int G = 0;
        int H = 0;
        int I = 0;
        int N = 0;
        int O = 0;
        int R = 0;
        int S = 0;
        int T = 0;
        int V = 0;
        int X = 0;
        int Z = 0;
        int W = 0;
        
        string input;
        cin >> input;
        
        
        for (int j=0; j<input.length(); j++){
            
            switch (input.at(j)){
                
                case 'Z':
                    Z ++;
                    break;
                case 'E':
                    E++;
                    break;
                case 'F':
                    F++;
                    break;
                case 'G':
                    G++;
                    break;
                case 'H':
                    H++;
                    break;
                case 'I':
                    I++;
                    break;
                case 'N':
                    N++;
                    break;
                case 'O':
                    O++;
                    break;
                case 'R':
                    R++;
                    break;
                case 'S':
                    S++;
                    break;
                case 'T':
                    T++;
                    break;
                case 'V':
                    V++;
                    break;
                case 'X':
                    X++;
                    break;
                case 'W':
                    W++;
                    break;
                    
                default:
                    break;
                
            }
        }
        
        for (int j=0; j<G; j++){
            
            vec.push_back(8);
        }
        E -= G;
        I -= G;
        H -= G;
        T -= G;
        G -= G;
        for (int j=0; j<W; j++){
            
            vec.push_back(2);
        }
        T -= W;
        O -= W;
        W -= W;
        
        
        for (int j=0; j<Z; j++){
            
            vec.push_back(0);
        }
        
        
        E -= Z;
        R -= Z;
        O -= Z;
        Z -= Z;
        
        for (int j=0; j<X; j++){
            
            vec.push_back(6);
            
        }
        
        S -= X;
        I -= X;
        X -= X;
        
        
        for (int j=0; j<S; j++){
            
            vec.push_back(7);
            
        }
        
        N -= S;
        E -= S;
        V -= S;
        E -= S;
        S -= S;
        
        
        for (int j=0; j<V; j++){
            
            vec.push_back(5);
            
        }
        
        F -= V;
        I -= V;
        E -= V;
        V -= V;
        
        for (int j=0; j<F; j++){
            

            vec.push_back(4);
            
        }
        
        R -=F;
        O -=F;
        F -=F;
        
        
        for (int j=0; j<O; j++){
            
            vec.push_back(1);
            
        }
        
        E -= O;
        N -= O;
        O -= O;
        
        for (int j=0; j<T; j++){
            

            vec.push_back(3);
        }
        
        E -= T;
        E -=T;
        H -=T;
        R -=T;
        T -= T;
        
        
        for (int j=0; j<E; j++){
            
            vec.push_back(9);
        }
        
        
        
        
        sort(vec.begin(), vec.end());
        vector<int>::iterator iter;
        
        int index = k+1;
        cout << "Case #" + to_string(index) << ": ";
        
        
        
        for (iter = vec.begin(); iter!=vec.end(); iter++){
            cout << *iter;
        }
        cout << endl;
    }
    
    
    
    return 0;
    
    
}
