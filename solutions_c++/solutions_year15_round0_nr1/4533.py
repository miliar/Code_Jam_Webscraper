#include <iostream>
#include <iomanip>
int main () {
    int T;
    std::cin >> T;

    for (int test = 1; test <= T; ++test) {
        int S_max;
        std::cin >> S_max;
        int extra_invitations = 0;
        int buffer = 0;
        for (int i = 0; i < S_max + 1; ++i) {
            char num_S_i;
            std::cin >> num_S_i;
            buffer += (num_S_i-'0');

            if (buffer == 0){
                ++extra_invitations;
            } 
            else {
                --buffer;
            }
        }
        std::cout << "Case #" << test << ": ";
        std::cout << extra_invitations << std::endl;
    }
}