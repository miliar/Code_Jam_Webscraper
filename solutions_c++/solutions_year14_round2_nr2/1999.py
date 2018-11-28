using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

#define D(x) cout << #x " = " << (x) << endl

int t;
const int MAXA = 1000;
int matriz[MAXA +5 ][MAXA +5 ];
int a,b,k;

void llenarMat(){
   for(int i = 0; i <= MAXA; ++i)
     for(int j = 0; j<= MAXA; ++j)
        matriz[i][j] = (i&j);     
}
int ans(){
   int acum = 0;
   for(int i = 0; i < a; ++i)
     for(int j = 0; j < b; ++j)
        if(matriz[i][j] < k) acum++;
   return acum;    
}

int main(){
    cin >> t;
    llenarMat();
    int z = 1;
    while(t--){
       cin >> a >> b >> k;
       cout << "Case #" << z++ << ": " << ans() << endl;    
    }
    return 0;    
}
