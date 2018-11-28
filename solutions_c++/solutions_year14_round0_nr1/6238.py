//
//  main.cpp
//  cj_A
//
//  Created by Daming Lu on 4/11/14.
//  Copyright (c) 2014 Daming Lu. All rights reserved.
//

#include <iostream>
#include <algorithm>
using namespace std;

int row1[4];
int row2[4];

int dummy[4];

int main(int argc, const char * argv[])
{

    int cases=0;
    cin >> cases;
    
    int r1=-1, r2=-1;
    
    for(int i=1; i<=cases; i++) {
        cin>>r1;
        for(int j=1; j<=4; j++){
            if(j==r1) {
                for(int k=0; k<4; k++) {
                    cin >> row1[k];
                }
            } else {
                for(int k=0; k<4; k++) {
                    cin >> dummy[k];
                }
            }
        }
        
        cin>>r2;
        for(int j=1; j<=4; j++){
            if(j==r2) {
                for(int k=0; k<4; k++) {
                    cin >> row2[k];
                }
            } else {
                for(int k=0; k<4; k++) {
                    cin >> dummy[k];
                }
            }
        }
        
        sort(row1, row1+4);
        sort(row2, row2+4);
        
        int ans = 0;
        int ansCount = 0;
        int i1=0, i2=0;
        while(i1<4 && i2<4) {
            if (row1[i1] == row2[i2]) {
                ans = row1[i1];
                i1++;
                i2++;
                ansCount++;
            } else if (row1[i1] < row2[i2]) {
                i1++;
            } else {
                i2++;
            }
        }
        if(ansCount==0) {
            cout<<"Case #"<<i<<": Volunteer cheated!\n";
            continue;
        }
        if(ansCount>1) {
            cout<<"Case #"<<i<<": Bad magician!\n";
            continue;
        }
        
        cout<<"Case #"<<i<<": "<<ans<<"\n";
    }
    
    return 0;
}

