#include <vector>
#include <utility>
#include <algorithm>
#include <iostream>
#include <sstream>

int main()
{
    int t = 0;
    std::cin >> t;
    for (int i = 0; i < t; ++i)
    {
        // contains the pairwise player sums for 4 rows, 4 columns and
        // the two diags.
        std::vector<std::pair<int, int>> board_sums;
        for (int k = 0; k < 10; ++k)
            board_sums.push_back({0, 0});
        std::stringstream ss;
        ss << "Case #" << i + 1 << ": ";
        for (int row = 0; row < 4; ++row)
        {
            for (int col = 0; col < 4; ++col)
            {
                char mark;
                std::cin >> mark;
                std::pair<int, int> to_add({0, 0});
                switch (mark)
                {
                case 'X': 
                    to_add.first += 1;
                    break;
                case 'O':
                    to_add.second += 1;
                    break;
                case 'T':
                    to_add.first += 1;
                    to_add.second += 1;
                    break;
                }
                // update row sum
                board_sums[row].first += to_add.first;
                board_sums[row].second += to_add.second;
                // update column sum
                board_sums[col + 4].first += to_add.first;
                board_sums[col + 4].second += to_add.second;
                // update diags
                if (row == col) // diag
                {
                    board_sums[8].first += to_add.first;
                    board_sums[8].second += to_add.second;
                }
                else if (row + col == 3) // anti diag
                {
                    board_sums[9].first += to_add.first;
                    board_sums[9].second += to_add.second;
                }
            }
        }
        if (std::any_of(board_sums.begin(), board_sums.end(), 
                        [](std::pair<int, int> pair)
                            {return pair.first == 4;}))
        {
            ss << "X won";
        }
        else if (std::any_of(board_sums.begin(), board_sums.end(),
                             [](std::pair<int, int> pair)
                                {return pair.second == 4;}))
        {
            ss << "O won";
        }
        else if (std::all_of(board_sums.begin(), board_sums.end(),
                             [](std::pair<int, int> pair)
                                {return (pair.first + pair.second) >= 4;}))
        {
            ss << "Draw";
        }
        else
        {
            ss << "Game has not completed";
        }
        std::cout << ss.str() << std::endl;
    }
    return 0;
}

