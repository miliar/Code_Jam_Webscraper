#define _SCL_SECURE_NO_WARNINGS

#include <vector>
#include <algorithm>
#include <functional>
#include <fstream>
#include <string>
#include <iostream>

int solveInstanceImpl(bool* pancakes, int length, int flips) {
    if(length == 0) {
        return flips;
    }

    if (pancakes[0]) {
        auto it = std::find(pancakes, pancakes + length, false);

        std::fill(pancakes, it, false);

        flips += 1;
    }

    auto it = std::find(pancakes, pancakes + length, true);
    int newLength = pancakes + length - it;

    std::reverse(pancakes, pancakes + length);
    std::transform(pancakes, pancakes + newLength, pancakes, std::logical_not<>());

    return solveInstanceImpl(pancakes, newLength, flips + 1);
}

int solveInstance(bool* pancakes, int length) {
    int newLength;

    for(newLength = length; newLength > 0; newLength--) {
        if(!pancakes[newLength - 1]) {
            break;
        }
    }

    return solveInstanceImpl(pancakes, newLength, 0);
}


int main(int argc, char** argv) {
    std::ifstream  stream(argv[1]);

    int instanceCount;

    std::string line;

    std::getline(stream, line);

    instanceCount = atoi(line.c_str());

    for(int i = 0; i < instanceCount; ++i) {
        std::getline(stream, line);
        int length = line.size();
        bool* arr = new bool[length];

        std::transform(line.begin(), line.end(), arr, [](char c) { return c == '+';});

        int result = solveInstance(arr, length);
        delete[] arr;

        std::cout << "Case #" << i + 1 << ": " << result << '\n';
    }
}