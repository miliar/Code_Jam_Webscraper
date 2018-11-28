#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include<cstdio>
#include<cmath>
#include <queue>

using namespace std;

#define I 2
#define J 3
#define K 4

int array[10010];
int mul[5][5];
int N;

bool go(int index, int cur, int gotten) {
    if(cur == I && gotten == 1){
        gotten = I;
        cur = 1;
    }
    if(cur == J && gotten == I){
        gotten = J;
        cur = 1;
    }
    if(cur == K && gotten == J && index == N){
        return true;
    } else if(cur != K && gotten == J && index == N) {
        return false;
    } else if(gotten != J && index == N) {
        return false;
    }
    if(cur < 0){
        return go(index+1, -mul[array[index]][-cur], gotten);
    } else {
        return go(index+1, mul[array[index]][cur], gotten);
    }
}

int main() {
    int TC;
    int casenum = 1;
    
    mul[1][1] = 1;
    mul[I][I] = -1;
    mul[J][J] = -1;
    mul[K][K] = -1;
    mul[I][1] = I;
    mul[I][J] = -K;
    mul[I][K] = J;
    mul[J][1] = J;
    mul[J][I] = K;
    mul[J][K] = -I;
    mul[K][1] = K;
    mul[K][I] = -J;
    mul[K][J] = I;
    
    cin >> TC;
    while(TC--){
        int L, X;
        cin >> L >> X;
        string line;
        cin >> line;
        N = 0;
        vector<int> from;
        vector<int> to;
        for(int i = 0; i < X; i++){
            for(int j = 0; j < L; j++){
                if(line[j] == 'i'){
                    array[N++] = I;
                } else if(line[j] == 'j'){
                    array[N++] = J;
                } else if(line[j] == 'k'){
                    array[N++] = K;
                }
            }
        } 
        string m = (go(0, 1, 1) ? "YES" : "NO");
        cout << "Case #" << casenum++ << ": " << m << endl;
    }
    
}
