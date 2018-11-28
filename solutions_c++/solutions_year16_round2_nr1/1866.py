#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main () {
    
    uint32_t T;
    uint32_t number;
    std::vector<uint32_t> digits(10,0);

    std::cin >> T;
    for (uint32_t t = 1; t <= T; ++t) {
    	std::string code;
    	std::cin >> code;
    	digits[0] = std::count(code.begin(),code.end(),'Z');
    	digits[2] = std::count(code.begin(),code.end(),'W');
    	digits[4] = std::count(code.begin(),code.end(),'U');
    	digits[6] = std::count(code.begin(),code.end(),'X');
    	digits[8] = std::count(code.begin(),code.end(),'G');

    	digits[3] = std::count(code.begin(),code.end(),'T') - digits[2] - digits[8];
    	digits[5] = std::count(code.begin(),code.end(),'F') - digits[4];
    	digits[7] = std::count(code.begin(),code.end(),'V') - digits[5];
    	digits[9] = std::count(code.begin(),code.end(),'I') - digits[5] - digits[6] - digits[8];
    	digits[1] = std::count(code.begin(),code.end(),'O') - digits[0] - digits[2] - digits[4];
    	 
    	
    	


    	std::cout << "Case #" << t << ": ";
    	for (uint32_t i = 0; i < digits.size(); ++i) {
    		if (digits[i] != 0) {
    			for (uint32_t j = 0; j < digits[i]; ++j) {
    				std::cout << i;
    			}
    		}
    	}
    	std::cout << std::endl;
    }
    return 0;
}