#include <iostream>
#include <fstream>
#include <vector>

size_t solve(std::vector<size_t> testcase) {
    if (testcase.size() == 0 || testcase.size() == 1)
        return 0;

    size_t num = 0;
    size_t needed = 0;

    for (size_t shyness = 0; shyness < testcase.size(); ++shyness) {
        if (num < shyness) {
            needed += shyness - num;
            num += shyness - num;
        }
        num += testcase[shyness];
    }

    return needed;
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
        ++size;
        testcases.push_back(std::vector<size_t>());

        for (size_t j = 0; j < size; ++j) {
            char t = 0;
            ifs >> t;
            testcases[i].push_back(t - '0');
        }
    }

    for (size_t i = 0; i < testcases.size(); ++i) {
        size_t num = solve(testcases[i]);
        std::cout << "Case #" << (i + 1) << ": " << num << std::endl;
    }
}
