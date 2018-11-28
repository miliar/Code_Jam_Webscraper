/* 
 * File:   main.cpp
 * Author: SCORPIUS
 *
 * Created on April 14, 2013, 1:39 AM
 */

#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        int n, m;
        cin >> n >> m;
        int arr[n][m], rows[n], cols[m];memset(rows,0,sizeof(rows));memset(cols,0,sizeof(cols));
        for (int j = 0; j < n; j++)
            for (int k = 0; k < m; k++) {
                cin >> arr[j][k];
                if (rows[j] < arr[j][k])rows[j] = arr[j][k];
                if (cols[k] < arr[j][k])cols[k] = arr[j][k];
            }
        bool b = true;
        int j = 0, k = 0;
        for (int j = 0; b && j < n; j++)
            for (int k = 0; b && k < m; k++)
                b = (arr[j][k] == min(rows[j], cols[k]));
        printf("Case #%ld: ", i);
        cout << ((b == 1) ? "YES" : "NO" )<< endl;
    }
    return 0;
}

