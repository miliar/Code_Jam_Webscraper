/* 
 * File:   main.cpp
 * Author: a.elbashandi
 *
 * Created on April 13, 2013, 5:16 AM
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

using namespace std;

/*
 * 
 */

struct node {
    node(int node_x, int node_y, int node_t) : x(node_x), y(node_y), t(node_t) {}
    int x, y, t; 
};

int visited[105][105];
int grid[105][105];
int row, col;
int dr [] = {-1, 0, 1, 0};
int dc [] = {0, 1, 0, -1};

//bool dfs(node n, int k){
//    
//    stack<node> s;
//    s.push(n);
//    
//    bool perfect = false;
//    while(!s.empty()){
//        node f = s.top();
//        s.pop();
//        
//        if(f.x < 0 || f.x >= row) continue;
//        if(f.y < 0 || f.y >= col) continue;
//        
//        if(f.t != k) continue;
//        if(visited[f.x][f.y]) continue;
//        
//        visited[f.x][f.y] = true;
//        
//        if(f.x == 0 || f.x == row-1)
//            perfect = true;
//        if(f.y == 0 || f.y == col-1)
//            perfect = true;
//        
//        for (int i = 0; i < 4; i++) {
//            s.push(node(f.x + dr[i], f.y + dc[i], grid[f.x + dr[i]][f.y + dc[i]]));
//        }
//    }
//    
//    return perfect;
//}

bool checkCol(int column, int value){
    bool perfect = true;
    for (int i = 0; i < row; i++) {
        if(grid[i][column] > value)
            perfect = false;
    }
    return perfect;
}

int main(int argc, char** argv) {
    Read("B-large.in");
    Write("file.out");
    
    int T; scanf("%d", &T);
    int cases = 1;
    while(T--){
        scanf("%d %d", &row, &col);
        
        //Set(visited, false);
        
        int a;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                scanf("%d", &a);
                grid[i][j] = a;
            }
        }
        
        //bool perfect = true;
//        for (int i = 0; i < row; i++) {
//            for (int j = 0; j < col; j++) {
//                if(!visited[i][j]){
//                    perfect = dfs(node(i, j, grid[i][j]), grid[i][j]);
//                    if(!perfect) break;
//                }
//            }
//            if(!perfect) break;
//        }
        
        bool perfect = true;
//        for (int i = 0; i < row; i++) {
//            int b;
//            b = grid[i][0];
//            for (int j = 1; j < col; j++) {
//                if(b < grid[i][j]){
//                    perfect = checkCol(j-1, b);
//                }else if(b > grid[i][j]){
//                    perfect = checkCol(j, grid[i][j]);
//                    b = grid[i][j];
//                }
//                //b = grid[i][j];
//                if(!perfect) break;
//            }
//            if(!perfect) break;
//        }

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                for (int k = 0; k < col; k++) {
                    if(grid[i][j] < grid[i][k]){
                        perfect = checkCol(j, grid[i][j]);
                    }
                    if(!perfect) break;
                }
                if(!perfect) break;
            }
            if(!perfect) break;
        }
        
        if(perfect) printf("Case #%d: YES\n", cases++);
        else printf("Case #%d: NO\n", cases++);
    }
    return 0;
}

