//
//  main.cpp
//  codejam4
//
//  Created by Youngsun Suh on 2015-04-10.
//  Copyright (c) 2015 Youngsun Suh. All rights reserved.
//

#include <iostream>

using namespace std;

bool fillGrid(int X, int R, int C) {
    if (R < X && C < X)
        return false;
    
    if ((R * C) % X)
        return false;
    
    if (C < X-1 || R < X-1)
        return false;
    
    return true;
}

int main(int argc, const char * argv[]) {
    int nCase;
    cin >> nCase;
    cin.ignore();
    
    for (int i=0; i<nCase; i++) {
        int X, R, C;
        
        cin >> X >> R >> C;
        
        cout << "Case #" << i+1 << ": "
        << (fillGrid(X, R, C) ? "GABRIEL" : "RICHARD") << endl;
    }
    return 0;
}
