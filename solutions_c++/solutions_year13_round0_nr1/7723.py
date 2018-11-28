//
//  T1.cpp
//  GCJ.2013.1
//
//  Created by Orpine on 13-4-13.
//  Copyright (c) 2013年 Orpine. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;

int T,ans;
string s[4];

int row(int x)
{
    int pos = 0;
    for (int i = 0; i < 4; i++) {
        if (s[x][i] == '.') {
            return 0;
        }
        if (s[x][i] != 'T') {
            if (!pos) {
                pos = s[x][i];
            }
            else if (pos != s[x][i]) {
                return -1;
            }
        }
    }
    return pos;
}
int col(int x)
{
    int pos = 0;
    for (int i = 0; i < 4; i++) {
        if (s[i][x] == '.') {
            return 0;
        }
        if (s[i][x] != 'T') {
            if (!pos) {
                pos = s[i][x];
            }
            else if (pos != s[i][x]) {
                return -1;
            }
        }
    }
    return pos;
}
int diagonal(int x)
{
    int pos = 0;
    if (x == 0) {
        for (int i = 0; i < 4; i++) {
            if (s[i][i] == 'x') {
                return 0;
            }
            if (s[i][i] != 'T') {
                if (!pos) {
                    pos = s[i][i];
                }
                else if (pos != s[i][i]) {
                    return -1;
                }
            }
        }
    }
    else
    {
        for (int i = 0; i < 4; i++) {
			if (s[3 - i][i] == '.') return 0;
			if (s[3 - i][i] != 'T') {
				if (!pos) pos = s[3 - i][i];
				else if (pos != s[3 - i][i]) return -1;
			}
		}
    }
    return pos;
}
int main(int argc, const char * argv[])
{
    scanf("%d",&T);
    for (int i = 1; i <= T; i++) {
        cout << "Case #" << i << ": ";
        for (int i = 0; i < 4; i++) {
            cin >> s[i];
            int ans = -2147483647;
            for (int i = 0; i < 4; i++) {
                ans = max(ans,row(i));
            }
            for (int i = 0; i < 4; i++) {
                ans = max(ans,col(i));
            }
            ans = max(ans,diagonal(0));
            ans = max(ans,diagonal(1));
        }
        if (ans == 0) {
            cout << "Game has not completed";
        }
        else if (ans == -1) {
            cout << "Draw";
        }
        else if (ans == 'X') {
            cout << "X won";
        }
        else {
            cout << "O won";
        }
        cout << endl;
    }
    return 0;
}