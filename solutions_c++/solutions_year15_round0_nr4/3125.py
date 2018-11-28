#include <iostream>
#include <map>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
#include <queue>
#include <set>
#include <string.h>
#include <iomanip>
#include <stdio.h>
#include <ctype.h>
#include <bitset>

//#pragma comment (linker, "/STACK:167177216")
//-Wl, --stack=

using namespace std;
#define mp(a, b)  make_pair(a, b);

bool testBit(int &mask, int bit){
    return (mask & (1 << bit));
}
void setBit(int &mask, int bit){
    mask = mask | (1 << bit);
}
void resetBit(int &mask, int bit){
    mask = mask & (~ (1 << bit));
}

int main(int argc, const char * argv[])
{
    ///////////////Conect File////////////////////////
    for(int i = 0; i < argc; i++){
        if((string)argv[i] == "viLap"){
            freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
        }
    }
    ///////////////////////////////////////////////////
    //  freopen("j3.in", "r", stdin);freopen("j3.out", "w", stdout);
    
    int T;
    cin >> T;
    for(int i = 1; i <=T; i++){
        int ans = 0;
        int x, r, c;
        cin >> x >> r >> c;
      //  cout <<x<<" "<<r<<" "<<c<<" ";
        if(r > c)swap(r, c);
        if((r*c)%x != 0) {
            cout <<"Case #" <<i<<": "<<"RICHARD"<<endl;
            continue;
        }
        if((r == 1 || c == 1)&&(x > 2)){
            cout <<"Case #" <<i<<": "<<"RICHARD"<<endl;
            continue;
        }
        if(x == 1){
            cout <<"Case #" <<i<<": "<<"GABRIEL"<<endl;
            continue;
        }
        if(x == 4 && r == 2 && c == 4){
            cout <<"Case #" <<i<<": "<<"RICHARD"<<endl;
            continue;
        }
        if(x == 4 && r == 2 && c == 2){
            cout <<"Case #" <<i<<": "<<"RICHARD"<<endl;
            continue;
        }
        
        
        
        cout <<"Case #" <<i<<": "<<"GABRIEL"<<endl;
    }
    
    return 0;
}