#include <cstdio>
#include <cmath>
#include <string>
#include <iomanip>
#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long ll;
int r, c;
int chart[100][100];
int config[100][100];

void solve(int cid){
    fill(config[0], config[0]+100*100, 15);

    //up
    int ch = 14;
    for(int i = 0; i < c; i++){
        if(chart[0][i] == -1){
            int j = 1;
            for(; j < r && chart[j][i] == -1; j++);
            if(j < r)
                config[j][i] &= ch;
        }
        else
            config[0][i] &= ch;
    }
    
    //down
    ch = 11;
    for(int i = 0; i < c; i++){
        if(chart[r-1][i] == -1){
            int j = r-2;
            for(; j >= 0 && chart[j][i] == -1; j--);
            if(j >= 0)
                config[j][i] &= ch;
        }
        else
            config[r-1][i] &= ch;
    }
    
    //left
    ch = 7;
    for(int i = 0; i < r; i++){
        if(chart[i][0] == -1){
            int j = 1;
            for(; j < c && chart[i][j] == -1; j++);
            if(j < c)
                config[i][j] &= ch;
        }
        else
            config[i][0] &= ch;
    }
    
    //right
    ch = 13;
    for(int i = 0; i < r; i++){
        if(chart[i][c-1] == -1){
            int j = c-2;
            for(; j >= 0 && chart[i][j] == -1; j--);
            if(j >= 0)
                config[i][j] &= ch;
        }
        else
            config[i][c-1] &= ch;
    }
    
    int cnt = 0;
    bool possible = true;
    for(int i = 0; i < r; i++)
        for(int j = 0; j < c; j++){
            if(chart[i][j] != -1){
                if(config[i][j] == 0)
                    possible = false;
                else if(config[i][j] & chart[i][j])
                    cnt += 0;
                else
                    cnt += 1;
            }
        }
    
    if(possible)
        printf("Case #%d: %d\n", cid, cnt);
    else
        printf("Case #%d: IMPOSSIBLE\n", cid);
}

int main()
{
    freopen("/Users/bochen/Downloads/textfile.in","r", stdin);
    freopen("/Users/bochen/Downloads/textfile.out","w", stdout);

    int t;
    cin >> t;
    for(int cid = 1; cid <= t; cid++){
        cin >> r >> c;
        char ch;
        for(int i = 0; i < r; i++)
            for(int j = 0; j < c; j++){
                cin >> ch;
                switch (ch) {
                    case '^':
                        chart[i][j] = 1;
                        break;
                    case '>':
                        chart[i][j] = 2;
                        break;
                    case 'v':
                        chart[i][j] = 4;
                        break;
                    case '<':
                        chart[i][j] = 8;
                        break;
                    default:
                        chart[i][j] = -1;
                }
            }
        solve(cid);
    }
    return 0;
}
