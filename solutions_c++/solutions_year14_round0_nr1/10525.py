/* 
 * File:   main.cpp
 * Author: absho
 *
 * Created on April 12, 2014, 5:59 PM
 */

#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define pi acos(-1.0)
#define N 1000000
#define LL long long

#define For(i, a, b) for( int i = (a); i < (b); i++ )
#define Fors(i, sz) for( size_t i = 0; i < sz.size (); i++ )
#define Fore(it, x) for(typeof (x.begin()) it = x.begin(); it != x.end (); it++)
#define Set(a, s) memset(a, s, sizeof (a))
#define Read(r) freopen(r, "r", stdin)
#define Write(w) freopen(w, "w", stdout)

#define isOn(S, j) (S & (1 << j))
#define setBit(S, j) (S |= (1 << j))
#define clearBit(S, j) (S &= ~(1 << j))
#define toggleBit(S, j) (S ^= (1 << j))
#define lowBit(S) (S & (-S))
#define setAll(S, n) (S = (1 << n) - 1)

using namespace std;

/*
 * 
 */

int gridA[5][5];
int gridB[5][5];

int main(int argc, char** argv) {
    Read("A-small-attempt0.in");
    Write("out.out");
    
    int T, a, b, cases = 1;; scanf("%d", &T);
    
    while(T--){
        scanf("%d", &a);
        
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                scanf("%d", &gridA[i][j]);
            }
        }
        
        scanf("%d", &b);
        
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                scanf("%d", &gridB[i][j]);
            }
        }
        
        int changes = 0, position;
        
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if(gridA[a-1][i] == gridB[b-1][j]){
                    changes++;
                    position = gridA[a-1][i];
                }
            }
        }
        
        if(changes == 0){
            printf("Case #%d: Volunteer cheated!\n", cases++);
        }
        else if(changes == 1){
            printf("Case #%d: %d\n", cases++, position);
        }
        else{
            printf("Case #%d: Bad magician!\n", cases++);
        }
    }
    return 0;
}