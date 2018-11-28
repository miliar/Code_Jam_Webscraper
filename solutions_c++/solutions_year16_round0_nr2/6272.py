#include <iostream>
#include <cstdio>
#include <string>

int countFlips(std::string s) {
    int flips = 0;
    for (int i = 0; i < s.size(); ++i) {
        if(s[i] == '-') {
            ++flips;
            //goto the last blank side that can be flipped
            while(i < s.size() && s[i] == '-')
                ++i;
            //flip all the stacks from top
            int j = i - 1;
            while (j >= 0) {
                s[j] = (s[j] == '-') ? '+' : '-';
                j--;
            }
            //back to top T.T (can be optimized)
            i = -1;
        }
    }
    return flips;
}

int main( void ) {
    int n;
    std::cin >> n;
    for (int i = 1; i <= n; ++i) {
        std::string s;
        std::cin >> s;
        printf("Case #%d: %d\n", i, countFlips(s));
    }
}