
#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <fstream>
#include <iostream>


using namespace std;

int  A[4][4], B[4][4], a, b, mult=0;
bool valid = false;


int solve(int r, int s, int n)
{
    int c, D[4], E[4];
    
    for(int i=0; i<4; i++) {
        D[i] = A[r-1][i];
        //cout << D[i] << " d ";
    }
    //cout << endl;
       
    for(int i=0; i<4; i++) {
        E[i] = B[s-1][i];
        //cout << E[i] << " e ";
    }
    //cout << endl;
    
    
    for(int j=0; j<4; j++) {
        
        for(int k=0; k<4; k++) {
            
            if(D[j] == E[k]) {
                if(!valid) {
                    c = D[j];
                    valid = true;
                    mult++;
                    //cout << c << " asas"<<endl;
                }
                else {
                    mult++;
                }
                
            }
            
        }
        
    }
    
    if(valid) {
        if(mult==1) {
            cout << "Case #" << n << ": " << c << endl;
        }
        else {
            cout << "Case #" << n << ": Bad magician!" << endl;
        }
        valid = false;
        mult = 0;
    }
    else {
        cout << "Case #" << n << ": Volunteer cheated!" << endl;
    }
    
    
    
}


void takeInput()
{
    
    int i, j, n=0, x=0;
    cin >> i;
    
    while(i!=0) {

        if(x%2==0) cin >> a;
        else cin >> b;
        
        for(int k=0; k<4; k++) {
            for(int l=0; l<4; l++) {
                
                if(x%2==0) {
                    cin >> A[k][l];
                }
                else {
                    cin >> B[k][l];
                }
                
            }
            
        }
        
        if(x%2!=0) {
            n++;
            solve(a,b,n);
        }
        
        x++;
        
        if(x%2==0) i--;
    }
    
    
}



int main()
{
    
    takeInput();
    
    /*
    for(int k=0; k<4; k++) {
            for(int l=0; l<4; l++) {
                cout << A[k][l] << " ";
            }
            cout << endl;
    }
    
    for(int k=0; k<4; k++) {
            for(int l=0; l<4; l++) {
                cout << B[k][l] << " ";
            }
            cout << endl;
    }
    cout << a << " " << b << " ddedc" << endl;
    */
    
    return 0;
}