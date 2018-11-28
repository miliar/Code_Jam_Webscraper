//  Google Code Jam - Qualification Round
//  Problem B - Lawnmower
//  Submission by Zemblan (nainan.kovoor@gmail.com)
//


#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;


enum { InitHeight = 100 };


struct Line
{
//  Construction
    Line(int length)
    :   m_vecOfPoints(length, InitHeight)
    {}
//  Attributes
    int  maxHeight() const
    { return *max_element(m_vecOfPoints.begin(), m_vecOfPoints.end()); }
//  Accessors
    int&  operator[](int i) { return m_vecOfPoints[i]; }
    const int&  operator[](int i) const { return m_vecOfPoints[i]; }

private:
//  Implementation
    vector<int>  m_vecOfPoints;
};


struct Pattern
{
//  Construction
    Pattern(int breadth, int width)
    :   m_vecOfCols (breadth,  Line(width))
    ,   m_vecOfRows (width,  Line(breadth))
    {}  
//  Attributes
    int  breadth() const { return m_vecOfCols.size(); }
    int  width() const { return m_vecOfRows.size(); }
//  Operations
    void  set(int col, int row, int height)
    {
        m_vecOfCols[col][row] = height;
        m_vecOfRows[row][col] = height;
    }
    const int&  get(int col, int row) const { return m_vecOfCols[col][row]; }
//  Accessors
    const Line&  lineForCol(int col) const { return m_vecOfCols[col]; }
    const Line&  lineForRow(int row) const { return m_vecOfRows[row]; }

private:
//  Implementation
    vector<Line>  m_vecOfCols;
    vector<Line>  m_vecOfRows;
};


bool canBeMowed(const Pattern& pattern)
{
    //  Compute col and row max heights

    int  breadth = pattern.breadth();
    int  width = pattern.width();
    vector<int>  vMaxHeightAlongCol (breadth, InitHeight);
    vector<int>  vMaxHeightAlongRow (width, InitHeight);

    // Determine max heights along cols
    for (int  col = 0; col != breadth; ++col) {
        vMaxHeightAlongCol[col] = pattern.lineForCol(col).maxHeight();
    }

    // Determine max heights along rows
    for (int  row = 0; row != width; ++row) {
        vMaxHeightAlongRow[row] = pattern.lineForRow(row).maxHeight();
    }


    //  Determine pattern feasibility by comparing height at each point
    //  with the max heights along that point's col and row
        
    // Scan all the points looking for one that is too low to have been touched
    // during mowing along both its col and its row - in which case infeasible
    for (int  col = 0; col != breadth; ++col) {
        for (int  row = 0; row != width; ++row) {
            const int&  heightAtPoint = pattern.get(col, row);
            if
            (   (heightAtPoint < vMaxHeightAlongRow[row])
            &&  (heightAtPoint < vMaxHeightAlongCol[col])
            ) {
                return false;
            }
        }
    }

    // Conclude that all points could have been touched during mowing - so feasible
    return true;
}


void processTestCase(int caseNum)
{
    // Initialise from input
    int  N, M;
    cin >> N >> M;
    Pattern  pattern (M, N);
    for (int  j = 0; j != N; ++j) {
        for (int  i = 0; i != M; ++i) {
            int  heightOfPoint;
            cin >> heightOfPoint;
            pattern.set(i, j, heightOfPoint);
        }
    }

    // Determine and output status
    cout << "Case #" << caseNum << ": ";
    if (canBeMowed(pattern)) {
        cout << "YES";
    } else {
        cout << "NO";
    }
    cout << endl;
}


int main()
{
    int  NTestCases;
    cin >> NTestCases;

    for (int  t = 0; t != NTestCases; ++t) {
        processTestCase(t + 1);
    }

    return 0;
}
