#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int n, m;

int readint() {
    int cc = getc(stdin);
    for (; cc < '0' || cc > '9';)
        cc = getc(stdin);
    int ret = 0;
    for (; cc >= '0' && cc <= '9';) {
        ret = ret * 10 + cc - '0';
        cc = getc(stdin);
    }
    return ret;
}

void perform(int temp[105][105], int row, int ind, int val) {
    if (row == 1)
        for (int i = 0; i < m; i++) {
            if (temp[ind][i] > val)
                temp[ind][i] = val;
        } else
        for (int i = 0; i < n; i++) {
            if (temp[i][ind] > val)
                temp[i][ind] = val;
        }
}

int comp(int arr[105][105], int temp[105][105]) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (arr[i][j] != temp[i][j]) return 0;
    return 1;
}

int main(void) {
    int t;

    freopen("input.in", "r", stdin);
    freopen("output.txt", "w+", stdout);

    t = readint();
    //cin >> t;
    for (int cases = 1; cases <= t; cases++) {
        int arr[105][105], temp[105][105], mxrow[105] = {0}, mxcol[105] = {0};
        n = readint();
        m = readint();
        //cin >> n >> m;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                arr[i][j] = readint();
                //cin >> arr[i][j];
                temp[i][j] = 100;

                if (arr[i][j] > mxrow[i])
                    mxrow[i] = arr[i][j];
                if (arr[i][j] > mxcol[j])
                    mxcol[j] = arr[i][j];
            }
        }

        for (int i = 0; i < n; i++)
            perform(temp, 1, i, mxrow[i]);
        for (int i = 0; i < m; i++)
            perform(temp, 0, i, mxcol[i]);

        if (comp(arr, temp) == 1) printf("Case #%d: YES\n", cases);
        else printf("Case #%d: NO\n", cases);
    }
    return 0;
}

