#include <iostream>
#include <fstream>

void solve(std::ifstream &input, std::ofstream &output)
{
    size_t row1, row2;
    size_t first[17], second[17];
    size_t result;
    size_t k = 0;

    input >> row1;

    for (size_t i = 0; i < 16; ++i) {
        input >> first[i];
    }
    input >> row2;

    for (size_t i = 0; i < 16; ++i) {
        input >> second[i];
    }

    for (size_t i = (row1 - 1) * 4; i < row1 * 4; ++i) {
        for (size_t j = (row2 - 1) * 4; j < row2 * 4; ++j) {
            if (first[i] == second[j]) {
                result = first[i];
                ++k;
            }
        }
    }

    if (k == 0)
        output << "Volunteer cheated!" << std::endl;
    else if (k == 1)
        output << result << std::endl;
    else
        output << "Bad magician!" << std::endl;
}

int main()
{
    std::ifstream input("A-small-attempt0.in.txt");
    std::ofstream output("out.txt");
    size_t t;

    input >> t;

    for (size_t i = 0; i < t; ++i) {
        output << "Case #" << i + 1 << ": ";
        solve(input, output);
    }

    input.close();
    output.close();

    return 0;
}
