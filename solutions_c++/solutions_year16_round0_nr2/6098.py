#include <iostream>
#include <string>

std::string generate_happy_stack(int n) {
    return std::string().assign(n, '+');
}

int get_number_flips(std::string p) {
    // check top pancake's mood
    // flip all following pancakes that have the same mood
    // repeat until no more sad pancakes
    std::string target = generate_happy_stack(p.length());
    int nb_flips = 0;
    
    while (p != target) {
        char first_mood = p[0];
        int last_pos_to_flip;
        auto first_opposite_pos = p.find_first_of(first_mood == '-' ? '+' : '-');
        if (first_opposite_pos == std::string::npos) {
            // all pancakes have the same mood, flip them all!
            last_pos_to_flip = p.length() - 1;
        } else {
            // flip all until the first opposite one (not included)
            last_pos_to_flip = first_opposite_pos - 1;
        }
        // perform flip
        nb_flips++;
        std::string old(p);
        for (int i = 0; i < last_pos_to_flip + 1; i++) {
            p[i] = old[last_pos_to_flip - i];
            if (p[i] == '-') {
                p[i] = '+';
            } else {
                p[i] = '-';
            }
        }
    }
    return nb_flips;
}

int main() {
    int t;
    std::string p; // pancake stack
    std::cin >> t;  // read T
    for (int i = 1; i <= t; ++i) {
        std::cin >> p;  // read p
        std::cout << "Case #" << i << ": " << get_number_flips(p) << std::endl;
    }
}
