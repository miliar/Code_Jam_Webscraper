#include <iostream>
#include <fstream>
unsigned nextPowerOf2(unsigned v) {
    --v;
    v |= v >> 1;
    v |= v >> 2;
    v |= v >> 4;
    v |= v >> 8;
    v |= v >> 16;
    return ++v;
}

int main(int argc, const char* argv[])
{
    if (argc != 2) {
        std::cout << "Missing file containing input\n";
        return -1;
    }

    std::ifstream istr(argv[1]);

    // Read in the number of test cases.
    unsigned T;
    istr >> T;

    for (unsigned i = 1; i <= T; ++ i) {
        unsigned A;
        unsigned B;
        unsigned K;
        istr >> A;
        istr >> B;
        istr >> K;

        unsigned num = 0;
        if (A < K || B < K) {
            num = A*B;
        } else {
            num = A*K + B*K - K*K;
            for (unsigned a = K; a < A; ++a) {
                for (unsigned b = K; b < B; ++b) {
                    if ((a&b) < K) {
                        ++num;
                    }
                }
            }
        }

        std::cout << "Case #" << i << ": " << num << '\n';
    }

    return 0;
}
