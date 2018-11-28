#include <iostream>

int main() {
    int _; std::cin >> _;
    for (int z = 1; z <= _; z++) {
        int maxShyness; std::cin >> maxShyness;
        std::cin.get();
        std::string people; std::getline(std::cin, people);
        int numStanding = 0;
        int addedFriends = 0;
        for (int i = 0; i <= maxShyness; i++) {
            if (numStanding < i) {
                addedFriends += (i - numStanding);
                numStanding = i;
            }
            numStanding += people[i] - '0';
        }
        std::cout << "Case #" << z << ": " << addedFriends << std::endl;
    }

    return 0;
}
