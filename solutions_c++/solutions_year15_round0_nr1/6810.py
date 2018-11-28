#include <iostream>
#include <string>

int standing_ovation(std::string people);

int main(void) {
    int num_of_tests;
    std::cin >> num_of_tests;

    for (int i = 1; i <= num_of_tests; ++i) {
        int max_shyness_lvl, people_to_invite;
        std::string people;

        std::cin >> max_shyness_lvl >> people;
        people_to_invite = standing_ovation(people);

        std::cout << "Case #" << i << ": " << people_to_invite << std::endl;
    }

}

int standing_ovation(std::string people) {
    int current_standing_people = 0;
    int people_to_invite = 0;

    for (int shyness_lvl = 1; shyness_lvl < people.length(); ++shyness_lvl) {
        current_standing_people += (people[shyness_lvl - 1] - '0');

        if (people[shyness_lvl] == '0') {
            continue;
        }

        if (current_standing_people < shyness_lvl) {
            int new_round_of_invites = (shyness_lvl - current_standing_people);
            people_to_invite += new_round_of_invites;
            current_standing_people += new_round_of_invites;
        }
    }

    return people_to_invite;
}
