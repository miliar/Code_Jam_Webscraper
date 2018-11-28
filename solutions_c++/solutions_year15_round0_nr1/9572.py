// standing-ovation.cpp
//
#include <iostream>
#include <string>
#include <cassert>

int main(int argc, char* argv[])
{
    int testcases = 0;
    std::cin >> testcases;
    for (int t = 1; t <= testcases; ++t) {
        int s_max = 0;
        std::string shyness;
        std::cin >> s_max >> shyness;
        assert(shyness.length() <= s_max + 1);
        
        int invited = 0;
        int total = 0;
        for (int s = 0; s < shyness.length(); ++s) {
            int k = shyness[s] - '0';
            if (total < s) {
                invited += (s - total);
                total = s;
            }
            total += k;
        }

        std::cout << "Case #" << t << ": " << invited << '\n';
    }
}
