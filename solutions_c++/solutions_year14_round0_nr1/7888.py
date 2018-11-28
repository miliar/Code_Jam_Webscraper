#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>

void solution(std::ifstream &input, std::ofstream &output)
{
    size_t ans1, ans2;
    size_t cards1[17], cards2[17];
    size_t res;
    size_t k = 0;

    input >> ans1;

    for (size_t i = 0; i < 16; ++i) {
        input >> cards1[i];
    }
    input >> ans2;

    for (size_t i = 0; i < 16; ++i) {
        input >> cards2[i];
    }

    for (size_t i = (ans1 - 1) * 4; i < ans1 * 4; ++i) {
        for (size_t j = (ans2 - 1) * 4; j < ans2 * 4; ++j) {
            if (cards1[i] == cards2[j]) {
                res = cards1[i];
                ++k;
            }
        }
    }

    if (k == 0)
        output << "Volunteer cheated!" << std::endl;
    else if (k == 1)
        output << res << std::endl;
    else
        output << "Bad magician!" << std::endl;
}

int main()
{
    std::ifstream input("A-small-attempt0.in");
    std::ofstream output("out.txt");
    size_t t;

    input >> t;

    for (size_t i = 0; i < t; ++i) {
        output << "Case #" << i + 1 << ": ";
        solution(input, output);
    }

    input.close();
    output.close();

    return 0;
}
