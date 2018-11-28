//
//  main1.cpp
//  CodeJam
//
//  Created by Victor Young on 4/16/16.
//  Copyright © 2016 Victor Young. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <deque>
using namespace std;
int a[2501];
int main(){
    
    if(freopen("/Users/Victor/Desktop/output.txt", "w", stdout) == NULL)
        fprintf(stderr,"error redirecting stdout\n");
    if(freopen("/Users/Victor/Desktop/B-large.in", "r", stdin) == NULL)
        fprintf(stderr,"error redirecting stdin\n");
    
    int n;
    cin >> n;
    
    for (int i=0; i<n; i++) {
        int N;
        cin >> N;
        memset(a, 0, 2501*sizeof(int));
        for (int k=0; k<2*N-1; k++) {
            for (int j = 0 ; j<N; j++) {
                int temp;
                cin >> temp;
                a[temp] ++;
            }

        }
        cout << "Case #"<<i+1<<":";
        for (int j=0; j<2501; j++) {
            if (a[j]%2) {
                cout << " "<<j;
            }
        }
        if (i!=n-1) {
            cout << endl;
        }

    }
}