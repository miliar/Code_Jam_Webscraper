#include <cstdlib>
#include <iostream>
#include <set>
#include <vector>

void solve(unsigned int N) {
    unsigned int cur_N = N;
    std::set<unsigned int> digits;

    if(N == 0) {
        std::cout << "INSOMNIA" << std::endl;
        return;
    }

    while(digits.size() != 10) {
        unsigned int tmp_N = N;
        do {
            digits.insert(tmp_N % 10);
            tmp_N /= 10;
        } while(tmp_N != 0);
        N += cur_N;
    }
    std::cout << N - cur_N << std::endl;
}

int main() {
    unsigned int nb_entries;
    std::vector<unsigned int> test_cases;

    std::cin >> nb_entries;
    test_cases.reserve(nb_entries);
    for(unsigned int i = 0 ; i < nb_entries ; i++) {
        unsigned int cur_case;

        std::cin >> cur_case;
        test_cases.push_back(cur_case);
    }

    for(std::vector<unsigned int>::size_type i = 0 ; i < test_cases.size() ; i++) {
        std::cout << "Case #" << (i + 1) << ": ";
        solve(test_cases[i]);
    }

    return EXIT_SUCCESS;
}
