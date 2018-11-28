
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void fillColumn(vector<vector<int> >& matrix, const vector<int>& col, int colPos)
{
    for (size_t i = 0; i < matrix.size(); ++i) {
        matrix[i][colPos] = col[i];
    }
}

bool fuzzyMatchRow(vector<vector<int> >& matrix, int rowPos, const vector<int>& row)
{
    for (size_t i = 0; i < row.size(); ++i) {
        int m = matrix[rowPos][i];
        if (m != -1 && m != row[i]) {
            return false;
        }
    }
    return true;
}

bool fuzzyMatchCol(vector<vector<int> >& matrix, int colPos, const vector<int>& col)
{
    for (size_t i = 0; i < col.size(); ++i) {
        int m = matrix[i][colPos];
        if (m != -1 && m != col[i]) {
            return false;
        }
    }
    return true;
}

vector<int> copyCol(vector<vector<int> >& matrix, int colPos)
{
    vector<int> result;
    for (size_t i = 0; i < matrix.size(); ++i) {
        result.push_back(matrix[i][colPos]);
    }
    return result;
}

void printMatrix(const vector<vector<int> >& matrix) {
    for (const auto& r : matrix) {
        for (const auto& e : r) {
            cout << e << ' ';
        }
        cout << endl;
    }
}

int main ()
{
    int tests;
    cin >> tests;

    for (int test = 1; test <= tests; ++test) {
        int numRows;
        vector< vector<int> > lists, listsCopy;
        vector< vector<int> > matrix;

        cin >> numRows;

        lists.resize(numRows*2-1);
        matrix.resize(numRows);

        int smallest = 99999;
        int largest  = 0;

        for (auto& l : lists) {
            l.resize(numRows);
            for (auto& n : l) {
                cin >> n;
                if (n > largest)  largest = n;
                if (n < smallest) smallest = n;
            }
        }

        listsCopy = lists;

        for (auto& m : matrix) {
            m.resize(numRows, -1);
        }

        // Try to find the box. We always have at least 3 of 4 walls
        // We can arbitrarily choose the orientation of the matrix

        vector< vector<int> > smallestList;
        vector< vector<int> > largestList;


        // Smallest must be in the top left corner
        for (auto litr = lists.begin(); litr != lists.end(); ++litr) {
            auto& l = *litr;
            if (l[0] == smallest) {
                smallestList.push_back(l);
            }
        }

        // Try to find the list with last elem == largest and first elem last of the top row
        int tallestFirstRow = matrix[0].back();
        for (auto litr = lists.begin(); litr != lists.end(); ++litr) {
            auto& l = *litr;
            if (l.back() == largest) {
                largestList.push_back(l);
            }
        }

        bool matrixFilled = false;
        for (const auto& s : smallestList) {
            for (const auto& l : largestList) {
                // Pick s and l as the first and last row and make sure we can build the matrix of that
                vector< vector<int> > m1 = matrix;
                vector< vector<int> > lsts = listsCopy;

                m1[0]     = s;
                m1.back() = l;

                for (auto litr = lsts.begin(); litr != lsts.end(); ++litr) {
                    if (*litr == s) {
                        lsts.erase(litr);
                        break;
                    }
                }
                for (auto litr = lsts.begin(); litr != lsts.end(); ++litr) {
                    if (*litr == l) {
                        lsts.erase(litr);
                        break;
                    }
                }

                for(size_t c = 0; c < numRows; ++c) {
                    for (auto litr = lsts.begin(); litr != lsts.end(); ++litr) {
                        if (litr->front() == s[c] && litr->back() == l[c]) {
                            fillColumn(m1, *litr, c);
                            lsts.erase(litr);
                            break;
                        }
                    }
                }
                for(size_t r = 0; r < numRows; ++r) {
                    for (auto litr = lsts.begin(); litr != lsts.end(); ++litr) {
                        if (fuzzyMatchRow(m1, r, *litr)) {
                            m1[r] = *litr;
                            lsts.erase(litr);
                            break;
                        }
                    }
                }

                if (lsts.empty()) {
                    matrix = m1;
                    matrixFilled = true;
                    break;
                }
            }
            if (matrixFilled) break;
        }


        // Turn matrix into list of rows and cols
        vector< vector<int> > fullList;

        for (const auto& r : matrix) {
            fullList.push_back(r);
        }

        for (size_t i = 0; i < numRows; ++i) {
            fullList.push_back(copyCol(matrix, i));
        }

        for (const auto& l : listsCopy) {
            for (auto fitr = fullList.begin(); fitr != fullList.end(); ++fitr) {
                if (*fitr == l) {
                    fullList.erase(fitr);
                    break;
                }
            }
        }


        if (fullList.size() != 1) {
            cerr << "You still lost - case " << test << endl;
        }

        vector<int> missing = fullList[0];

        cout << "Case #" << test << ": ";
        for (size_t i = 0; i < numRows; ++i) {
            cout << missing[i];
            if (i != numRows - 1) {
                cout << ' ';
            }
        }
        cout << endl;
    }
}
