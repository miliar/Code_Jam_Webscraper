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
        int now = 0;
        int s;
        cin >> s;
        for(int j = 0; j <= s; j++ ){
            char ch;
            cin >> ch;
            if(j <= now){
                now+= int(ch - '0');
            }else{
                ans+=j-now;
                now = j+int(ch - '0');
            }
        }
        
        cout <<"Case #" <<i<<": "<<ans<<endl;
    }
    
    return 0;
}