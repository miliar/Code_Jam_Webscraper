#include <bits/stdc++.h>

unsigned next() {
    unsigned Smax;
    std::cin >> Smax;

    std::string input;
    std::cin >> input;

    unsigned ret = 0;

//4 11111
//1 09
//5 110011
//0 1

    unsigned curr = 0;

    for(std::string::iterator it = input.begin(); it != input.end(); ++it) {
        unsigned i = std::distance(input.begin(), it);

        if(i > curr) {
            ret += i - curr;
            curr = i;
        }

        curr += *it - '0';
    }

    return ret;
}

int main(int argc, char *argv[]) {
    unsigned TC;
    std::cin >> TC;

    for(unsigned TCi = 1; TCi <= TC; ++TCi) {
        std::cout << "Case #" << TCi << ": " << next() << std::endl;
    }

    return 0;
}
