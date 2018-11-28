#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

int flips(string pancakes) {
    const auto n = pancakes.size();
    auto blank = count_if(pancakes.begin(), pancakes.end(), [](char ch) { return ch == '-'; });
    if (blank == 0) { return 0; }
    int count = 0;
    while (blank > 0) {
        ++count;
        char top = pancakes.front();
        auto it = pancakes.begin();
        while (*it == top && it != pancakes.end()) {
            *it = '+' + '-' - *it;
            ++it;
        }
        reverse(pancakes.begin(), it);
        blank = count_if(pancakes.begin(), pancakes.end(), [](char ch) { return ch == '-'; });
    }
    return count;
}

int main(int argc, char **argv) {
    fstream input("/Users/garygaojun/Downloads/codejam/rotp.in", ios_base::in);
    fstream output("/Users/garygaojun/Downloads/codejam/rotp.out", ios_base::out);
    if (!input.is_open()) {
        cout << "fail to open input file" << endl;
        return -1;
    }
    int lines;
    input >> lines;
    for (int i = 1; i <= lines; ++i) {
        string pancakes;
        input >> pancakes;
        output << "Case #" << i << ": " << flips(pancakes) << endl;
    }
    return 0;
}