#include <cstdint>
#include <iterator>
#include <iostream>
#include <vector>
#include <algorithm>
#include <bitset>



int main() {
    // Read in the test cases
    int test_count = 0;
    std::cin >> test_count;
    
    std::vector<uint64_t> inputs;
    inputs.reserve(test_count);
    std::copy_n(std::istream_iterator<uint64_t>(std::cin), test_count, std::back_inserter(inputs));
    
    // For each test case
    for (size_t i = 0; i < inputs.size(); ++i) {
        auto& v = inputs[i];
        // Special case for 0, doesn't diverge so causes insomnia
        if (v == 0) {
            std::cout << "Case #" << (i + 1) << ": INSOMNIA" << std::endl;
        } else {
            // Generate incrementing sequence N, 2N, 3N, ...
            uint64_t num = 0;
            std::bitset<10> seen_digits;
            while (!seen_digits.all()) {
                num += v;
                uint64_t num_copy = num;
                // Check each digit
                while (num_copy > 0) {
                    size_t digit = num_copy % 10;
                    num_copy /= 10;
                    seen_digits.set(digit);
                }
            }
            std::cout << "Case #" << (i + 1) << ": " << num << std::endl;
        }
    }
    
    /* code */
    return 0;
}