#include <iostream>
#include <list>

std::string last_word(std::string input) {
    std::list<char> output;
    for(char c : input) {
        if(output.empty() || (c >= output.front())) {
            output.push_front(c);
        } else {
            output.push_back(c);
        }
    }
    return std::string(output.begin(), output.end());
}

int main(int argc, char **argv) {
    unsigned int u, T;
    std::string s;
    
    std::cin >> T;
    for(u = 0; u < T; ++u) {
        std::cin >> s;
        std::cout << "Case #" << u + 1 << ": " << last_word(s) << std::endl;
    }
    
    
    return 0;
}
