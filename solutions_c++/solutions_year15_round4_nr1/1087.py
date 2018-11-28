#include <iostream> 
#include <map> 
#include <vector> 
#include <string> 
#include <set> 
#include <bitset> 
#include <algorithm> 
#include <numeric> 
#include <queue> 
#include <list> 
#include <limits> 
#include <stack> 
#include <sstream> 
#include <fstream> 
#include <ctime> 
#include <cstdlib> 
#include <complex> 
#include <cctype> 
#include <iomanip> 
#include <functional> 
#include <cstring> 
using namespace std; 
 
typedef long long int64 ; 
typedef unsigned long long uint64;

int dir[][2] = {
    -1, 0, 0,1, 1,0, 0 , -1 
}; 

int getdir(char c){
    if(c=='^') return 0 ;
    if(c=='>' ) return 1;
    if( c=='v') return 2;
    if( c =='<') return 3;
}

char s[100+10][100+10];
int main (){
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);

    int T; 
    cin >> T ; 
    for(int cas  = 1 ; cas <= T ; ++cas){ 
        int R,C; 
        cin >> R >> C; 
        for(int i = 0 ; i < R ; ++i)
            scanf("%s", s[i]);
        bool fail = false;
        int ans = 0; 
        for(int i = 0 ; i < R ; ++i){ 
            for(int j = 0 ; j < C ; ++j){ 
                if(s[i][j] =='.') continue;
                bool have = false; 
                for(int ii = 0 ; ii < R ; ++ii){ 
                    if( ii == i ) continue; 
                    if(s[ii][j] != '.') have = true; 
                }
                for(int jj = 0 ; jj < C ; ++jj){ 
                    if( jj == j ) continue; 
                    if( s[i][jj] != '.') have = true; 
                 }
                if(!have) fail = true; 
                int d = getdir(s[i][j]); 
                int tx = i , ty = j; 
                int can = 0;
                while( tx >= 0 && tx < R && ty >= 0 && ty < C){
                    if(s[tx][ty] != '.')++can; 
                    tx += dir[d][0]; 
                    ty += dir[d][1]; 
                }
                if(can==1) 
                    ++ans; 
            }
        }
        cout <<"Case #"<<cas <<": "; 
        if(fail) cout <<"IMPOSSIBLE"<<endl;
        else cout <<ans<<endl;                

    }
    return 0;
}

