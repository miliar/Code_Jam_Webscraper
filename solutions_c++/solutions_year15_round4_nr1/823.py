#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string.h>
#include "gcj.h"
using namespace std;


const int MAXN = 110;
string mp[MAXN];

int getID(int i, int j, int c)
{
    return i * c + j;
}

int indeg[MAXN * MAXN], outdeg[MAXN * MAXN];


void move(int i, int j, int dx, int dy, int R, int C){
    //cout << "see " << mp[i][j] << " at " << i << " " << j << endl;
    int id = getID(i, j, C);
    i += dx, j += dy;
    while(i<R && i>=0 && j<C && j>=0){
        if(mp[i][j] != '.') {
            outdeg[id]++;
    //        cout << "see " << mp[i][j] << " at " << i << " " << j << endl;
            id = getID(i, j, C);
            indeg[id]++;
            break;
        }
        i += dx; j += dy;
    }
}

int row[MAXN], col[MAXN];
bool judge(int R, int C)
{
    memset(row, 0, sizeof(row));
    memset(col, 0, sizeof(col));

    for(int i=0; i<R; i++){
        for(int j=0; j<C; j++){
            if(mp[i][j] == '.') continue;
            row[i]++;
            col[j]++;
        }
    }
    for(int i=0; i<R; i++)
    for(int j=0; j<C; j++){

        if( mp[i][j] != '.' && row[i] == 1 && col[j] == 1 ) {
            //cout << i << " " << j << "is false" << endl;
            return false;
        }

    }
    return true;
}

int solve(int R, int C)
{
    if(judge(R, C) == false) return -1;
    memset(indeg, 0, sizeof(indeg));
    memset(outdeg, 0, sizeof(outdeg));
    for(int i=0; i<R; i++){
        for(int j=0; j<C; j++){
            if(mp[i][j] == '.') continue;
            //cout << "now " << mp[i][j] << endl;
            switch(mp[i][j]){
            case '>':
                move(i, j, 0, 1, R, C);
            break;
            case 'v':
                move(i, j, 1, 0, R, C);
            break;
            case '<':
                move(i, j, 0, -1, R, C);
            break;
            case '^':
                move(i, j, -1, 0, R, C);
            break;
            }
        }
    }

    int ans = 0;
    for(int i=0; i<R; i++){
        for(int j=0; j<C; j++){
            if(mp[i][j] != '.'){
                int id = getID(i, j, C);
                if(outdeg[id] == 0) ans++;
            }
        }
    }
    return ans;
}


int main(){
    useFile("A4");
    int T, N, M, Q, K;
    cin >> T;
    for(int ca = 1; ca <= T; ca++){
        int R, C;
        cin >> R >> C;
        for(int i=0; i<R; i++){
            cin >> mp[i];
        }
        int res = solve(R, C);

        cout << "Case #" << ca << ": ";
        if(res == -1) cout << "IMPOSSIBLE" << endl;
        else cout << res << endl;
    }
}
