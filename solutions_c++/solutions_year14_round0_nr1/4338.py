//
//  main.cpp
//  DemoTest
//
//  Created by mezheng on 10/14/13.
//
//

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(int argc, const char * argv[])
{
    int n, r1, r2;
    int grid1[4][4];
    int grid2[4][4];
    
    cin>>n;
    for(int i=0; i<n; i++) {
        cin>>r1;
        for(int j=0; j<4; j++) {
            for (int k=0; k<4; k++) {
                cin>>grid1[j][k];
            }
        }
        cin>>r2;
        for(int j=0; j<4; j++) {
            for (int k=0; k<4; k++) {
                cin>>grid2[j][k];
            }
        }
        cout<<"Case #" << i+1 << ": ";
        bool isFound = false;
        bool isBad = false;
        int res;
        for(int j=0; j<4; j++) {
            for (int k=0; k<4; k++) {
                if(grid1[r1-1][j] == grid2[r2-1][k]) {
                    if (isFound) {
                        isBad = true;
                    } else {
                        isFound = true;
                        res = grid1[r1-1][j];
                    }
                    break;
                }
            }
            if (isBad) {
                break;
            }
        }
        if (isBad) {
            cout<<"Bad magician!\n";
        } else if (isFound) {
            cout<<res<<endl;
        } else {
            cout<<"Volunteer cheated!\n";
        }
    }
    return 0;
}

