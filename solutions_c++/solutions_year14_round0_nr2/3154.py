#include <iostream>
#include <map>
#include <algorithm>
#include <string>
#include <queue>
#include <vector> 
#include <cstdio>
#include <stack>
#include <cassert>
#include <sstream>
using namespace std;  


int main (){ 
    freopen("b.in","r",stdin); 
    freopen("b.out","w",stdout); 
    int T ;
    cin >> T ; 
    for(int Cas = 1 ; Cas <= T; ++Cas){ 
        double C,F,X; 
        cin >>C >> F >> X; 
        double ans = 10000000000.; 
        int bd = (int)X;
        while( bd < X + 1.) ++bd; 
        double speed = 2., cur = 0; 
        for(int i=0; i <= 100000000 ; ++i){  
            ans = min( X / speed + cur, ans); 
            cur += C/speed; 
            if(cur > ans ) break; 
            speed += F; 
        }
        cout << "Case #"<<Cas<<": " ; 
        printf("%.10lf\n", ans); 
    }
    return 0;
}
