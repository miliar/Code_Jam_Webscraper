//
//  main.cpp
//  codejam2013qual
//
//  Created by Petro Boychuk on 4/13/13.
//  Copyright (c) 2013 Petro Boychuk. All rights reserved.
//

#include <iostream>
using namespace std;

int a[1000][1000];

void solve() {
    int n,m;
    
    cin >> n >> m;
    
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cin >> a[i][j];
        }
    }
    
    int can = true;
    
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            //Row
            bool left = false;
            bool right = false;
            for (int k=0; k<j; k++) {
                if(a[i][j] < a[i][k]) {
                    left = true;
                }
            }
            
            for (int k=j+1; k<m; k++) {
                if(a[i][j] < a[i][k]) {
                    right = true;
                }
            }
            
            
            bool top = false;
            bool bottom = false;
            
            for (int k=0; k<i; k++) {
                if(a[i][j] < a[k][j]) {
                    top = true;
                }
            }
            
            for (int k=i+1; k<n; k++) {
                if(a[i][j] < a[k][j]) {
                    bottom = true;
                }
            }
            
            if((left || right) && (top || bottom)) {
                cout << "NO";
                return;
            }
        }
    }
    
    cout << "YES";
    
    
}


int main(int argc, const char * argv[])
{
    
    freopen("inputB.txt", "r", stdin);
    freopen("outputB.txt", "w", stdout);

    int t;
    cin >> t;
    
    for (int i=0; i<t; i++) {
        cout << "Case #" << i+1 << ": ";
        solve();
        cout << endl;
    }
    
    
    return 0;
}

