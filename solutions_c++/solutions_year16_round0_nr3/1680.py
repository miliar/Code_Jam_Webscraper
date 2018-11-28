#include <stdexcept>
#include <bitset>
bool fullAdder(bool b1, bool b2, bool& carry) {
    bool sum = (b1 ^ b2) ^ carry;
    carry = (b1 && b2) || (b1 && carry) || (b2 && carry);
    return sum;
}

bool fullSubtractor(bool b1, bool b2, bool& borrow) {
    bool diff;

    if (borrow)

    {
        diff = !(b1 ^ b2);
        borrow = !b1 || (b1 && b2);
    } else

    {
        diff = b1 ^ b2;
        borrow = !b1 && b2;
    }

    return diff;
}

template<unsigned int N>
bool bitsetLtEq(const std::bitset<N>& x, const std::bitset<N>& y) {
    for (int i = N - 1; i >= 0; i--)

    {
        if (x[i] && !y[i]) {
            return false;
        }

        if (!x[i] && y[i]) {
            return true;
        }
    }

    return true;
}

template<unsigned int N>
bool bitsetLt(const std::bitset<N>& x, const std::bitset<N>& y) {
    for (int i = N - 1; i >= 0; i--) {
        if (x[i] && !y[i]) {
            return false;
        }

        if (!x[i] && y[i]) {
            return true;
        }
    }

    return false;
}

template<unsigned int N>
bool bitsetGtEq(const std::bitset<N>& x, const std::bitset<N>& y) {
    for (int i = N - 1; i >= 0; i--) {
        if (x[i] && !y[i]) {
            return true;
        }

        if (!x[i] && y[i]) {
            return false;
        }
    }

    return true;
}

template<unsigned int N>
bool bitsetGt(const std::bitset<N>& x, const std::bitset<N>& y) {
    for (int i = N - 1; i >= 0; i--)

    {
        if (x[i] && !y[i]) {
            return true;
        }

        if (!x[i] && y[i]) {
            return false;
        }
    }

    return false;
}

template<unsigned int N>
void bitsetAdd(std::bitset<N>& x, const std::bitset<N>& y) {
    bool carry = false;

    for (int i = 0; i < N; i++)

    {
        x[i] = fullAdder(x[i], y[i], carry);
    }
}

template<unsigned int N>
void bitsetSubtract(std::bitset<N>& x, const std::bitset<N>& y) {
    bool borrow = false;

    for (int i = 0; i < N; i++)

    {
        if (borrow)

        {
            if (x[i])

            {
                x[i] = y[i];
                borrow = y[i];
            } else

            {
                x[i] = !y[i];
                borrow = true;
            }

        } else

        {
            if (x[i])

            {
                x[i] = !y[i];
                borrow = false;
            } else

            {
                x[i] = y[i];
                borrow = y[i];
            }
        }
    }
}

template<unsigned int N>
void bitsetMultiply(std::bitset<N>& x, const std::bitset<N>& y) {
    std::bitset<N> tmp = x;
    x.reset( );

// we want to minimize the number of times we shift and add
    if (tmp.count( ) < y.count( ))

    {
        for (int i = 0; i < N; i++)
            if (tmp[i]) {
                bitsetAdd<N>(x, y << i);
            }
    } else

    {
        for (int i = 0; i < N; i++)
            if (y[i]) {
                bitsetAdd<N>(x, tmp << i);
            }
    }
}

template<unsigned int N>
void bitsetDivide(std::bitset<N> x, std::bitset<N> y,
                  std::bitset<N>& q, std::bitset<N>& r) {
    if (y.none( ))

    {
        throw std::domain_error("division by zero undefined");
    }

    q.reset( );
    r.reset( );

    if (x.none( ))

    {
        return;
    }

    if (x == y)

    {
        q[0] = 1;
        return;
    }

    r = x;

    if (bitsetLt<N>(x, y))

    {
        return;
    }

// count significant digits in divisor and dividend
    unsigned int sig_x;

    for (int i = N - 1; i >= 0; i--)

    {
        sig_x = i;

        if (x[i]) {
            break;
        }
    }

    unsigned int sig_y;

    for (int i = N - 1; i >= 0; i--)

    {
        sig_y = i;

        if (y[i]) {
            break;
        }
    }

// align the divisor with the dividend
    unsigned int n = (sig_x - sig_y);
    y <<= n;
// make sure the loop executes the right number of times
    n += 1;

// long division algorithm, shift, and subtract
    while (n--) {
// shift the quotient to the left
        if (bitsetLtEq<N>(y, r)) {
// add a new digit to quotient
            q[n] = true;
            bitsetSubtract<N>(r, y);
        }

// shift the divisor to the right
        y >>= 1;
    }
}

#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

int main(int argc, char** argv) {
    int times;
    std::cin >> times;

    for (int z = 0; z < times; z++) {
        std::bitset<30> binary;
        int N, J;
        std::cin >> N >> J;

        std::cout << "Case #" << z + 1 << ":" << std::endl;
        std::bitset<30> twopsize;
        twopsize.set(29);
        std::cerr << "tpsize: " << twopsize << std::endl;

        //for (int l = 0; l < size; l++) {
        //bitsetMultiply<30>(twopsize,std::bitset<30>(2));
        //}
        for (std::bitset<30> i = std::bitset<30>(0); bitsetLt<30>(i, twopsize); bitsetAdd<30>(i, std::bitset<30>(1))) {
            //std::cerr << "Now: " << i << std::endl;
            binary = std::bitset<30>(i);
            std::vector<long> divisors_list;

            bool isInvalid = false;

            for (int base = 2; base <= 10; base++) {
                std::bitset<200> number = std::bitset<200>(1);
                std::bitset<200> pow = std::bitset<200>(base);

                for (int index = 0; index < 30; index++) {
                    //number += (binary[index] ? 1 : 0) * pow;
                    if (binary[index]) {
                        bitsetAdd<200>(number, pow);
                    }

                    bitsetMultiply<200>(pow, base);
                }

                bitsetAdd<200>(number, pow);

                std::ifstream prime_file;
                prime_file.open("primes32.txt");
                long long prime;
                bool isPrime = true;

                int wcount = 0;
                while(prime_file >> prime && bitsetLt<200>(std::bitset<200>(prime), number) && wcount < 5000) {
                    std::cerr << "p: " << prime << std::endl;
                    std::bitset<200> quotient, remainder;
                    bitsetDivide<200>(number, prime, quotient, remainder);

                    if (remainder.none()) {
                        divisors_list.push_back(prime);
                        isPrime = false;
                        break;
                    }
                    wcount++;
                }

                if (isPrime == true) {
                    isInvalid = true;
                    break;
                }
            }

            if (isInvalid == false) {
                std::cout << "1" << binary << "1" << " ";

                for (unsigned long m = 0; m < divisors_list.size() - 1; m++) {
                    std::cout << divisors_list[m] << " ";
                }

                std::cout << divisors_list[divisors_list.size() - 1] << std::endl;
                J--;

                if (J == 0) {
                    break;
                }
            }
        }
    }
}
