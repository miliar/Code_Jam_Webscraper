#include <fstream>
#include <unordered_map>
#include <iostream>
#include <string>
using namespace std;

#include <cstdint>
#include <cmath>
#include <cstdio>

bool is_palin(char *str, uint32_t len) {
    for (int left = 0, right = len - 1; left < right; ++left, --right) {
        if (str[left] != str[right]) return false;
    }
    return true;
}

// Actually uses a reverse string, but for palindromes who cares
static unordered_map<uint32_t, bool> m;
static unordered_map<uint32_t, bool>::iterator it;

bool is_palin(uint32_t n) {
    static char buffer[255];

    /*it = m.find(n);
    if (it != m.end()) {
        return it->second;
    }
    */
    int pos = 0;
    while (n != 0) {
        buffer[pos++] = (n % 10);
        n /= 10;
    }
    bool check = is_palin(buffer, pos);
    //m[n] = check;
    return check;
}

bool is_perfect(uint32_t n) {
    return is_palin(n);
}

int main(void) {
    fstream fout("output.txt", fstream::out);

    int T;
    cin >> T;

    for (int case_num = 1; case_num <= T; ++case_num) {
        fout << "Case #" << case_num << ": ";

        uint32_t rangeStart, rangeEnd;
        cin >> rangeStart >> rangeEnd;

        // Change the problem domain, iterate over the roots themselves
        // Find the lowest and highest perfect square roots in the range
        // Then iterate between the two roots, every number in that range is the root of a perfect square
        // Check those for palindromes, then check their square
        
        uint32_t start = ceil(sqrt(rangeStart));
        uint32_t end = floor(sqrt(rangeEnd));
        uint32_t square;
        uint32_t count = 0;
        
        for (uint32_t i = start; i <= end; ++i) {
            square = i * i;
            if (is_palin(i) && is_palin(square)) ++count;
        }
        fout << count << endl;
    }

    return 0;
}
