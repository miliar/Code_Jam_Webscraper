#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int grass[100][100];
int n, m;

bool allSame()
{
    int value = grass[0][0];
    for (int j = 0; j < n; j++) {
        for (int k = 0; k < m; k++) {
            if (grass[j][k] != value) {
                return false;
            }
        }
    }
    
    return true;
}

bool minValue()
{
    int value, minVal = 100;
    bool flag = false;
    int direction, pos;
    
    for (int j = 0; j < n; j++) {
        for (int k = 0; k < m; k++) {
            if (grass[j][k] < minVal) {
                minVal = grass[j][k];
            }
        }
    }
    
    for (int j = 0; j < n; j++) {
        value = grass[j][0];
        if (value == minVal) {
            minVal = value;
            if (m == 1) {
                flag = true;
                direction = 0;
                pos = j;
            }
            else {
                for (int k = 1; k < m; k++) {
                    if (grass[j][k] != value) {
                        break;
                        flag = false;
                    }
                    if (k == m - 1) {
                        flag = true;
                        direction = 0;
                        pos = j;
                    }
                }
            }
        }
    }
    for (int j = 0; j < m; j++) {
        value = grass[0][j];
        if (value == minVal) {
            minVal = value;
            if (n == 1) {
                flag = true;
                direction = 1;
                pos = j;
            }
            else {
                for (int k = 1; k < n; k++) {
                    if (grass[k][j] != value) {
                        break;
                        flag = false;
                    }
                    if (k == n - 1) {
                        flag = true;
                        direction = 1;
                        pos = j;
                    }
                }
            }
        }
    }
    if (flag) {
        if (direction == 0) {
            for (int j = 0; j < m; j++) {
                int val = 1000;
                for (int k = 0; k < n; k++) {
                    if (grass[k][j] > grass[pos][j] && grass[k][j] <= val) {
                        val = grass[k][j];
                    }
                }
                if (val != 1000) {
                    grass[pos][j] = val;
                }
            }
        }
        if (direction == 1) {
            for (int j = 0; j < n; j++) {
                int val = 1000;
                for (int k = 0; k < m; k++) {
                    if (grass[j][k] > grass[j][pos] && grass[j][k] <= val) {
                        val = grass[j][k];
                    }
                }
                if (val != 1000) {
                    grass[j][pos] = val;
                }
            }
        }
        return true;
    }
    else {
        return false;
    }
}

int main(void)
{
    ifstream fin("B-large.in");
    
    int t, i;
    fin >>t;
    //cin >>t;
    for (i = 1; i <= t; i++) {
        fin >>n >>m;
        //cin >>n >>m;
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < m; k++) {
                fin >>grass[j][k];
  //              cin >>grass[j][k];
            }
        }
        
        bool flag = true;
        
        while (!allSame()) {
            if (!minValue()) {
                flag = false;
                break;
            }
        }
        
        if (flag) {
            cout <<"Case #" <<i <<": YES" <<endl;
        }
        else {
            cout <<"Case #" <<i <<": NO" <<endl;
        }
    }
    
    return 0;
}

