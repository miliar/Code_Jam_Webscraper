#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <ctime>
#define INF 100000000
#define N 5
using namespace std;

bool p[N][N][N];

int main() {
    int x,r,c;
    for( x = 1; x<N; x++){
        for(r = 1; r<N; r++){
            for(c = 1; c<=r; c++){
                if(r<x && c<x){
                    p[x][r][c] = true;
                }
                else if(x==1 ){
                    p[x][r][c] = false;
                }
                else if(x==2){
                    if(r*c%2==0)
                        p[x][r][c] = false;
                    else p[x][r][c] = true;
                }
                else if(x==4 || x == 5){
                    if(r>1 && c>1 && ((r%3==0 && c%2==0) ||
                                      (c%3==0 && r%2==0))){
                        p[x][r][c] = false;
                    }else{
                        p[x][r][c] = true;
                    }
                }else{
                    if(r>1 && c>1 && ((r%3==0 && c%2==0) ||
                                    (c%3==0 && r%2==0))){
                        p[x][r][c] = false;
                    }else{
                        p[x][r][c] = true;
                    }
                }
                p[x][c][r] = p[x][r][c] ;
            }
        }
    }
    p[3][3][3] = false;
    p[3][4][3] = false;
    p[3][3][4] = false;
    p[4][4][3] = false;
    p[4][3][4] = false;
    p[4][4][4] = false;
	int T; cin >> T;
	for(int _case = 1; _case <= T; _case++) {
        cin >> x >> r >> c;
        //cout << "---------\n";
        //cout << x << " " << r << " " << c << endl;
        cout << "Case #" << _case << ": ";
        if(p[x][r][c]){
            cout << "RICHARD";
        }else{
            cout << "GABRIEL";
        }
        cout << endl;
	}
	return 0;
}
