/*
 * =====================================================================================
 *
 *       Filename:  gcj.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  04/13/2013 09:18:14 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  ranaflx
 *        Company:  hit-ACM-Group
 *
 * =====================================================================================
 */

#include <cstdio>
#include <queue>
using namespace std;

int n, m;
const int N = 100;
int h[N][N], tar[N][N];

bool can_cut_row(int ith, int v) {
    for(int i = 0;i < m;i++) {
        if(!(tar[ith][i] <= v && v <= h[ith][i])) return false;
    }
    return true;
}
void cut_row(int ith, int v) {
    for(int i = 0;i < m;i++) h[ith][i] = v;
}

bool can_cut_col(int ith, int v) {
    for(int i = 0;i < n;i++) {
        if(!(tar[i][ith] <= v && v <= h[i][ith])) return false;
    }
    return true;
}
void cut_col(int ith, int v) {
    for(int i = 0;i < n;i++) h[i][ith] = v;
}

typedef pair<int, pair<int, int> > PIII;
bool solve(int n, int m) {
    priority_queue<PIII> pq;
    for(int i = 0;i < n;i++) for(int j = 0;j < m;j++) h[i][j] = N + 1;
    for(int i = 0;i < n;i++) for(int j = 0;j < m;j++) {
        if(i == 0 || j == 0 || i == n - 1 || j == m - 1) {
            pq.push(make_pair(tar[i][j], make_pair(i, j)));
        }
    }
    while(!pq.empty()) {
        PIII now = pq.top();
        pq.pop();
        int v = now.first, i = now.second.first, j = now.second.second;
//        printf("%d (%d, %d)\n", v, i, j);
//        for(int i = 0;i < n;i++) for(int j = 0;j < m;j++) {
//            printf("%d%c", h[i][j], j == m - 1 ? '\n' : ' ');
//        }
        if((i == 0 || i == n - 1) && can_cut_col(j, v)) cut_col(j, v);
        if((j == 0 || j == m - 1) && can_cut_row(i, v)) cut_row(i, v);
    }
    for(int i = 0;i < n;i++) for(int j = 0;j < m;j++) {
        if(tar[i][j] != h[i][j]) {
            return false;
        }
    }
    return true;
}
int main() {
    int t;
    scanf("%d", &t);
    for(int cas = 1;cas <= t;cas++) {
        scanf("%d %d", &n, &m);
        for(int i = 0;i < n;i++) for(int j = 0;j < m;j++) scanf("%d", &tar[i][j]);
        printf("Case #%d: %s\n", cas, solve(n, m) ? "YES" : "NO");
    }
    return 0;
}
