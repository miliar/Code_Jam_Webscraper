#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T;

    std::cin >> T;

    for (int idx = 1; idx <= T; idx ++)
    {
        int flips = 0;
        char prev_char = '-';

        std::string pancakes;
        
        std::cin >> pancakes;
        for (int i = 0 ; i < pancakes.size(); i++) {
            if (pancakes[i] == '-') {
                if (i == 0) {
                    flips++;
                } else if (prev_char != '-') {
                    flips += 2;
                }
            }

            prev_char = pancakes[i];
        }

        std::cout << "Case #" << idx << ": " << flips  << std::endl;
    }

    return 0;
}
