/*
 *  lawnmower.cpp
 *  Google_Jam
 *
 *  Created by Hugo Manet on 13/04/13.
 *  Copyright 2013 __MyCompanyName__. All rights reserved.
 *
 */

using namespace std;

//*
#include <iostream>
/*/
#include <fstream>

ifstream fcin("/Users/hugo/Downloads/B-large.in.txt");
ofstream fcout("/Users/hugo/Downloads/B-large.out.txt");

#define cin fcin
#define cout fcout
//*/

#include <queue>


enum Direction { Horizontal, Vertical };

int nbC, nbL;
int height[100][100];
int actualValue[2][100]; // First the direction (horiz enumerates lines), then line or column


struct Coord
{
    int line, col;
    
    Coord(int line, int col) : line(line), col(col) {}
    
    Coord& operator += (const Coord& o)
    {
        line += o.line;
        col += o.col;
        return *this;
    }
    
    int operator*()
    {
        return height[line][col];
    }
};

void readGrid()
{
    cin >> nbL >> nbC;
    
    for (int line = 0; line < nbL; line++)
        for (int col = 0; col < nbC; col++)
            cin >> height[line][col];
}

Coord findMax()
{
    Coord fromMax(0,0);
    
    for (int line = 0; line < nbL; line++)
        for (int col = 0; col < nbC; col++)
            if (height[line][col] > *fromMax)
                fromMax = Coord(line,col);
    
    return fromMax;
}


bool solveOne()
{
    readGrid();
    Coord start = findMax();
    
    for (int line = 0; line < nbL; line++)
        actualValue[Horizontal][line] = height[line][start.col];
    
    for (int col = 0; col < nbC; col++)
        actualValue[Vertical][col] = height[start.line][col];
    
    for (int line = 0; line < nbL; line++)
        for (int col = 0; col < nbC; col++)
            if (height[line][col] != min(actualValue[Horizontal][line], actualValue[Vertical][col]))
                return false;
    
    return true;
}

int main()
{
    int  T;
    cin>>T;
    
    for (int numTest = 1; numTest <= T; numTest++)
        if (solveOne())
            cout << "Case #" << numTest << ": YES\n";
        else
            cout << "Case #" << numTest << ": NO\n";
}

