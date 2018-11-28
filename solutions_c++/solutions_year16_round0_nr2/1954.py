#include <iostream>
#include <cstdio>

int main(int argc, char** argv) {
    int times;
    std::cin >> times;

    for (int i = 0; i < times; i++) {
        int flip_count = 0;
        std::string bitstring;
        std::cin >> bitstring;
        int len = bitstring.length();
        char last_char, curr_char;

        if (len > 0) {
            last_char = bitstring[0];
            curr_char = bitstring[1];
        }

        for (int j = 1; j < len; j++) {
            if (bitstring[j] != bitstring[j - 1]) {
                flip_count++;
            }
        }

        if (bitstring[len - 1] == '-') {
            flip_count++;
        }

        std::cout << "Case #" << i + 1 << ": " << flip_count << std::endl;
    }
}
