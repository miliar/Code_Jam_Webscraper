#include <iostream>
#include <stdio.h>
#include <assert.h>

using namespace std;

enum winner{
    GABRIEL,
    RICHARD
};

void print_winner(int caseNo, enum winner winner){
    if (winner == GABRIEL){
        printf("Case #%d: %s\n", caseNo, "GABRIEL");
    } else {
        printf("Case #%d: %s\n", caseNo, "RICHARD");
    }
}

// True if a tile can be chosen that can force a spillover.
// This should cover sizes 4, 5 and 6.
bool force_spillover(int size, int rows, int columns){
    assert (size < 7);
    // 1 by size tiles can't fit. Richard autowins.
    if (size > rows && size > columns){
        return true;
    }
    int shortside = (size + 1) / 2;
    int longside = size + 1 - shortside;

    if (shortside > columns || shortside > rows){
        return true;
    }
    return false;
}

// True if it is possible to make a T shape that can divide the rectangle into
// two sides that are both not divisible by size.
// L shapes can't work because they can be put to the side.
// Example:
//
// - * * *
// - - * -
//
// Invalid

bool possible_t(int size, int rows, int columns){

}

// Gabriel wins if he can tile.
// Richard wins if Gabriel can't.
enum winner omino(){
    int size, rows, columns;
    cin >> size >> rows >> columns;
    // Trivial cases

    // If tiles don't divide evenly, Richard wins.
    if ((rows * columns) % size != 0){
        return RICHARD;
    }

    // 1 and 2 are easy tilings.
    if ( size == 1){
        return GABRIEL;
    } else if (size == 2){
        return GABRIEL;
    }

    // For any combination of rows and columns divisible by 3,
    // only 1 x 3 and 3 x 1 can't be tiled.
    // An L shape prevents tiling.
    if (size == 3){
        if (rows == 1 || columns == 1){
            return RICHARD;
        } else {
            return GABRIEL;
        }
    }

    // With a size of 7 or greater, Richard can choose a tile with a hole.
    //
    // ***
    // * *
    // **
    // It's impossible to fill it in without overlapping.
    if (size >= 7){
        return RICHARD;
    }

    // Only size 4, 5 and 6 left.
    if (force_spillover(size, rows, columns)){
        return RICHARD;
    }

    // A T piece can split the rectangle into two shapes with odd number of tiles.
    // The cross bar can be used to force the orientation.
    if (size == 4 && (rows == 2 || columns == 2)){
        return RICHARD;
    }

    // It can't work with 5 since a T piece of size 5 can be rotated.

    // This also applies to 6.
    if (size == 6 && (rows == 3 || columns == 3)){
        return RICHARD;
    }
    // Any other special cases?
    return GABRIEL;


}

int main(int argc, char* argv[]){
    int cases;
    cin >> cases;
    for (int i = 1; i <= cases; i++){
        print_winner(i, omino());
    }
}
