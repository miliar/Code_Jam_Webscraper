#include <iostream>
#include <string>
#include <algorithm>

int main() {
        int testCases = 0;
        std::string arg1;
        std::cin >> testCases;
        for ( int i = 1; i <= testCases; ++i ) {
                std::cin >> arg1;
                int turns = 0;

                char prevChar = arg1[0];
                int plusBlock = 0;
                int minusBlock = 0;
                for (int currentPos = 0; currentPos < arg1.size(); ++currentPos) {
                        if ( arg1[currentPos] != prevChar ) {
                                if ( prevChar == '+' ) {
                                        ++plusBlock;
                                } else {
                                        ++minusBlock;
                                }
                                prevChar = arg1[currentPos];
                        }
                }

                if ( prevChar == '+' ) {
                        ++plusBlock;
                } else {
                        ++minusBlock;
                }

//std::cout<< "@@@ turns=" << turns << " " << arg1 << std::endl;
                if ( minusBlock > plusBlock ) {
                        std::for_each( arg1.begin(), arg1.end(), [](char &c) { c = (c == '+') ? '-' : '+'; });
                        ++turns;
//std::cout<< "@@@ turns=" << turns << " " << arg1 << std::endl;
                }

                while ( std::count( arg1.begin(), arg1.end(), '+' ) != arg1.size() ) {
                        int pos = arg1.find_first_of( '-' );
                        if ( pos == 0 ) {
                                pos = arg1.find_first_of( '+' );
                                if ( pos == std::string::npos ) {
                                        pos = arg1.size();
                                }
                        }
                        std::for_each( arg1.begin(), arg1.begin() + pos, [](char &c) { c = (c == '+') ? '-' : '+'; });
                        ++turns;
//std::cout<< "@@@ turns=" << turns << " " << arg1 << std::endl;
                }
                std::cout << "Case #" << i << ": " << turns << std::endl;
        }

        return 0;
}
