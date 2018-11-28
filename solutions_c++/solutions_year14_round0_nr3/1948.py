// -*- C++ -*-
// File: a.cpp
// Copyright (C) 2013
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <numeric>
#include <memory.h>
#include <cstdio>
#include <assert.h>

using namespace std;

#define pb push_back
#define INF 1011111111
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define rep(i,n) FOR(i,0,n)
#define CL(a,v) memset((a),(v),sizeof(a))
#define mp make_pair
#define X first
#define Y second
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))

typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> pii;

/*** TEMPLATE CODE ENDS HERE */

const int MAX = 55;
int a[MAX][MAX];

bool b[5][5];
string ans[6][6][26];

void go(int x, int y, int R, int C) {
    
    if(x==R && y==C-1) {
        int M = 0;
        rep(i,R) rep(j,C) M += b[i][j];
        
        if(ans[R][C][M].size()>0) return;
        
        rep(i,R) rep(j,C) {
            if(b[i][j])
                a[i][j] = -1;
            else {
                a[i][j] = 0;
                FOR(dx,-1,2) FOR(dy,-1,2) {
                    if(dx==0&&dy==0) continue;
                    int nx = i+dx, ny = j+dy;
                    if(nx<0 || nx>=R || ny<0 || ny>=C) continue;
                    a[i][j] += b[nx][ny];
                }
            }
        }
        
        int cx = -1, cy = -1;
        rep(i,R) rep(j,C) {
            if(a[i][j]==0) {
                cx = i, cy = j;
            }
        }
        
        if(cx==-1) {
            if(R*C==M+1) {
                string str(R*C, '?');
                rep(i,R) rep(j,C) str[i*C+j] = '*';
                rep(i,R) rep(j,C) {
                    if(!b[i][j]) {
                        str[i*C+j] = 'c';
                    }
                }
                
                ans[R][C][M] = str;
            }
            return;
        }
        
        bool zeros_connected = true;
        rep(i,R) rep(j,C) {
            if(a[i][j]==0) {
                if(i==cx&&j==cy) continue;
                bool has_zero = false;
                FOR(dx,-1,2) FOR(dy,-1,2) {
                    if(dx==0&&dy==0) continue;
                    int nx = i+dx, ny = j+dy;
                    if(nx<0 || nx>=R || ny<0 || ny>=C) continue;
                    if(a[nx][ny]==0) has_zero = true;
                }
                zeros_connected &= has_zero;
            }
        }
        
        if(zeros_connected==false) {
            return;
        }
        
        bool nonzero_connected = true;
        rep(i,R) rep(j,C) {
            if(a[i][j]>0 && !b[i][j]) {
                bool has_zero = false;
                FOR(dx,-1,2) FOR(dy,-1,2) {
                    if(dx==0&&dy==0) continue;
                    int nx = i+dx, ny = j+dy;
                    if(nx<0 || nx>=R || ny<0 || ny>=C) continue;
                    if(a[nx][ny]==0) has_zero = true;
                }
                nonzero_connected &= has_zero;
            }
        }
        
        if(nonzero_connected==false) {
            return;
        }
        
        string str(R*C, '?');
        rep(i,R) rep(j,C) str[i*C+j] = b[i][j]?'*' : '.';
        str[cx*C+cy] = 'c';
        ans[R][C][M] = str;

        return;
    }
    
    if(x==R) x=0, y++;
    
    b[x][y] = false;
    go(x+1,y, R, C);
    
    b[x][y] = true;
    go(x+1,y, R, C);
}

void init_ans() {
    FOR(R,1,6) FOR(C,R,6) {
        CL(b,0);
        go(0,0,R,C);
    }
    FOR(R,1,6) FOR(C,R,6) FOR(M,0,R*C) if(ans[R][C][M].size()==0) ans[R][C][M] = "Impossible";
}

bool go(int x, int y, int left, int R, int C, int M, bool first = false) {
    
    if(left==M) return true;
    if(left<M) return false;
    
    bool memo[3][3];
    CL(memo,0);
    
    FOR(dx,-1,2) FOR(dy,-1,2) {
        
        if(first) {
            if(!(dx==0&&dy==0)) continue;
        }
        else {
            if(dx==0&&dy==0) continue;
        }
        
        int nx = x + dx, ny = y + dy;
        if(nx<0 || nx>= R || ny < 0 || ny >= C) continue;
        
        int discovered_cells = 0;
        
        FOR(i,max(0,nx-1), min(R-1,nx+1)+1) {
            FOR(j,max(0,ny-1), min(C-1,ny+1)+1) {
                memo[i-nx+1][j-ny+1] = a[i][j];
                if(!a[i][j]) discovered_cells ++;
                a[i][j] = true;
            }
        }
        if(discovered_cells==0) continue;
        
        if(go(nx, ny, R, C, M, left - discovered_cells)) return true;
        
        FOR(i,max(0,nx-1), min(R-1,nx+1)+1) {
            FOR(j,max(0,ny-1), min(C-1,ny+1)+1) {
                a[i][j] = memo[i-nx+1][j-ny+1];
            }
        }
    }
    return false;
}

pii solve(int R, int C, int M) {
    rep(i,R) rep(j,C) {
        CL(a,0);
        if(go(i,j,R*C, R, C, M, true)) return mp(i,j);
    }
    return mp(-1,-1);
}

int main() {
#ifdef LOCAL_HOST
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif
    
//    CL(b,1);
//    b[0][0] = false;
//    go(2,4,2,5);
    
    init_ans();

    int T;
    cin >> T;
    
    FOR(cs,1,T+1) {
        
        int R,C,M;
        cin >> R >> C >> M;
        
//        pii rr = solve(R, C, M);
        
        bool swaped = false;
        if(R>C) swap(R,C), swaped = true;
        
        if(ans[R][C][M]!="Impossible") {
            printf("Case #%d: \n", cs);
            if(!swaped) {
                rep(i,R){
                    rep(j,C) cout << ans[R][C][M][i*C+j];
                    if(!(i+1==R)) cout << endl;
                }
            }
            else {
                rep(j,C){
                    rep(i,R) cout << ans[R][C][M][i*C+j];
                    if(!(j+1==C)) cout << endl;
                }
            }
//            cout << endl;
//            if(rr.X==-1) {
//                cout << "mismatch " << cs << "\n"; 
//            }
        }
        else {
            printf("Case #%d: \n", cs);
            cout << "Impossible";
//            if(!(rr.X==-1)) {
//                
//                if(swaped) swap(R,C);
//                
//                printf("Case #%d:\n", cs);
//                rep(i,R) {
//                    rep(j,C) {
//                        if(a[i][j]) {
//                            if(rr==mp(i,j))
//                                printf("c");
//                            else
//                                printf(".");
//                        } else
//                            printf("*");
//                    }
//                    if(i+1<R) printf("\n");
//                }
//                cout << endl;
//            }
        }
        
        if(cs<T) cout << endl;
    }
    
    return 0;
}
