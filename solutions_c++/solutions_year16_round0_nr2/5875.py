#include <iterator>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdint>

void flip_pancakes(std::string& v, size_t n) {
    std::reverse(v.begin(), v.begin() + n);
    for (auto it = v.begin(); it != (v.begin() + n) && it != v.end(); ++it) {
        if (*it == '-')
            *it = '+';
        else
            *it = '-';
    }
}

int main() {
    // Read in the test cases
    int test_count = 0;
    std::cin >> test_count;
    
    std::vector<std::string> inputs;
    inputs.reserve(test_count);
    std::copy_n(std::istream_iterator<std::string>(std::cin), test_count, std::back_inserter(inputs));
    
    // For each test case
    for (size_t i = 0; i < inputs.size(); ++i) {
        auto& v = inputs[i];
        size_t checked_pos = v.rfind('-');
        uint64_t move_count = 0;
        while (checked_pos != std::string::npos) {
            // flip all top pancakes that are '+' side up
            size_t top_flip = v.find('-');
            if (top_flip != 0) {
                // if there's at least one + on top
                flip_pancakes(v, top_flip);
                ++move_count;
            }
            
            // flip the stack from the top to the last '-' inclusive
            flip_pancakes(v, checked_pos + 1);
            ++move_count;
            
            // Advance pointer to next '-'
            checked_pos = v.rfind('-', checked_pos - 1);
        }
        std::cout << "Case #" << (i + 1) << ": " << move_count << std::endl;
    }
    
    return 0;
}