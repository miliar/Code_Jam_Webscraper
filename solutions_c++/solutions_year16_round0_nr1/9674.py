//
//  main.cpp
//  CountingSheep
//
//  Created by TT on 09/04/2016.
//  Copyright © 2016 TT. All rights reserved.
//

#include <iostream>
#include <cstring>

using namespace std;

typedef unsigned long long ull;

bool check(bool *isSeen){
    for (int i=0; i < 10; ++i){
        if (! isSeen[i]){
            return true;
        }
    }
    return false;
}

void updateOccurence(ull N, bool *isSeen){
    while (N > 0){
        int d = N % 10;
        isSeen[d] = true;
        N /= 10;
    }
}

void fMain(int t){
    ull N;
    cin >> N;
    
    if (N == 0){
        cout << "Case #" << t << ": INSOMNIA" << endl;
        return;
    }
    
    bool isSeen[10];
    memset(isSeen, false, 10);
    ull i = 0;
    for (; check(isSeen); ++i){
        updateOccurence(i * N, isSeen);
    }
    cout << "Case #" << t << ": " << (i - 1) * N << endl;
}


int main(int argc, const char * argv[]) {
    int T;
    cin >> T;
    for (int t = 1; t <=T; ++t){
        fMain(t);
    }
    return 0;
}
