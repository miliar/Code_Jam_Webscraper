#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <iterator>

int main() {
        // Read in the test cases
        int test_count = 0;
        std::cin >> test_count;
        
        std::vector<std::string> inputs;
        inputs.reserve(test_count);
        std::copy_n(std::istream_iterator<std::string>(std::cin), test_count, std::back_inserter(inputs));
        
        for (size_t i = 0; i < inputs.size(); ++i) {
            std::string word;
            // add the first character directly - no choice to be made here
            word += inputs[i][0];
            // for each character after the first in the input string
            for (size_t j = 1; j < inputs[i].size(); ++j) {
                // If the letter is greater (later in the alphabet) or equal insert, otherwise append
                if (inputs[i][j] >= word[0]) {
                    word.insert(word.begin(), inputs[i][j]);
                } else {
                    word.append(1, inputs[i][j]);
                }
            }
            std::cout << "Case #" << (i + 1) << ": " << word << std::endl;
        }
}