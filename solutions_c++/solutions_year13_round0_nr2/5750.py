
//
//  LawnMower.h
//  Lawnmower
//
//  Created by Matthew Wein on 4/13/13.
//  Copyright (c) 2013 Matthew Wein. All rights reserved.
//

#ifndef __Lawnmower__LawnMower__
#define __Lawnmower__LawnMower__

#include <vector>
#include <iostream>

using namespace std;

class CLawnMower {
private:
    int m_width;
    int m_height;
    int m_max;
    vector<vector<int>> m_lawn;
    bool IsValid(int M);
    bool IsValid(int M, int r, int c);
public:
    void SetLawnDimensions(int N, int M);
    void Set(int r, int c, int v) { m_lawn[r][c] = v; }
    int Get(int r, int c) { return m_lawn[r][c]; }

    bool CanCreatePattern();
};

#endif /* defined(__Lawnmower__LawnMower__) */
