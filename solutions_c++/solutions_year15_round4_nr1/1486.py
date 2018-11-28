#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <stack>
#include <cstring>
#include <iomanip>
#include <cctype>
#include <map>

using namespace std;

#define BLANK 0
#define UP 1
#define RIGHT 2
#define DOWN 3
#define LEFT 4

int a[105][105];

int p[105][105][5];

void solve(int t) {
    int r,c; cin>>r>>c;
    for(int i = 0;i < r;i++) {
        string s; cin>>s;
        for(int j = 0;j < c;j++) {
            if(s[j] == '.') a[i][j] = BLANK;
            else if(s[j] == '^') a[i][j] = UP;
            else if(s[j] == '>') a[i][j] = RIGHT;
            else if(s[j] == 'v') a[i][j] = DOWN;
            else a[i][j] = LEFT;
        }
    }
    int flag = 0;
    for(int i = 0;i < r;i++) {
        flag = 0;
        for(int j = 0;j < c;j++) {
            if(flag) p[i][j][LEFT] = 1;
            else p[i][j][LEFT] = 0;
            if(a[i][j] != BLANK) flag = 1;
        }
    }
    flag = 0;
    for(int j = 0;j < c;j++) {
        flag = 0;
        for(int i = 0;i < r;i++) {
            if(flag) p[i][j][UP] = 1;
            else p[i][j][UP] = 0;
            if(a[i][j] != BLANK) flag = 1;
        }
    }
    flag = 0;
    for(int i = 0;i < r;i++) {
        flag = 0;
        for(int j = c - 1;j >= 0;j--) {
            if(flag) p[i][j][RIGHT] = 1;
            else p[i][j][RIGHT] = 0;
            if(a[i][j] != BLANK) flag = 1;
        }
    }
    flag = 0;
    for(int j = 0;j < c;j++) {
        flag = 0;
        for(int i = r - 1;i >= 0;i--) {
            if(flag) p[i][j][DOWN] = 1;
            else p[i][j][DOWN] = 0;
            if(a[i][j] != BLANK) flag = 1;
        }
    }
    int cnt = 0;
    for(int i = 0;i < r;i++) {
        for(int j = 0;j < c;j++) {
            if(a[i][j] == BLANK) continue;
            if(p[i][j][a[i][j]]) continue;
            if(p[i][j][UP] || p[i][j][DOWN] || p[i][j][RIGHT] || p[i][j][LEFT]) {
                cnt++;
                continue;
            }
            printf("Case #%d: IMPOSSIBLE\n",t);
            return;
        }
    }
    printf("Case #%d: %d\n",t,cnt);
}

int main() {
    freopen("/Users/administrator/Desktop/A-large.in","r",stdin);
    freopen("/Users/administrator/Desktop/gcjoutput.txt","w",stdout);
    int t; cin>>t;
    for(int i = 1;i <= t;i++) {
        solve(i);
    }
    
}