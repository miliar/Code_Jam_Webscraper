#include <iostream>

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(false);
    int nCase = 0;
    std::cin >> nCase;
    for (int i = 1; i <= nCase; ++i) {
        int S_max = 0;
        std::string input;
        std::cin >> S_max;
        std::cin >> input;
        int cumulative = input[0] - '0';
        int diff_max   = 0;
        
        for (int i = 1; i < input.length(); ++i) {
            if (cumulative < i) {
                int diff = i - cumulative;
                if (diff > diff_max) {
                    diff_max = diff;
                }
            }
            cumulative += input[i] - '0';
        }
        
        std::cout << "Case #" << i << ": " << diff_max << std::endl;
    }
}