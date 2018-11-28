#include <string>
#include <iostream>

int main( void ) {
    int n;
    std::cin >> n;
    for (int i = 1; i <= n; ++i) {
        std::cout << "Case #" << i << ": ";
        
        std::string s;
        std::cin >> s;
        
        std::string best_string;
        best_string += s[0];
        for(int i = 1; i < s.size(); ++i) {
            if(best_string[0] <= s[i])
                best_string = s[i] + best_string;
            else
                best_string += s[i];
        }
        
        std::cout << best_string << "\n";
    }
}