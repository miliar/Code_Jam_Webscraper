////////////////////////////////////////////////////////////////////////////////
// B.cc
////////////////////////////////////////////////////////////////////////////////
/*! @file
//      Solves Google Code Jam Qualification Round Problem B
*/ 
//  Author:  Julian Panetta (jpanetta), julian.panetta@gmail.com
//  Company:  New York University
//
//  Created:  04/13/2013 18:08:24
//  Revision History:
//      04/13/2013  Julian Panetta    Initial Revision
////////////////////////////////////////////////////////////////////////////////
#include <iostream>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <limits>
#include <algorithm>

using namespace std;

struct Board {
    Board(size_t rows, size_t cols)
        : rows(rows), cols(cols), rowsLeft(rows), colsLeft(cols)
    {
        data = new int[rows * cols];
    }

    int get(size_t r, size_t c) const {
        return data[r * cols + c];
    }

    int &operator()(size_t r, size_t c) {
        assert((r < rows) && (c < cols));
        assert((r < rowsLeft) && (c < colsLeft));
        return data[r * cols + c];
    }

    const int &operator()(size_t r, size_t c) const {
        assert((r < rows) && (c < cols));
        assert((r < rowsLeft) && (c < colsLeft));
        return data[r * cols + c];
    }

    void deleteRow(size_t r) {
        assert(r < rowsLeft);
        // Shift everything back
        for (size_t rSource = r + 1; rSource < rowsLeft; ++rSource) {
            for (size_t c = 0; c < colsLeft; ++c) {
                (*this)(rSource - 1, c) = (*this)(rSource, c);
            }
        }
        --rowsLeft;
    }

    void deleteCol(size_t c) {
        assert(c < colsLeft);
        // Shift everything back
        for (size_t cSource = c + 1; cSource < colsLeft; ++cSource) {
            for (size_t r = 0; r < rowsLeft; ++r) {
                (*this)(r, cSource - 1) = (*this)(r, cSource);
            }
        }
        --colsLeft;
    }

    ~Board() { delete[] data; }

    int minValue() const {
        int theMin = numeric_limits<int>::max();
        for (int r = 0; r < (int) rowsLeft; ++r) {
            for (int c = 0; c < (int) colsLeft; ++c) {
                theMin = std::min(theMin, get(r, c));
            }
        }
        return theMin;
    }

    int removableRow() const {
        assert((rowsLeft > 0) && (colsLeft > 0));
        int minVal = minValue();
        // Find a row that is filled with the minimum value
        for (int r = 0; r < (int) rowsLeft; ++r) {
            bool validRow = true;
            for (int c = 0; c < (int) colsLeft; ++c) {
                if (get(r, c) != minVal) {
                    validRow = false;
                    break;
                }
            }
            if (validRow)
                return r;
        }

        return -1;
    }

    int removableCol() const {
        assert((rowsLeft > 0) && (colsLeft > 0));
        int minVal = minValue();
        // Find a col that is filled with the minimum value
        for (int c = 0; c < (int) colsLeft; ++c) {
            bool validCol = true;
            for (int r = 0; r < (int) rowsLeft; ++r) {
                if (get(r, c) != minVal) {
                    validCol = false;
                    break;
                }
            }
            if (validCol)
                return c;
        }

        return -1;
    }

    void print() const {
        for (size_t r = 0; r < rowsLeft; ++r) {
            for (size_t c = 0; c < colsLeft; ++c) {
                cout << (*this)(r, c) << ' ';
            }
            cout << endl;
        }
    }

    size_t rows, cols;
    size_t rowsLeft, colsLeft;
    int *data;
};

////////////////////////////////////////////////////////////////////////////////
/*! Program entry point
//  @param[in]  argc    Number of arguments
//  @param[in]  argv    Argument strings
//  @return     status  (0 on sucess)
*///////////////////////////////////////////////////////////////////////////////
int main(int argc, const char *argv[])
{
    int numTests;
    cin >> numTests;

    for (int t = 1; t <= numTests; ++t)  {
        size_t N, M;
        cin >> N >> M;
        Board board(N, M);
        for (size_t r = 0; r < N; ++r) {
            for (size_t c = 0; c < M; ++c) {
                cin >> board(r, c);
            }
        }

        bool possible = true;
        while ((board.rowsLeft > 0) && (board.colsLeft > 0)) {
            int r = board.removableRow();
            if (r >= 0) {
                board.deleteRow(r);
                continue;
            }

            int c = board.removableCol();
            if (c >= 0) {
                board.deleteCol(c);
                continue;
            }

            possible = false;
            break;
        }

        cout << "Case #" << t << ": " << (possible ? "YES" : "NO") << endl;
    }

    return 0;
}
