#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>

void solution(std::ifstream &input, std::ofstream &output)
{
    size_t n;
    size_t res = 0;
    size_t timeline;
    char k;

    input >> n;
    input >> k;
    timeline = (k - '0');

    for (size_t i = 1; i <= n; ++i) {
        input >> k;

        if (timeline < i) {
            res += (i - timeline);
            timeline += (i - timeline);
        }

        timeline += (k - '0');
    }

    output << res << std::endl;
}

int main()
{
    std::ifstream input("A-large.in");
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
