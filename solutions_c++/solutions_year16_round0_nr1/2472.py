
#include <vector>
#include <array>
#include <iostream>
#include <fstream>
#include <string>

void addDigits(std::vector<int>& digits, std::vector<int> const& term) {
    int digits_length = digits.size();

    for (int i = 0; i < digits_length - 1 && i < term.size(); i++) {
        digits[i] += term[i];

        if(digits[i] >= 10) {
            digits[i] -= 10;
            digits[i + 1] += 1;
        }
    }

    digits[digits_length - 1] += term.size() == digits_length ? term[digits_length - 1] : 0;

    if(digits[digits_length - 1] >= 10) {
        digits[digits_length - 1] -= 10;
        digits.push_back(1);
    }
}

int digitsToValue(std::vector<int> const& digits) {
    int base = 10;
    int curr_mul = 1;

    int value = 0;

    for(auto d : digits) {
        value += curr_mul * d;
        curr_mul *= base;
    }

    return value;
}


void addSeen(std::array<bool, 10>& seen, std::vector<int> digits) {
    for(auto d : digits) {
        seen[d] = true;
    }
}

int solveInstance(std::vector<int> digits) {
    std::vector<int> term = digits;

    std::array<bool, 10> seen;
    std::fill(seen.begin(), seen.end(), false);

    addSeen(seen, digits);

    while(!std::all_of(seen.begin(), seen.end(), std::identity<bool>())) {
        addDigits(digits, term);
        addSeen(seen, digits);
    }

    return digitsToValue(digits);
}

int main(int argc, char** argv) {
    std::ifstream stream(argv[1]);

    std::string line;


    std::getline(stream, line);

    int T = atoi(line.c_str());

    for(int i = 0; i < T; ++i) {
        std::getline(stream, line);

        std::vector<int> number(line.size());

        std::transform(line.begin(), line.end(), number.rbegin(), [](char c) { return c - '0';});

        if(digitsToValue(number) != 0) {
            auto solution = solveInstance(number);
            std::cout << "Case #" << i + 1 << ": " << solution << std::endl;
        }
        else {
            std::cout << "Case #" << i + 1 << ": " << "INSOMNIA" << std::endl;
        }

    }

    return 0;
}