#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

template<class T>
inline T read() {
    T value;
    std::cin >> value;
    return value;
}

struct case_t {
    int number;
    char mark_letter;
    const char* spelling;
};

static const case_t cases[] = {
    {0, 'Z', "ZERO"},
    {6, 'X', "SIX"},
    {8, 'G', "EIGHT"},
    {2, 'W', "TWO"},
    {4, 'U', "FOUR"},
    {5, 'F', "FIVE"},
    {7, 'V', "SEVEN"},
    {3, 'H', "THREE"},
    {1, 'O', "ONE"},
    {9, 'I', "NINE"},
};

int main() {
    int T = read<int>();
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        std::string S = read<std::string>();
        int counters[128] = {0};
        for (char c : S) {
            ++counters[c];
        }
        int results[10] = {0};
        for (int i = 0; i < 10; ++i) {
            const auto& c = cases[i];
            int x = counters[c.mark_letter];
            if (x > 0) {
                results[c.number] += x;
                for (int j = 0; j < strlen(c.spelling); ++j) {
                    counters[c.spelling[j]] -= x;
                }
            }
        }
        for (int c : counters) {
            if (c != 0) {
                fprintf(stderr, "WARNING: something is wrong!\n");
                break;
            }
        }
        std::string result;
        for (int i = 0; i < 10; ++i) {
            for (int j = 0; j < results[i]; ++j) {
                result.push_back('0' + i);
            }
        }
        printf("Case #%d: %s\n", caseNum, result.c_str());
    }
    return 0;
}
