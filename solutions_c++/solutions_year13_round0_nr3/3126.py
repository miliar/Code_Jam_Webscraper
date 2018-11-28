//
//  main.cpp
//  GCJ2013
//
//  Created by wang yan hao on 13-4-13.
//  Copyright (c) 2013年 wang yan hao. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

ifstream in("/Users/wangyanhao/Documents/XcodeProjects/GCJ2013/C-small-attempt0.in.txt");
ofstream out("/Users/wangyanhao/Documents/XcodeProjects/GCJ2013/C-small-attempt0.out");

//#define in cin
//#define out cout

typedef long long ll;
int T;
ll A, B;

bool isPal(ll num) {
    ll d = 1;
    while (d * 10 < num) {
        d *= 10;
    }
    while (num > 10) {
        if (num / d != num % 10) {
            return false;
        }
        num -= (num / d) * d;
        num /= 10;
    }
    return true;
}

int main() {
    in >> T;
    for (int count = 1; count <= T; count++) {
        in >> A >> B;
        ll a = sqrt(A * 1.0);
        if (a * a < A) {
            a++;
        }
        ll b = sqrt(B * 1.0);
        int res = 0;
        for (ll i = a; i <= b; i++) {
            if (isPal(i) && isPal(i * i)) {
                res++;
            }
        }
        out << "Case #" << count << ": " << res << endl;
    }
    return 0;
}



/*
int T, N, M;
int desired[105][105];
int origin[105][105];

int main() {
    in >> T;
    for (int count = 1; count <= T; count++) {
        in >> N >> M;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                in >> desired[i][j];
                origin[i][j] = 100;
            }
        }
        for (int i = 0; i < N; i++) {
            int tmax = 0;
            for (int j = 0; j < M; j++) {
                if (desired[i][j] > tmax) {
                    tmax = desired[i][j];
                }
            }
            for (int j = 0; j < M; j++) {
                origin[i][j] = tmax;
            }
        }
        for (int i = 0; i < M; i++) {
            int tmax = 0;
            for (int j = 0; j < N; j++) {
                if (desired[j][i] > tmax) {
                    tmax = desired[j][i];
                }
            }
            for (int j = 0; j < N; j++) {
                if (origin[j][i] > tmax) {
                    origin[j][i] = tmax;
                }
            }
        }
        bool res = true;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (desired[i][j] != origin[i][j]) {
                    res = false;
                    break;
                }
            }
            if (!res) {
                break;
            }
        }
        out << "Case #" << count << ": ";
        if (res) {
            out << "YES" << endl;
        } else {
            out << "NO" << endl;
        }
    }
    return 0;
}

*/



/*
int T;
char board[5][5];

int main()
{
    in >> T;
    for (int count = 1; count <= T; count++) {
        bool Xwin = false, Ywin = false, hasEmpty = false;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                in >> board[i][j];
                if (board[i][j] == '.')
                    hasEmpty = true;
            }
        }
        //test win
        for (int i = 0; i < 4; i++) {
            int Xnum = 0, Ynum = 0;
            for (int j = 0; j < 4; j++) {
                if (board[i][j] == 'X' || board[i][j] == 'T')
                    Xnum++;
                if (board[i][j] == 'O' || board[i][j] == 'T')
                    Ynum++;
            }
            if (Xnum == 4) {
                Xwin = true;
                break;
            }
            if (Ynum == 4) {
                Ywin = true;
                break;
            }
            Xnum = 0, Ynum = 0;
            for (int j = 0; j < 4; j++) {
                if (board[j][i] == 'X' || board[j][i] == 'T')
                    Xnum++;
                if (board[j][i] == 'O' || board[j][i] == 'T') {
                    Ynum++;
                }
            }
            if (Xnum == 4) {
                Xwin = true;
                break;
            }
            if (Ynum == 4) {
                Ywin = true;
                break;
            }
            
        }
        int Xnum = 0, Ynum = 0;
        for (int i = 0; i < 4; i++) {
            if (board[i][i] == 'X' || board[i][i] == 'T') {
                Xnum++;
            }
            if (board[i][i] == 'O' || board[i][i] == 'T') {
                Ynum++;
            }
        }
        if (Xnum == 4) {
            Xwin = true;
        }
        if (Ynum == 4) {
            Ywin = true;
        }
        Xnum = 0, Ynum = 0;
        for (int i = 0; i < 4; i++) {
            if (board[i][3-i] == 'X' || board[i][3-i] == 'T') {
                Xnum++;
            }
            if (board[i][3-i] == 'O' || board[i][3-i] == 'T') {
                Ynum++;
            }
        }
        if (Xnum == 4) {
            Xwin = true;
        }
        if (Ynum == 4) {
            Ywin = true;
        }
        out << "Case #" << count << ": ";
        if (Xwin) {
            out << "X won" << endl;
        } else if (Ywin) {
            out << "O won" << endl;
        } else if (hasEmpty) {
            out << "Game has not completed" << endl;
        } else {
            out << "Draw" << endl;
        }
    }
    out.close();
    return 0;
}
 */

