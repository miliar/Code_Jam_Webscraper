#pragma comment(linker,"/STACK:256000000")
#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <functional>
#include <cmath>
#include <sstream>
#include <utility>
#include <ctime>
#include <memory.h>
#include<bitset>
#define forn(i,n) for (int i = 0; i < (int)(n); i++)
#define forv(i, a) for(int i=0; i<(int)a.size(); i++)
#define mset(a, val) memset(a, val, sizeof(a))
#define all(a) a.begin(),a.end()
#define mp make_pair
#define pb push_back
#define VI vector< int >
#define PII pair< int,int >
#define sqr(a) ((a)*(a))
#define cube(a) ((a)*(a)*(a))
#define pi 3.1415926535897932384626433832795
#define PI pi
#define iinf 1000000000
#define linf 1000000000000000000LL
#define sinf 10000
#define eps 1e-9
#define lng long long
#define ulng unsigned long long
#define uint unsigned int
#define X first
#define Y second
using namespace std;
#define prev asdprev
#define exit(a) do{ if (a) cerr<<"oops "<<a<<endl; exit(a); }while(0)

int dx[] = {-1, -1, -1, 0, 1, 1, 1, 0};
int dy[] = {-1, 0, 1, 1, 1, 0, -1, -1};

int get(int field, int rows, int cols, int x, int y) {
    if(x <0 || y <0 || x >=rows || y>=cols) {
        return -1;
    }
    else {
        return !!(field & (1 << (x*cols + y)));
    }
}

void setBit(int & mask, int rows, int cols, int x, int y) {
    mask |=  (1 << (x*cols + y));
}

int cntNeighbour(int field, int rows, int cols, int x, int y) {
    if(get(field, rows, cols, x, y) > 0) {
        return -1;
    }

    int res = 0;

    forn(t, 8) {
        int tx = x + dx[t];
        int ty = y + dy[t];

        if(get(field, rows, cols, tx, ty) > 0) {
            ++res;
        }
    }

    return res;
}

void reveal(int field, int & mask, int rows, int cols, int i, int j) {
    setBit(mask, rows, cols, i, j);

    if(cntNeighbour(field, rows, cols, i, j) == 0) {
        forn(t, 8) {
            int tx = i +dx[t];
            int ty = j + dy[t];

            if(get(mask, rows, cols, tx, ty) == 0) {
                reveal(field, mask, rows, cols, tx, ty);
            }
        }
    }
}

bool check(int field, int mask, int rows, int cols) {
    return (field ^ mask) == ((1<< (rows * cols)) - 1); 
}

int openField(int field, int rows, int cols) {
    forn(i, rows) {
        forn(j, cols) {
            int mask = 0;

            if(get(field, rows, cols, i, j) != 0) continue;

            reveal(field, mask, rows, cols, i, j);

            if(check(field, mask, rows, cols)) {
                return i*cols + j;
            }
        }
    }

    return -1;
}

int bitcnt(int num) {
    int res = 0;

    while(num) {
        ++res;
        num &= (num-1);
    }
    return res;
}

void print(int field, int pos, int rows, int cols) {
    if(pos==-1 || field==-1) {
        cout << "Impossible" << endl;
        return;
    }

    vector<string> res(rows);
    forn(i, rows) res[i].resize(cols);

    forn(i, rows) {
        forn(j, cols) {
            if(get(field, rows, cols, i, j) == 0) {
                res[i][j] = '.';
            }
            else {
                res[i][j] = '*';
            }
        }
    }

    res[pos/cols][pos%cols] = 'c';

    forn(i, rows) {
        forn(j, cols) {
            cout << res[i][j];
        }
        cout << endl;
    }
}

int resF[6][6][30];
int resP[6][6][30];

void generate() {
    mset(resP, -1);
    int maxc = 5;
    int maxr = 5;

    for(int row = 1; row <= maxr; ++row) {
        for(int col = 1; col <= maxc; ++col) {
            for(int field = 0; field < (1 << (row * col)); ++field) {
                int mines = bitcnt(field);

                if(resP[row][col][mines] != -1) continue;

                resP[row][col][mines] = openField(field, row, col);
                resF[row][col][mines] = field;
            }
        }
    }

}

#define taska "casting"
int main() {
#ifdef __ASD__
    freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
#else
    //freopen(taska".in", "r", stdin);freopen(taska".out", "w", stdout);
    //freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
#endif
    //ios_base::sync_with_stdio(false); cin.tie(0);

    generate();

    int T;
    cin >> T;

    forn(tc, T) {
        int r, c, m;
        cin>>r>>c>>m;
        
        cout << "Case #" << tc +1 <<":" << endl;
        print(resF[r][c][m], resP[r][c][m], r, c);
    }

    return 0;
}