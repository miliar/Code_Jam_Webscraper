#include <iostream>
#include <fstream>
#include <cstdint>
#include <set>

int main(int argc, char** argv) {
    std::ifstream ifile(argv[1]);
    int t = 0;
    ifile >> t;
    for (unsigned int i = 0; i < t; i++) {
        uint64_t n;
        ifile >> n;
        if (n == 0) {
            std::cout << "Case #" << i + 1 << ": INSOMNIA" << std::endl;
            continue;
        }
        int j = 0;

        std::set<int> digits;
        uint64_t tmp = 0;

        while (digits.size() < 10) {
            tmp = j * n;
            while (tmp != 0) {
                int tmp2 = tmp % 10;
                digits.insert(tmp2);
                tmp /= 10;
            }
            j++;
        }
        std::cout << "Case #" << i + 1 << ": " << (j-1)*n << std::endl;
    }
    return 0;
}