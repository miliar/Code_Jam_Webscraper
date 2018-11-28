#include <iostream>
#include <limits>

int main() {
    int t;
    std::cin >> t;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    std::string pancakes;

    for (int i = 0; i < t; i++) {
        std::getline(std::cin, pancakes);
        pancakes += '+';

        int maneuvers = 0;

        for (int j = 0; j < pancakes.size() - 1; j++) {
            if (pancakes[j] != pancakes[j + 1])
                maneuvers++;
        }

        std::cout << "Case #" << i + 1 << ": " << maneuvers << "\n";
    }
}
