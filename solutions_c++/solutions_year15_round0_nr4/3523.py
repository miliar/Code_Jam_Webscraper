//
//  main.cpp
//  Omino
//
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

#define ADR "/Users/kisczio/Desktop/CodeJam/Omino/Omino/"

using namespace std;

int main(int argc, const char * argv[]) {
    freopen("" ADR "input.in", "rt", stdin);
    freopen("" ADR "output.in", "w", stdout);
    int T, X, R, C;
    string sol;
    cin >> T;
    
    
    
    for(int i=1; i<=T; i++){
        cin >> X;
        cin >> R;
        cin >> C;
        //cout << "X: " << X << " R: " << R << " C: " << C << endl;
        if(X==1){
            sol = "GABRIEL";
        }
        
        if(X==2){
            if(((R*C)%2)!=0){
                sol = "RICHARD";
            }
            else {
                sol = "GABRIEL";
            }
        }
        
        if(X==3){
            if(((R*C)%3)!=0){
                sol ="RICHARD";
            }
            else {
                if((R*C)==3){
                    sol ="RICHARD";
                }
                else {
                    sol ="GABRIEL";
                }
            }
        }
        
        if(X==4){
            if((R*C>=12)){
                sol ="GABRIEL";
            }
            else{
                sol="RICHARD";
            }
        }
        
        cout << "Case #" << i << ": " << sol << endl;
        
    }
}
