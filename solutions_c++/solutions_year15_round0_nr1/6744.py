// GCJ 2015
// Qualification Round
// Problem A
// Standing Ovation

// Jonathan Lee


#include <iostream>
#include <vector>
#include <string>


int main() {
    int T;
    std::cin >> T;
    
    std::vector<std::string> cases;
    for(int i = 0; i < T; i++) {
        int s_max;
        std::string audience;
        std::cin >> s_max >> audience;
        cases.push_back(audience);
    }
    
    for(int i = 0; i < T; i++) {
        int friends = 0, clapping = 0;
        std::string audience = cases[i];
        
        for(int s_i = 0; s_i < audience.size(); s_i++) {
            int n = (char)audience[s_i] - '0';
            while(clapping < s_i) {
                friends++;
                clapping++;
            }
            clapping += n;
        }
        
        std::cout << "Case #" << (i + 1) << ": ";
        std::cout << friends << std::endl;
    }
    
    return 0;
}
