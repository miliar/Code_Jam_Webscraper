#include <iostream>
#include <string>
#include <map>

int main() {
        int testCases = 0;
        int arg1 = 0;
        int result = 0;
        std::cin >> testCases;

        for ( int i = 1; i <= testCases; ++i ) {
                std::map<int, bool> results;
                int multiplier = 0;
                std::cin >> arg1;

                if ( arg1 == 0 ) {
                        std::cout << "Case #" << i << ": INSOMNIA" << std::endl;
                        continue;
                }

                while ( ++multiplier ) {
                        std::string s = std::to_string(arg1 * multiplier);
                        for ( int j = 0; j <= 9; ++j ) {
                                if ( s.find_first_of( 0x30 + j ) != std::string::npos ) {
                                        results[j] = true;
                                }
                        }

                        // check map
                        if ( results.size() == 10 ) {
                                break;
                        }
                }
                std::cout << "Case #" << i << ": " << arg1 * multiplier << std::endl;
        }

        return 0;
}
