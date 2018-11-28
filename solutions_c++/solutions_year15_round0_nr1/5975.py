#include <iostream>
#include <string>

int main(int argc, char **argv) {
    int T = 0;
    std::cin >> T;
    for (int x = 0; x < T; ++x) {
        int Smax = 0, y = 0, z = 0;
        std::string S = "";
        std::cin >> Smax >> S;
        for (int i = 0; i < Smax + 1; ++i) {
            int Si = S[i] - '0';
            if (Si > 0) {
                if (z < i) {
                    y += i - z;
                    z = i;
                }
                z += Si;
            }
        }
        std::cout << "Case #" << x + 1 << ": " << y << std::endl;
    }
    return 0;
}
