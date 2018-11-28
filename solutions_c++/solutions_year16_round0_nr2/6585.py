#include <iostream>
#include <string>

int main(void)
{
    int t;
    std::cin >> t;
    for (int c = 0; c < t; ++c) {
        std::string s;
        std::cin >> s;
        const int l = s.length();
        int times = s[0] == '-'?1:0; 
        for (int i = 1; i < l; ++i) {
            if (s[i] == '-' && s[i-1] == '+') {
                times += 2;
            }
        }
        std::cout << "Case #" << c+1 << ": " << times << std::endl;
    }
    return 0;
}
