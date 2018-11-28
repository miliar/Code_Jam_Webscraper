#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <algorithm>

typedef std::vector< std::vector<size_t> > Matrix;

std::ostream&
operator<<(std::ostream& os, const std::vector<size_t>& _vect)
{
    for (size_t i = 0; i < _vect.size(); ++i) {
        os << _vect [i] << " ";
    }
    return (os);
}

bool
checkPattern(const Matrix& _matrix)
{
    bool isPossible = true;
    
    std::vector<size_t> maxRowElements(_matrix.size());
    std::vector<size_t> maxColElements(_matrix[0].size());
    
    for (size_t i = 0; i < _matrix.size(); ++i) {
        size_t maxRowElem = _matrix[i][0];
        for (size_t j = 1; j < _matrix[0].size(); ++j) {
            if (_matrix[i][j] > maxRowElem) {
                maxRowElem = _matrix[i][j];
            }
            maxRowElements[i] = maxRowElem;
        }
    }
    for (size_t j = 0; j < _matrix[0].size(); ++j) {
        size_t maxColElem = _matrix[0][j];
        for (size_t i = 1; i < _matrix.size(); ++i) {
            if (_matrix[i][j] > maxColElem) {
                maxColElem = _matrix[i][j];
            }
            maxColElements[j] = maxColElem;
        }
    }
    for (size_t i = 0; i < _matrix.size() && true == isPossible; ++i) {
        for (size_t j = 0; j < _matrix[0].size() && true == isPossible; ++j) {
            if (_matrix[i][j] < std::min(maxRowElements[i], maxColElements[j])) {
                isPossible = false;
            }
        }
    }
    return (isPossible);
}

void
usage()
{
    std::cout << "Please specify input and output files\n";
}

int
main(int argc, char** argv)
{
    int retValue = EXIT_SUCCESS;
    if (3 > argc) {
        usage();
        retValue = EXIT_FAILURE;
    } else {
        std::ifstream in(argv[1]);
        std::ofstream out(argv[2]);
        if (in.fail()) {
            retValue = EXIT_FAILURE;
        } else {
            size_t numTests = 0;
            in >> numTests;
            for (size_t i = 0; i < numTests; ++i) {
                /// ******************************
                /// read test case[i]
                /// ******************************
                size_t n = 0;
                in >> n;
                size_t m = 0;
                in >> m;
                Matrix matrix(n);
                for (size_t j = 0; j < n; ++j) {
                    matrix[j].resize(m);
                    for(size_t k = 0; k < m; ++k) {
                        size_t item;
                        in >> item;
                        matrix[j][k] = item;
                    }
                }
                
                /// ******************************
                /// process test case[i]
                /// ******************************
                bool isPossible = checkPattern(matrix);
                
                /// ******************************
                /// write result
                /// ******************************
                out << "Case #" << (i+1) << ": " << (isPossible ? "YES" : "NO") << "\n";
            }
        }
        out.close();
        in.close();
    }
    return (retValue);
}