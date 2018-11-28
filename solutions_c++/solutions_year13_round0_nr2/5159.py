#include <fstream>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <sstream>

// Usage:
// cat input.txt | ./main > output.txt
// ./main input.txt > output.txt
// ./main input.txt output.txt

void processAllCases(std::istream &is, std::ostream &os);
void processCase(const int iteration, std::istream &is, std::ostream &os);

int main(int argc, char *argv[]) {
    std::ostream* os;
    std::istream* is;
    std::ofstream fout;
    std::ifstream fin;
    switch(argc) {
        case 1:
            os = &std::cout;
            is = &std::cin;
            break;
        case 2:
            fin.open(argv[1]);
            is = &fin;
            os = &std::cout;
            break;
        case 3:
            fin.open(argv[1]);
            is = &fin;
            fout.open(argv[2]);
            os = &fout;
            break;
        default:
            std::cout
                << "Usage:" << std::endl
                << "cat input.txt | ./main > output.txt" << std::endl
                << "./main input.txt > output.txt" << std::endl
                << "./main input.txt output.txt" << std::endl;
            return 1;
    }
    processAllCases(*is, *os);
    return 0;
}

// process all cases
void processAllCases(std::istream &is, std::ostream &os)
{
    int totalCases;
    is >> totalCases;
    for(int caseNumber = 1; caseNumber <= totalCases; ++caseNumber)
    {
        processCase(caseNumber, is, os);
    }
}

bool processLawn(std::vector<std::vector<int> > & lawn, int rows, int columns);

// process individual case, caseNumber = 1..totalCases
void processCase(const int caseNumber, std::istream &is, std::ostream &os)
{
    int rows;
    int columns;
    is >> rows;
    is >> columns;
    std::vector<std::vector<int> > lawn;

    for(int i = 0; i < rows; ++i)
    {
        std::vector<int> row;
        for (int j = 0; j < columns; ++j)
        {
            int height;
            is >> height;
            row.push_back(height);

        }

        lawn.push_back(row);
    }
    bool possible = processLawn(lawn, rows, columns);

    os << "Case #" << caseNumber << ": ";
    if (possible)
    {
        os << "YES" << std::endl;
    }
    else
    {
        os << "NO" << std::endl;
    }

}

bool processLawn(std::vector<std::vector<int> > & lawn, int rows, int columns)
{
    int row = 0;
    for(std::vector<std::vector<int> >::iterator it = lawn.begin();
            it != lawn.end();
            ++it)
    {
        int column = 0;
        for(std::vector<int>::iterator it1 = it->begin();
                it1 != it->end();
                ++it1)
        {


            // if there are values more than this points value in both rows and columns then it cannot be possible

            bool columnPossible = true;

            for(int i = 0; i < rows; ++i)
            {
                if (lawn[i][column] > *it1)
                {
                    columnPossible = false;
                    break;
                }
            }

            bool rowPossible = true;
            for(int i = 0; i < columns; ++i)
            {
                if (lawn[row][i] > *it1 )
                {
                    rowPossible = false;
                    break;
                }
            }

            if (!columnPossible && !rowPossible)
            {
                return false;
            }

            ++column;
        }
        ++row;
    }

    return true;

}
