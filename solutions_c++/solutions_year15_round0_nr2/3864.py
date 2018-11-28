#include <iostream>
#include <fstream>
#include <vector>

std::vector<size_t> eat(const std::vector<size_t> testcase) {
    std::vector<size_t> result;

    for (auto &x : testcase)
        if (x > 1)
            result.push_back(x - 1);

    return result;
}

std::vector<size_t> distribute(std::vector<size_t> testcase, const size_t index, const size_t num) {
    std::vector<size_t> result = testcase;
    result.push_back(num);
    result[index] -= num;
    return result;
}

size_t solve(std::vector<size_t> testcase) {
    if (testcase.size() == 0)
        return 0;

    size_t max = 0;
    size_t max_index = 1001;
    for (size_t i = 0; i < testcase.size(); ++i) {
        size_t x = testcase[i];

        if (x > max) {
            max = x;
            max_index = i;
        }
    }

    std::vector<size_t> eaten = eat(testcase);
    size_t eat_time = solve(eaten);

    if (max <= 2)
        return 1 + eat_time;

    std::vector<size_t> initial = distribute(testcase, max_index, max / 2);
    size_t initial_time = solve(initial);
    size_t min = initial_time;

    for (size_t i = max / 2 - 1; i > 1; --i) {
        std::vector<size_t> d = distribute(testcase, max_index, i);
        size_t time = solve(d);
        min = std::min(min, time);
        if (time > initial_time)
            break;
    }

    return 1 + std::min(eat_time, min);
}

int main(int argc, char** argv) {
    std::ifstream ifs;

    ifs.open(argv[1], std::ifstream::in);

    size_t num_testcases = 0;
    ifs >> num_testcases;

    std::vector<std::vector<size_t> > testcases;
    

    for (size_t i = 0; i < num_testcases; ++i) {
        size_t size = 0;
        ifs >> size;
        testcases.push_back(std::vector<size_t>());

        for (size_t j = 0; j < size; ++j) {
            size_t t = 0;
            ifs >> t;
            testcases[i].push_back(t);
        }
    }

    for (size_t i = 0; i < testcases.size(); ++i) {
        size_t num = solve(testcases[i]);
        std::cout << "Case #" << (i + 1) << ": " << num << std::endl;
    }
}
