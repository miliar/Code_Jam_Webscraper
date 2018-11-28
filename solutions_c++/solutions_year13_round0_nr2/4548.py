/* 
 * File:   main.cpp
 * Author: tuannguyen
 *
 * Created on April 13, 2013, 4:48 PM
 */

#include <iostream>
#include <algorithm>
#include <iomanip>
#include <limits>
#include <cstring>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    int test;
    cin >> test;
    for(int t = 1; t <= test; t++){
        int n,m;
        cin >> n >> m;
        int a[100][100];
        int rCount[100][101] = {};
        int cCount[100][101] = {};
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++){
                cin >> a[i][j];
                rCount[i][a[i][j]]++;
                cCount[j][a[i][j]]++;
            }
        for(int i = 0; i<n; i++){
            for(int j = 99; j > 0; j--)
                rCount[i][j]+=rCount[i][j+1];
        }
        for(int i = 0; i<m; i++){
            for(int j = 99; j > 0; j--)
                cCount[i][j]+=cCount[i][j+1];
        }
        bool isOk = false;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(!(rCount[i][a[i][j] + 1] == 0 || cCount[j][a[i][j] + 1] == 0)){
                    cout << "Case #" << t << ": NO\n";
                    isOk = true;
                    break;
                }
            }
            if(isOk)
                break;
        }
        if(!isOk)
            cout << "Case #" << t << ": YES\n";
    }
    return 0;
}

