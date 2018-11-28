#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <iterator>
#include <cstdint>
#include <tuple>

bool find_num(std::string& haystack, const std::string& needle) {
    std::vector<size_t> posns;
    //std::cout << "DEBUG: searching '" << haystack << "' for '" << needle << "'" << std::endl;
    size_t pos = haystack.find(needle[0]);
    bool found = pos != std::string::npos;
    if (found) {
        for (auto& c : needle) {
            haystack[haystack.find(c)] = '0';
        }
    }
    return found;
}

int main() {
    // Read in the test cases
    int test_count = 0;
    std::cin >> test_count;
    
    std::vector<std::string> inputs;
    inputs.reserve(test_count);
    std::copy_n(std::istream_iterator<std::string>(std::cin), test_count, std::back_inserter(inputs));
    
    for (size_t i = 0; i < inputs.size(); ++i) {
        auto& current = inputs[i];
        //std::cout << "DEBUG: starting case " << (i + 1) << ", current=" << current << std::endl;
        std::vector<int> nums;
        // first pass, pick out easy nums
        std::vector<std::tuple<std::string, int>> first_pass = {std::make_tuple("ZORE", 0), std::make_tuple("WTO", 2), 
            std::make_tuple("URFO", 4), std::make_tuple("XSI", 6), std::make_tuple("GHTIE", 8)};
        
        for (auto& s : first_pass) {
            //std::cout << "DEBUG: checking for num " << std::get<0>(s) << std::endl;
            auto posns = find_num(current, std::get<0>(s));
            while (posns) {
                //std::cout << "DEBUG: found num " << std::get<1>(s) << std::endl;
                nums.push_back(std::get<1>(s));
                posns = find_num(current, std::get<0>(s));
            }
        }
        // second pass, pick out harder nums
        std::vector<std::tuple<std::string, int>> second_pass = {std::make_tuple("ONE", 1), std::make_tuple("RHTEE", 3), std::make_tuple("FVIE", 5), std::make_tuple("SVNEE", 7)};
    
        for (auto& s : second_pass) {
            //std::cout << "DEBUG: checking for num " << std::get<0>(s) << std::endl;
            auto posns = find_num(current, std::get<0>(s));
            while (posns) {
                //std::cout << "DEBUG: found num " << std::get<1>(s) << std::endl;
                nums.push_back(std::get<1>(s));
                posns = find_num(current, std::get<0>(s));
            }
        }
        // third pass, pick out NINE
        {
            auto posns = find_num(current, "NNIE");
            while (posns) {
                nums.push_back(9);
                posns = find_num(current, "NNIE");
            }
        }
        std::sort(nums.begin(), nums.end());
        
        std::cout << "Case #" << (i + 1) << ": ";
        for (auto n : nums) {
            std::cout << n;
        }
        std::cout << std::endl;
    }
    
    return 0;
}