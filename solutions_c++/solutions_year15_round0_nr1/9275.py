#include <iostream>
#include <cstdint>

int main(int argc, char *argv[]) {
    int32_t test_count;
    std::cin >> test_count;
    for (int32_t tindex = 1; tindex <= test_count; ++tindex) {
        int32_t n;
        char ch;
        std::cin >> n;
        int32_t fcount = 0;
        int32_t acc = 0;
        for (int32_t i = 0; i <= n; ++i) {
            std::cin >> ch;
            ch -= '0';
            // std::cout << (int)ch << std::endl;
            // std::cout << ">" << i - acc - fcount << std::endl;
            if (ch > 0 && i - (acc+fcount) > 0) {
                fcount += i - (acc+fcount);
            }
            acc += ch;
        }
        std::cout << "Case #" << tindex << ": " << fcount << std::endl;
    }
    return 0;
}
