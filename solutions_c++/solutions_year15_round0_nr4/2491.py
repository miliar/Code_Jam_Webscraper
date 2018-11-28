#include <cassert>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
#include <gmpxx.h>
#include <Board.hpp>

using namespace std;


//------------------------------------------------------------------------------
int main() {
    int caseCount;
    cin >> caseCount;

    Board board;
    for (int i = 1; i <= caseCount; ++i) {
        board.init();
        board.calc();

        cout << "Case #" << i << ": " << (board.isWinRechard() ? "RICHARD" : "GABRIEL") << endl;
        //board.dump();
    }
    
    return 0;
}

//------------------------------------------------------------------------------
