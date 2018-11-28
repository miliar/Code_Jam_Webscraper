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

void read(int &row, int a[4][4]) {
    cin >> row;
    --row;
    forn(i, 4) forn(j, 4) {
        cin >> a[i][j];
    }
}

void findAndMark(int val, int a[4][4]) {
    forn(i, 4)forn(j, 4) {
        if(a[i][j]==val) {
            a[i][j]=-a[i][j];
        }
    }
}

int solve() {
    int row1, row2;
    int a[4][4], b[4][4];

    read(row1, a);
    read(row2, b);

    forn(j, 4) {
        findAndMark(a[row1][j], b);
    }

    int res = 0;
    forn(j, 4) {
        if(b[row2][j] < 0) {
            if(res != 0) {
                res = -1;
            }
            else {
                res = -b[row2][j];
            }
        }
    }

    return res;
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
    
    int T;
    cin >> T;

    for(int tc = 0; tc < T; ++tc) {
        int res = solve();

        cout << "Case #" << tc + 1 << ": ";

        if(res == -1) {
            cout << "Bad magician!";
        }
        else if(res == 0) {
            cout << "Volunteer cheated!";
        }
        else {
            cout << res;
        }
        
        cout << endl;
    }


    return 0;
}