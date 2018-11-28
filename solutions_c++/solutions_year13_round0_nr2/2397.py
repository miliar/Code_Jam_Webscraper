//
//  main.cpp
//  lawn
//
//  Created by John Scholes on 13/04/2013.
//  Copyright (c) 2013 John Scholes. All rights reserved.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    int N; cin >> N;
    int i, j, a[100][100], htError, rprob, cprob, tooshort, k;
    for(int N1=1; N1<=N; N1++) {
        int R,C; cin >> R >> C;
        for(i=0; i<R; i++)
            for(j=0; j<C; j++)
                cin >> a[i][j];
        htError=0;
        for(i=0; i<R; i++) for(j=0; j<C; j++)
            if(a[i][j]<1 || a[i][j]>100) htError=1;
        if(htError) {
            cout << "Case #" << N1 << ": NO\n";
            continue;
        }
        for(i=0; i<R; i++) {
            for(j=0; j<C; j++) {
                rprob=0; cprob=0; tooshort=0;
                for(k=0; k<R; k++) if(k!=i && a[k][j]>a[i][j]) rprob=1;
                for(k=0; k<C; k++) if(k!=j && a[i][k]>a[i][j]) cprob=1;
                if(rprob==1 && cprob==1) {
                    tooshort=1;
                    break;
                }
            }
            if(tooshort==1) break;
        }
        if(tooshort==1) {
            cout << "Case #" << N1 << ": NO\n";
            continue;
        }
        cout << "Case #" << N1 << ": YES\n";
    }
    return 0;
}

