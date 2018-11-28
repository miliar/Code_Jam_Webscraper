//
//  main.cpp
//  fair
//
//  Created by John Scholes on 13/04/2013.
//  Copyright (c) 2013 John Scholes. All rights reserved.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    int N; cin >> N;
    for(int N1=1; N1<=N; N1++) {
        int A, B, count;
        cin >> A >> B;
        count=0;
        if(A==1) count++;
        if(A<=4 && B>=4) count++;
        if(A<=9 && B>=9) count++;
        if(A<=121 && B>=121) count++;
        if(A<=484 && B>=484) count++;
        cout << "Case #" << N1 << ": " << count << "\n";
    }
    return 0;
}

