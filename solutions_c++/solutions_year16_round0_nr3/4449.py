#include <iostream>
#include <cmath>
#include <bitset>
#include <vector>

bool isPrime( long n ) {
        if ( n <= 1 ) {
                return false;
        } else if ( n <= 3 ) {
        return true;
        } else if ( n % 2 == 0 ||  n % 3 == 0 ) {
        return false;
        }

        long i = 5;
    while ( i * i <= n ) {
                if ( n % i == 0 || n % (i + 2) == 0 ) {
            return false;
                }
        i += 6;
        }

    return true;
}

int main() {
        long testCases = 0;
        long arg1 = 0;
        long arg2 = 0;
        std::cin >> testCases;
        for ( long i = 1; i <= testCases; ++i ) {
                std::cin >> arg1 >> arg2;

                arg1 -= 2;

                std::cout << "Case #" << i << ":" << std::endl;
                std::string maxString(arg1, '1');
                long maxValue = std::stoi( maxString, NULL, 2);
                for ( long j = 1; j <= maxValue; ++j ) {
                        std::bitset<32> input( j );
                        std::string inputStr = input.to_string();
                        inputStr = inputStr.substr( inputStr.size() - arg1, arg1 );

                        std::string s = "1" + inputStr + "1";
                        std::vector<long> factors;
//std::cout << "@@@ j=" << j << " s=" << s << std::endl;
                        for ( long k = 2; k <= 10; ++k ) {
                                long value = std::stol( s, NULL, k);
                                if ( isPrime( value ) ) {
//std::cout << "@@@ isPrime value=" << value << " k=" << k << std::endl;
                                        break;
                                }

//std::cout << "@@@ notPrime value=" << value << " k=" << k << std::endl;
                                long factor = 0;
                                for ( long l = 2; l < value; ++l ) {
//std::cout << "@@@ value=" << value << " l=" << l << std::endl;
                                        if ( value % l == 0 ) {
                                                factor = l;
                                                factors.push_back( factor );
                                                break;
                                        }
                                }
                        }

                        if ( factors.size() == 9 ) {
                                --arg2;
                                std::cout << s << " ";
                                for ( std::vector<long>::const_iterator it = factors.begin(); it != factors.end(); ++it ) {
                                        std::cout << *it << " ";
                                }
                                std::cout << std::endl;

                                if ( arg2 == 0 ) {
                                        break;
                                }
                        }
                }
        }

        return 0;
}
