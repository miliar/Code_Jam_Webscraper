#include <iostream>
#include <fstream>
#include <vector>
#include <string>

bool empty;


std::string status(const std::vector<std::vector<char> >& matrix);
int main()
{
    std::fstream in("in.txt"), out("out.txt");
    std::vector<std::vector<char> > matrix(4, std::vector<char>(4));
    int cases = 0;
    in >> cases;
    std::cout << cases << " cases" << std::endl;
    for (int i = 1; i <= cases; ++i)
    {
        empty = false;
        for (int a = 0; a < 4; ++a)
        {
            for (int b = 0; b < 4; ++b)
            {
                in >> matrix[a][b];
                std::cout << matrix[a][b];
                empty = empty || matrix[a][b] == '.';
                //std::cout << empty;
            }
            //in.ignore('\n');
            std::cout << std::endl;
        }
        //in.ignore('\n');
        std::cout << std::endl;
        out << "Case #" << i << ": " << status(matrix) << std::endl;
    }
    in.close();
    out.close();
    return 0;
}


std::string status(const std::vector<std::vector<char> >& matrix)
{
    char player;

    for (int a = 0; a < 4; ++a)
    {
        if (matrix[a][0] == '.')
            continue;
        player = matrix[a][0];
        for (int b = 1; b < 4; ++b)
        {
            //std::cout << player << a << b << std::endl;
            if (matrix[a][b] == '.')
                break;
            if (player == 'T')
                player = matrix[a][b];
            if (matrix[a][b] != player && matrix[a][b] != 'T')
                break;
            if (b == 3)
                return std::string(1, player) + " won";
        }
    }

    for (int b = 0; b < 4; ++b)
    {
        if (matrix[0][b] == '.')
            continue;
        player = matrix[0][b];
        for (int a = 1; a < 4; ++a)
        {
            if (matrix[a][b] == '.')
                break;
            if (player == 'T')
                player = matrix[a][b];
            if (matrix[a][b] != player && matrix[a][b] != 'T')
                break;
            if (a == 3)
                return std::string(1, player) + " won";
        }
    }

    player = matrix[0][0];
    for (int a = 0; a < 4; ++a)
    {
        if (matrix[a][a] == '.')
                break;
        if (player == 'T')
            player = matrix[a][a];
        if (matrix[a][a] != player && matrix[a][a] != 'T')
            break;
        if (a == 3)
            return std::string(1, player) + " won";
    }

    player = matrix[0][3];
    for (int a = 0; a < 4; ++a)
    {
        std::cout << player << a << 3-a << std::endl;
        if (matrix[a][3-a] == '.')
                break;
        if (player == 'T')
            player = matrix[a][3-a];
        if (matrix[a][3-a] != player && matrix[a][3-a] != 'T')
            break;
        if (a == 3)
            return std::string(1, player) + " won";
    }

    return empty ? "Game has not completed" : "Draw";
}
