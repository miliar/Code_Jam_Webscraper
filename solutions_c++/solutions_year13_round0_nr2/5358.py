#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>

typedef std::vector<std::string> lawn_t;

void printLawn( const lawn_t& lawn )
{
    for (int i = 0; i < lawn.size(); i++)
    {
        std::cout << lawn[i] << std::endl;
    }
}

bool checkRow( const lawn_t lawn, int row )
{
    for (int i = 0; i < lawn[row].size(); i++)
    {
        if (lawn[row][i] != '1')
        {
            return false;
        }
    }

    return true;
}

bool checkColumn( const lawn_t lawn, int col )
{
    for (int i = 0; i < lawn.size(); i++)
    {
        if (lawn[i][col] != '1')
        {
            return false;
        }
    }

    return true;
}

bool possible( const lawn_t& lawn )
{
    for (int i = 0; i < lawn.size(); i++)
    {
        for (int j = 0; j < lawn[i].size(); j++)
        {
            if (lawn[i][j] == '1')
            {
                if (!checkRow(lawn, i) && !checkColumn(lawn, j))
                {
                    return false;
                }
            }
        }
    }

    return true;
}

int main ( void )
{
    std::ifstream file;

    file.open("lawn-small.in");

    int numTestCases = 0;

    file >> numTestCases;
    //std::cout << "numTestCases " << numTestCases << std::endl;

    for(int i = 1; i <= numTestCases; i++)
    {
        lawn_t lawn;

        int row;
        int col;

        file >> row;
        file >> col;

        std::string trash;
        getline(file, trash);

        //std::cout << "row " << row << " col " << col << std::endl;
        for (int j = 0; j < row; j++)
        {
            std::string temp;
            std::string row;
            getline(file, temp);
            for (int k = 0; k < temp.size(); k++)
            {
                if (temp[k] != ' ')
                {
                    row += temp[k];
                }
            }
            lawn.push_back(row);
        }

        //printLawn(lawn);
        std::cout << "Case #" << i << ": ";
        if (possible(lawn))
        {
            std::cout << "YES";
        }
        else
        {
            std::cout << "NO";
        }

        std::cout << std::endl;
    }

    return 0;
}

