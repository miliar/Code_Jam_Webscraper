#include <iostream>

static const char *digits[] = {
    "ZERO",
    "ONE",
    "TWO",
    "THREE",
    "FOUR",
    "FIVE",
    "SIX",
    "SEVEN",
    "EIGHT",
    "NINE"
};

static int uses[10][26] = {0};

bool test(int *out, int digit, int chars[26]) {
    int maxFit = 2000;
    for (int i = 0; i < 26; ++i)
        if (uses[digit][i])
            maxFit = std::min(maxFit, chars[i]/uses[digit][i]);
    
    if (digit == 9) {
        for (int i = 0; i < 26; ++i)
            if (chars[i] > maxFit*uses[digit][i])
                return false;
        out[digit] = maxFit;
        return true;
    } else {
        for (int i = 0; i <= maxFit; ++i) {
            if (test(out, digit + 1, chars)) {
                out[digit] = i;
                return true;
            }
            
            for (int j = 0; j < 26; ++j)
                chars[j] -= uses[digit][j];
        }
        for (int j = 0; j < 26; ++j)
            chars[j] += (maxFit + 1)*uses[digit][j];
        return false;
    }
}

int main() {
    int t;
    std::cin >> t;
    
    for (int i = 0; i < 10; ++i)
        for (int j = 0; digits[i][j]; ++j)
            uses[i][digits[i][j] - 'A']++;
    
    for (int i = 0; i < t; ++i) {
        std::string s;
        std::cin >> s;
        
        int chars[26] = {0};
        for (size_t j = 0; j < s.size(); ++j)
            chars[s[j] - 'A']++;
        
        int result[10] = {0};
        test(result, 0, chars);
        
        std::cout << "Case #" << (i + 1) << ": ";
        for (int j = 0; j < 10; ++j) {
            for (int k = 0; k < result[j]; ++k)
                std::cout << j;
        }
        std::cout << std::endl;
    }
    return 0;
}
